from Crypto.Cipher import AES
from Encrypter import Encrypter
from Decrypter import Decrypter
import hashlib
from Actuador import Actuador

class Cifrador:

	def __init__(self,key,file_orig):
		self.key=key
		self.file=file_orig
		self.encrypter=None

	def get_key_number(self):
		if self.encrypter==None:
			raise ValueError("You need to apply cifra(), before get_key_number")

		return self.encrypter.get_key()

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

class Descifrador:
	def __init__(self,file_frg):
		self.file_frg=file_frg

		
	def descifra(self, key_sha, cryp_file, original_ext):
		if key_sha==None:
			print("Clave o descifrador no conocido")
			return
		shares=Actuador.convert_file_in_list(self.file_frg)
		d=Decrypter( self.file_frg, shares)
		d.save_decrypted_file(Actuador.change_to_new_term(cryp_file, original_ext))






