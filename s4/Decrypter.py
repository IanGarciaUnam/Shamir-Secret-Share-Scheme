from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Encrypter import Encrypter
from LarangeInterpolation import LagrangeInterpolation
import hashlib

class Decrypter:
    """
    A class that has decrypting methods
    """
    def __init__(self, encrypter, cryp_file, shares):
        """
        Constrcut a decrypter method

        Args:
            encrypter (Encrypter): We obtain the IV from the original Encrypter
            cryp_file (str): Encrypted file
            shares (list): List of shares to use
        """
        self.iv = encrypter.get_cipherIV()
        self.file = cryp_file
        self.n, self.k, self.p = encrypter.get_nkp()
        self.shares = shares
        
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
        key = hashlib.sha256(num.encode('utf8')).digest()
        cipher = AES.new(key, AES.MODE_CBC, self.iv)
            
        decrypted_file = unpad(cipher.decrypt(encrypted_file), AES.block_size)
        
        return decrypted_file
    
    def get_secret(self):
        """
        Gets the password to decrypt the crypted file

        Returns:
            int: the password to decrypt
        """
        return LagrangeInterpolation.reconstruct_secret(self.shares, 0, self.k)
        
    
    def save_decrypted_file(self, new_name):
        """
        Saves the decrypted file

        Args:
            new_name (str): new name for the the decrypted file
        """
        with open(new_name, 'wb') as f:
            f.write(self.decipher_file())
            
            
