from main import encrypt, decrypt
import json, os

def test_encrypt():
    encrypt("Test message", "1234567890123456")
    assert os.path.exists("Encrypted_data.json"), "File not created"
    
def test_decrypt():
    encrypt("Test message", "_=-!@# $%^{}|ab0")
    message = decrypt("_=-!@# $%^{}|ab0")
    assert message == "Test message", "Message not decrypted correctly"
