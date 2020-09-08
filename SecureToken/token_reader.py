from SecureToken.encryptor import *
from SecureToken.decryptor import *
from Constants.key_constants import access_key

encrypt_msg = encrypt_message(access_key)
decrypt_msg = decrypt_message(encrypt_msg).decode('utf-8')
