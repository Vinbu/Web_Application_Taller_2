from main import encrypt, decrypt
import json, os

def test_encrypt():
    encrypt("Test message", "1234567890123456")
    assert os.path.exists("Encrypted_data.json"), "File not created"
    
def test_decrypt():
    encrypt("Test message", "1234567890123456")
    message = decrypt("1234567890123456")
    decoded_string = message.decode('utf-8')
    assert decoded_string == "Test message", "Message not decrypted correctly"
    
# Test if the JSON file has keys and values
def test_json():
    encrypt("Test message", "1234567890123456")
    with open('Encrypted_data.json', 'r') as file:
        parsed_json = json.load(file)
    assert "nonce" in parsed_json and parsed_json["nonce"], "Missing or empty nonce"
    assert "ciphertext" in parsed_json and parsed_json["ciphertext"], "Missing or empty ciphertext"
    assert "tag" in parsed_json and parsed_json["tag"], "Missing or empty tag"
    os.remove("Encrypted_data.json")