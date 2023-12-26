from mfrc522 import SimpleMFRC522

def write_nfc(data):
    reader = SimpleMFRC522()
    print("Bitte halte eine leere NFC-Karte vor den Reader...")
    print("Schreibe Daten auf die Karte:", data)
    reader.write(data)
    print("Daten erfolgreich geschrieben.")


eingabe = input("eingabe:\n>")
write_nfc(eingabe)
