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
	def change_to_new_term(original_name, new_ext):
		"""
		Change the original extension of the file to the new one
		Params:
		original_name: str
		new_ext:str
		Return:
		The new str: in fussion
		"""
		original=original_name.split(".")[0]
		original+="."+new_ext
		return original