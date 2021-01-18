from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import random

class Encrypter:
    def __init__(self, in_file, key):
        """
        Creates an object that encryptes a file

        Args:
            in_file (str): file to encrypt
            key (str): password
        """
        self.file = in_file
        self.key = hashlib.sha256(key.encode('utf8')).digest()
        self.mode = AES.MODE_CBC
        self.cipher = AES.new(self.key, self.mode)
        
        
    def encrypt_file(self):
        """
        Encrypts the file given

        Returns:
            file: The file encrypted with AES
        """
        self.file = in_file
        self.key = key
        self.mode = AES.MODE_CBC
        self.cipher = AES.new(self.key, self.mode)
        
    def normalize_lenght(self, file):
        while len(file) % 16 != 0:
            file = file + b'0' 
        return file
        
    def encrypt_file(self):
      """
      Encrypt a file readed
      """
        with open(self.file, 'rb') as f:
            orig_file = f.read()
        
        
        return self.cipher.encrypt(pad(orig_file, AES.block_size))
    
    def save_encrypted_file(self, out_name):

        """
        Saves the encrypted file

        Args:
            out_name (str): the new name for the encrypted file
        """

        with open(out_name, 'wb') as f:
            f.write(self.encrypt_file())
            
    def get_cipherIV(self):

        """
        Returns the IV from the cipher

        Returns:
            list: IV from cipher
        """
        return self.cipher.iv
    
        