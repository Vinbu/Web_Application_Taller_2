import typer
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

app = typer.Typer()
iv = b'3afMoPuzpXwkdoOO'  # default iv to encrypt and decrypt


@app.command()
def encrypt(message: str, key: str) -> str:
    """
    encrypt function will encrypt the message using the key providedddddddddddddddddddddddddddddddddddddddddddddddddddd
    and global iv

    Parameters:
        message (str): Message to be encrypted
        key (str): Key to encrypt the message
    """
    if len(key) != 16:
        raise ValueError("The key must be exactly 16 characters length")

    # parse to bytes
    key = key.encode()
    message = message.encode()
    # encrypt the message
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(message, AES.block_size))
    ciphertext = b64encode(ct_bytes).decode('utf-8')
    print(f"Encrypted Message: {ciphertext}")
    return ciphertext


@app.command()
def decrypt(encode_message: str, key: str) -> str:
    """
    decrypt function will decrypt the message using the key provided,
    encrypted message and global iv

    Parameters:
        encode_message (str): Encrypted message to be decrypted
        key (str): Key to decrypt the message
    """

    try:
        if len(key) != 16:
            raise ValueError("The key must be exactly 16 characters length")
        # parse to bytes
        key = key.encode()
        ct = b64decode(encode_message)

        # decrypt the message
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_message = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

        print("The message was:", decrypted_message)
        return decrypted_message

    except (ValueError, KeyError):
        print("Incorrect decryption")


if __name__ == "__main__":
    app()
