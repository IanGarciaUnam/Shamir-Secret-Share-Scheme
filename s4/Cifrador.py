from Crypto.Cipher import AES
from Encrypter import Encrypter
import hashlib
from Actuador import Actuador

class Cifrador:

	def __init__(self,key,file_orig, file_frg):
		self.key=key
		self.file=file
		self.encrypter=None
		self.file_frg=file_frg

	def cifra(self):
		"""
		A method that encrypte the file a write the encrypted one in the 
		same route
		Params:
			self. : The Cifrador's Object
		"""
		e=Encrypter(self.file, self.key)
		e.encrypt_file()
		new_file_name= Actuador.change_to_new_term(str(self.file),"aes")
		e.save_encrypted_file(new_file_name)
		self.encrypter=e
		
	def descifra(self, key_sha, cryp_file, original_ext):
		if key_sha==None or self.encrypter==None:
			print("Clave o descifrador no conocido")
			return

		d=Decrypter(self.encrypter, cryp_file, key_sha)
		d.decipher_file()
		d.save_decrypted_file(Actuador.change_to_new_term(cryp_file, original_ext))






