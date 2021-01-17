from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Encrypter import Encrypter
import hashlib

class Decrypter:
    def __init__(self, encrypter, cryp_file, key):
        self.iv = encrypter.get_cipherIV()
        self.key = key
        self.cipher =  AES.new(self.key, AES.MODE_CBC, self.iv)
        self.file = cryp_file
        
    def decipher_file(self):
        with open(self.file, 'rb') as f:
            encrypted_file = f.read()
            
        decrypted_file = unpad(self.cipher.decrypt(encrypted_file), AES.block_size)
        
        return decrypted_file
    
    def save_decrypted_file(self, new_name):
        with open(new_name, 'wb') as f:
            f.write(self.decipher_file())
            
            
