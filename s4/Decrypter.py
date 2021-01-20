from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Encrypter import Encrypter
from LaGrangeInterpolation import LagrangeInterpolation
import hashlib, sys

class Decrypter:
    """
    A class that has decrypting methods
    """
    def __init__(self , cryp_file, shares):
        """
        Construct a decrypter object

        Args:
            cryp_file (str): Encrypted file
            shares (list): List of shares to use
        """
        self.file = cryp_file
        """ Encryted file"""
        self.shares = shares
        """ (list) List of Shares"""
        self.mode = AES.MODE_CBC
        """ mode for AES"""

        
    def decrypt_text(self, text):
        """
        Decrypts a given text

        Args:
            text (str): text to decrypt
            key (str): key to decrypt the text

        Returns:
            str: decrypted text
        """
        iv = text[:AES.block_size]
        password = self.alphanumric_pass(self.key)
        #try:
        cipher = AES.new(password, self.mode, iv)
        decrypted_text = cipher.decrypt(text[AES.block_size:])
        #except:
        #print("Clave incorrecta, no se pudo decifrar el archivo")
        #sys.exit(1)
        
        return unpad(decrypted_text, AES.block_size)
        
    def decipher_file(self):
        """
        Decrypts the encrypted file
        Returns:
            file: Decrypted file
        """
        try:
            with open(self.file, 'rb') as f:
                encrypted_file = f.read()
        except:
            print("There was an error while reading " + str(self.file))
           
        
        secret = self.get_secret() 
        num = str(secret)
        self.key = hashlib.sha256(num.encode('utf-8')).digest()
        """ Recover of the key to decrypt the file"""
        decrypted_text = self.decrypt_text(encrypted_file)        
        return decrypted_text
    
    def get_secret(self):
        """
        Gets the password to decrypt the crypted file
        Returns:
            int: the password to decrypt
        """
        return LagrangeInterpolation.reconstruct_secret(self.shares, 0)
        
    
    def save_decrypted_file(self, new_name):
        """
        Saves the decrypted file
        Args:
            new_name (str): new name for the the decrypted file
        """
        with open(new_name, 'wb') as f:
            f.write(self.decipher_file())
            
    def alphanumric_pass(self, key):
        """
        Applies sha256 to a string

        Args:
            key (str): password 

        Returns:
            str: pass with sha256 applied
        """
        num = str(key)
        return hashlib.sha256(num.encode('utf-8')).digest()