import typer
from Crypto.Cipher import AES
import json

app = typer.Typer()

@app.command()
def encrypt(message : str, key: str):
    
    key = key.encode()
    
    cipher = AES.new(key, AES.MODE_EAX)
    
    nonce = cipher.nonce
    
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    print(f"key: {key}")
    print(f"Encrypted Message: {ciphertext}")
    print(f"nonce: {nonce}, tag: {tag}")
    
    data = {
        'nonce' : nonce.hex(),
        'ciphertext' : ciphertext.hex(),
        'tag' : tag.hex()
    }
    
    with open('Encrypted_data.json', 'w') as f:
        json.dump(data, f)
    
    
@app.command()
def decrypt(key : str):
    print("alsdoanfabf")
    
if __name__ == "__main__":
    app()