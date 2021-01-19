import getpass as gt
from Crypto.Cipher import AES
import hashlib

class Actuador:

	@staticmethod
	def get_secret(show_to_public:str)->str:
		"""
		Get some string from the user withoud doing echo in the Terminal
		"""
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
	def convert_list_in_file(list_out,file_frg):
		arch=open(file_frg, "w")
		for (x,y) in list_out:
			chain=str(x)+","+str(y)+"\n"
			arch.write(chain)

		arch.close()

	@staticmethod
	def convert_file_in_list(file_frg)->list:
		out_list=[]
		arch= open(file_frg, "r")
		for line in arch.readlines():
			print("")

