from Encrypter import Encrypter
from Decrypter import Decrypter
from Cifrador import Cifrador,Descifrador
from Actuador import Actuador
from Polynomio import Lagrange_Polynomial as Polynomio
from random import randint
from unittest import TestCase
from os import remove
import os
import io
class test_Encrypter_Cifrador_Descifrador(TestCase):
	"""
	Class for test Cifrador Class
	"""

	def test_verify_encryption(self):
		"""
		Verify that the encryption become unreadable to the common user
		"""
		PRIMO=208351617316091241234326746312124448251235562226470491514186331217050270460481
		Original=""

		way="test_files/"
		with open(way+"test.cat","r") as f:
			Original=f.read()
			f.close()

		self.cifra_descifra(way,PRIMO)
		no_readable=""

		with open(way+"test.cat.aes", "rb") as file:
			no_readable=file.read()

		assert Original != no_readable

		after=""
		with open(way+"test.cat","r") as t:
			after=t.read()
		assert Original==after and no_readable != after
		self.clean_dir(way+"test.cat.aes")
		self.clean_dir(way+"test.cat.frg")





	def test_encrypt_decrypt(self):
		"""
		Verify the encryption using Cifrador
		"""	
		PRIMO=208351617316091241234326746312124448251235562226470491514186331217050270460481
		Original=""
		maximum= randint(70,140)
		minimum=randint(2,69)

		way="test_files/"
		with open(way+"test.cat","r") as f:
			Original=f.read()
			f.close()

		self.cifra_descifra(way,PRIMO)
		assert os.path.isfile(way+"test.cat")

		after=""
		with open(way+"test.cat","r") as t:
			after=t.read()
			t.close()
		assert Original==after
		
		self.clean_dir(way+"test.cat.aes")
		self.clean_dir(way+"test.cat.frg")

	def clean_dir(self, file):
		os.remove(file)

	def cifra_descifra(self,way,PRIMO):
		maximum= randint(70,140)
		minimum=randint(2,69)
		c=Cifrador("password",way+"test.cat")
		c.cifra()
		key=c.get_key_number()
		p = Polynomio(PRIMO, minimum, maximum, key)
		out_list=p.generate_random_shares()
		frg_file=way+"test.cat.frg"
		Actuador.convert_list_in_file(out_list, frg_file)
		d= Descifrador(way+"test.cat.frg")
		d.descifra(way+"test.cat.aes", "cat")






