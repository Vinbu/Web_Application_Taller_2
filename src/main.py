import typer
from Crypto.Cipher import AES
import json
import os

app = typer.Typer()

@app.command()
def encrypt(message : str, key: str):
    
    key = key.encode()
    
    cipher = AES.new(key, AES.MODE_EAX)
    
    nonce = cipher.nonce
    
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    
    print(f"Encrypted Message: {ciphertext}")
    
    data = {
        "nonce" : nonce.hex(),
        "ciphertext" : ciphertext.hex(),
        "tag" : tag.hex()
    }
    
    with open("Encrypted_data.json", "w") as f:
        json.dump(data, f)
    
    
@app.command()
def decrypt(key : str):
    
    with open("Encrypted_data.json", "r") as f:
        data = json.load(f)
    
    key = key.encode()
    nonce = bytes.fromhex(data['nonce'])
    ciphertext = bytes.fromhex(data['ciphertext'])
    tag = bytes.fromhex(data['tag'])
    
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    
    try:
        cipher.verify(tag)
        decoded_text = plaintext.decode('utf-8')
        print(f"The message is authentic: {decoded_text}")
        
        if os.path.exists("Encrypted_data.json"):
            os.remove("Encrypted_data.json")
        else:
            print("There was an error with data elimination, please verify 'Encrypted_data.json' archive")
        return decoded_text
    except ValueError:
        print("Key incorrect or message corrupted")
    
if __name__ == "__main__":
    app()