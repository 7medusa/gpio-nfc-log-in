from mfrc522 import SimpleMFRC522

def write_nfc(data):
    reader = SimpleMFRC522()
    print("data to write:", data)
    reader.write(data)
    print("success")


data = input("input:\n>")
write_nfc(data)
