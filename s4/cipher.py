import hashlib
import os


BIG = 208351617316091241234326746312124448251235562226470491514186331217050270460481
BITS=256



class cipher:
	"""Instance related with the cipher process for a file
	"""

	def __init__(self, file):
		"""
		Builder for a file to be chipered
		Args:
			file(string): The route/file to be cihpered
		"""
		self.file=str(file)

	def is_file(self):
		"""
		A method that ask for a file
		Args:
			self: the instance of the object
		Return:
			True |if it is a file - False|If it is not a file
		"""
		return os.path.isfile(str(self.file))

	def encrypt():
		pass

	def decrypt():
		pass





