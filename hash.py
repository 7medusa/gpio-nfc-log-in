import hashlib
import binascii

def hash_berechnung(content):
    data = content.strip()  # Entferne Leerzeichen am Anfang und Ende der Zeichenkette
    data_bytes = data.encode('utf-8')#codierung in bytes
    hash_object = hashlib.sha256()#festelgen der hash codierung
    hash_object.update(data_bytes)#codierung der eingabe
    return hash_object.hexdigest()#codierung returnen in hex
