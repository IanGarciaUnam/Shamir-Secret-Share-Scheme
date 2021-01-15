from cipher import cipher
from operations import Operations


class manager:

	def __init__(self):
		self=self


	def encrypt(self):
		password=Operations.input_invisible("Introduce your password:\t")
		passed=Operations.apply_sha256(password)
		


M = manager()
M.encrypt()
