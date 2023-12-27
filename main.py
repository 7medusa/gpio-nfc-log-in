from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from time import sleep
import subprocess
import hash

hash_code = "b0c3fd36b5de1487ecf726db8edc1c05ab8b97f0ee224f9842b27d69844c2f51" #  hash of the password on the nfc_tag
username = "username" #  username, please change this
password = "password" #  in work...

 #  light control beginning
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
green = 21
red = 26
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
def led_on(color):
    GPIO.output(color, GPIO.HIGH)
def led_off(color):
    GPIO.output(color, GPIO.LOW)
 #  light control ending


def read_nfc():
    global nfc_text
    reader = SimpleMFRC522()
    print("waiting...")
    id, nfc_text = reader.read()


def log_in(username, password):
    command = f"echo '{password}' | sudo -S -u {username} bash -c 'echo Login successful'"
    result = subprocess.run(command, shell=True, check=True, text=True, input=password)


if __name__ == "__main__":
    while True:
        read_nfc()
        if str(hash.hash_berechnung(nfc_text)) == hash_code:
            print("correct")
            led_on(green)
            log_in(username, password)
            sleep(5)
            led_off(green)
        else:
            print("wrong")
            led_on(red)
            sleep(5)
            led_off(red)
