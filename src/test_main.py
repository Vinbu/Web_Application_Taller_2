from main import encrypt, decrypt
import pytest

def test_encrypt():
    encrypted_message = encrypt("Test message", "1234567890123456")
    assert encrypted_message == "YRNFocfXi5FBg0oR6TEjtg==", "Message not encrypted correctly"
    
def test_decrypt():
    message = decrypt("YRNFocfXi5FBg0oR6TEjtg==", "1234567890123456")
    assert message == "Test message", "Message not decrypted correctly"

def test_invalid_key_length():
    message = "Test message"
    invalid_key = "shortkey"
    
    with pytest.raises(ValueError, match="The key must be exactly 16 characters length"):
        encrypt(message, invalid_key)