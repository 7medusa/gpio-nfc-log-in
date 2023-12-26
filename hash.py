import hashlib
import binascii

def hash_berechnung(content):
    data = content.strip()  # deleting space for the correct hash
    data_bytes = data.encode('utf-8')
    hash_object = hashlib.sha256() #  sha256
    hash_object.update(data_bytes)
    return hash_object.hexdigest()
