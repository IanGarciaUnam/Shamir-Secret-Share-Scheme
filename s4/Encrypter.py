from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import random

class Encrypter:
    def __init__(self, in_file, key):
        self.file = in_file
        self.key = key
        self.mode = AES.MODE_CBC
        self.cipher = AES.new(self.key, self.mode)

        
    def encrypt_file(self):
        with open(self.file, 'rb') as f:
            orig_file = f.read()
        
        
        return self.cipher.encrypt(pad(orig_file, AES.block_size))
    
    def save_encrypted_file(self, out_name):
        with open(out_name, 'wb') as f:
            f.write(self.encrypt_file())
            
    def get_cipherIV(self):
        return self.cipher.iv

