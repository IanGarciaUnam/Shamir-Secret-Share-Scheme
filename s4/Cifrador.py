from Crypto.Cipher import AES
import hashlib
class Cifrador:


	def cifra_contrasena(self, key:str):
		"""
		Appy SHA-256 with the user's key as a parameter
		Params:
			key: str, passed by the user
		Returns:
			int of 256 bits

		"""
		return int(hashlib.sha256(key.encode()).hexdigest(),16)


	def cifra_archivo(self, key, file):
		key_sha=hashlib.sha256(key.encode()).digest()
		apply_AES(key_sha, file)



