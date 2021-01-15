import getpass
import hashlib

class operations:


	@staticmethod
	def input_invisible(show_to_public:str):
		"""
		The user can give him password in secret mode
		Args:
			show_to_public: str - Password
		Return getpass.getpass(show_to_public)
		"""
		return getpass.getpass(show_to_public)
	@staticmethod
	def apply_sha_256(content:str):
		"""
		Apply SHA-256 to the content of the String
		Args:
			content:str - content to be applied by sha-256
		Return:
			str: Hexadecimal Character of the content applied to SHA-256
		"""

		return hashlib.sha256(content.encode())


