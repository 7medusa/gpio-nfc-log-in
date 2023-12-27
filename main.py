from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from time import sleep
import subprocess
import hash

hash_code = "14b114aa5fadf41b4caa65f2dd788c0ae04a543231a6fadc7435257299dcec0d" #  hash of the password on the nfc_tag
username = "username" #  username, please change this
password = "normal" #  in work...

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
    command = f"echo '{password}' | sudo -S -u {username} whoami"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        if "Authentication failure" in e.stderr:
            print("error. wrong password")
        else:
            print("unknown error")


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
