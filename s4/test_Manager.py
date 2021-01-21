from Manager import Manager,Verifier_Builder
from os import remove
from random import randint
from unittest import TestCase
from os import remove
import pytest
import os

import io
class test_Manager(TestCase):
	"""
	Class for test Cifrador Class
	"""

	def test_entry_no_file(self):
		"""
		Verify that user's file exists
		"""
		maximum= randint(70,140)
		minimum=randint(2,69)

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Manager("No_existente", maximum, minimum)
		assert pytest_wrapped_e.type == SystemExit




	def test_entry_no_max_min_in_right_order(self):
		"""
		Verify the values of max and min are right
		"""	
		maximum= randint(70,140)
		minimum=randint(2,69)

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			m=Manager("test_files/test.cat",minimum, maximum)
		assert pytest_wrapped_e.type == SystemExit

	def test_good_manager_good_verifier(self):
		"""
		Verify the correct use of Manager Class 
		"""
		maximum= randint(70,140)
		minimum=randint(2,69)
		m=Manager("test_files/test_manager_verifier.cdf", maximum,minimum)
		m.work_to_cipher("password1234qwerty")
		v= Verifier_Builder("test_files/test_manager_verifier.cdf.frg", "test_files/test_manager_verifier.cdf.aes")
		v.work_to_descipher()
		assert os.path.isfile("test_files/test_manager_verifier.cdf")
		os.remove("test_files/test_manager_verifier.cdf.frg")
		os.remove("test_files/test_manager_verifier.cdf.aes")


	def test_bad_verifier(self):

		with pytest.raises(SystemExit) as pytest_wrapped_e:
			v= Verifier_Builder("No existente", "No existente")
			v.work_to_descipher()
		assert pytest_wrapped_e.type==SystemExit

	def cifra_descifra(self,way,PRIMO):

		c=Cifrador("password",way+"test.cat")
		c.cifra()
		key=c.get_key_number()
		p = Polynomio(PRIMO, minimum, maximum, key)
		out_list=p.generate_random_shares()
		frg_file=way+"test.cat.frg"
		Actuador.convert_list_in_file(out_list, frg_file)
		d= Descifrador(way+"test.cat.frg")
		d.descifra(way+"test.cat.aes", "cat")






