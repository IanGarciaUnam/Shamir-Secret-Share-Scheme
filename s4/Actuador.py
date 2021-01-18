import getpass as gt
from Crypto.Cipher import AES
import hashlib

IV = "1234567890123456"
BIG_PRIMO=208351617316091241234326746312124448251235562226470491514186331217050270460481
class Actuador:

	@staticmethod
	def get_secret(show_to_public:str)->str:
		return gt.getpass(show_to_public)

	@staticmethod	
	def apply_AES(key_sha, direc):
		encriptador = AES.new(key_sha,AES.MODE_CBC, IV)
		file= open(direc, "rb")
		encrypted_file= open("file.aes","wb")
		while True:
			reading=file.read(16)
			size=len(reading)
			if size==0:
				break
			elif size%16 != 0:
				reading +=b'0'*(16- size % 16)
			out= encriptador.encrypt(reading)
			encrypted_file.write(out)
		file.close()
		encrypted_file.close()

key="Hola"
key_sha=hashlib.sha256(key.encode()).digest()
Actuador.apply_AES(key_sha, "test.txt")