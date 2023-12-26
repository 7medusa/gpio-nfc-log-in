import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import hash
from time import sleep

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


def read_nfc():
    global text
    reader = SimpleMFRC522()
    print("Bitte halte eine NFC-Karte vor den Reader...")
    id, text = reader.read()

def write_nfc(data):
    reader = SimpleMFRC522()
    print("Bitte halte eine leere NFC-Karte vor den Reader...")
    print("Schreibe Daten auf die Karte:", data)
    reader.write(data)
    print("Daten erfolgreich geschrieben.")

if __name__ == "__main__":
    while True:
        read_nfc()
        if str(hash.hash_berechnung(text)) == "b0c3fd36b5de1487ecf726db8edc1c05ab8b97f0ee224f9842b27d69844c2f51":
            print("korrekt")
            led_on(green)
            sleep(5)
            led_off(green)
        else:
            print("falsch")
            led_on(red)
            sleep(5)
            led_off(red)
