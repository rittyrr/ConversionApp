"""AES Algorithm used (any preferable encoding can also be used like base64"""

from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it to a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    """NOTE : 'with' keyword is used for exception handling. 
    Advantages of 'with' : 1. It will create the file if it is not present,
     2. The file will get auto-closed after execution"""

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    generate_key()
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message






