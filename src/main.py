import typer
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json
import os

app = typer.Typer()
iv = b'3afMoPuzpXwkdoOO'

@app.command()
def encrypt(message : str, key: str):
    
    if len(key) != 16:
        raise ValueError("The key must be exactly 16 characters length")
    
    key = key.encode()
    
    message = message.encode()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    ct_bytes = cipher.encrypt(pad(message, AES.block_size))
    
    ciphertext = b64encode(ct_bytes).decode('utf-8')
    
    print(f"Encrypted Message: {ciphertext}")
    
    
@app.command()
def decrypt(encode_message : str, key : str):
    
    try:
        if len(key) != 16:
            raise ValueError("The key must be exactly 16 characters length")
        
        key = key.encode()

        ct = b64decode(encode_message)

        cipher = AES.new(key, AES.MODE_CBC, iv)

        pt = unpad(cipher.decrypt(ct), AES.block_size)

        print("The message was: ", pt.decode('utf-8'))

    except (ValueError, KeyError):

        print("Incorrect decryption")
    
if __name__ == "_main_":
    app()