from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Encrypter import Encrypter
import hashlib

class Decrypter:

    """
    A class that has decrypting methods
    """
    def __init__(self, encrypter, cryp_file, key):
        """
        Constrcut a decrypter method

        Args:
            encrypter (Encrypter): We obtain the IV from the original Encrypter
            cryp_file (str): Encrypted file
            key (str): password from the Encrypter
        """
        self.iv = encrypter.get_cipherIV()
        self.key = hashlib.sha256(key.encode('utf8')).digest()

    def __init__(self, encrypter, cryp_file, key):
        self.iv = encrypter.get_cipherIV()
        self.key = key
        self.cipher =  AES.new(self.key, AES.MODE_CBC, self.iv)
        self.file = cryp_file
        
    def decipher_file(self):
        """
        Decrypts the encrypted file

        Returns:
            file: Decrypted file
        """
        with open(self.file, 'rb') as f:
            encrypted_file = f.read()
            
        decrypted_file = unpad(self.cipher.decrypt(encrypted_file), AES.block_size)
        
        return decrypted_file
    
    def save_decrypted_file(self, new_name):

        """
        Saves the decrypted file

        Args:
            new_name (str): new name for the the decrypted file
        """
        with open(new_name, 'wb') as f:
            f.write(self.decipher_file())
            
            
