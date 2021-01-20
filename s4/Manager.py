import sys as system
from Encrypter import Encrypter
from Cifrador import Cifrador, Descifrador
from Actuador import Actuador
from LaGrangeInterpolation import LagrangeInterpolation as LGI
from Polynomio import Lagrange_Polynomial as Polynomio
import os
import sys as System

USO="Usage python main.py [c|d] <file-original> <total-points required >1 > <total> \"minimum points required\" >1> "
PRIMO=208351617316091241234326746312124448251235562226470491514186331217050270460481
class Manager:

	def __init__(self, file_original:str, total_points:int, minimum_points:int):
		if not os.path.exists(file_original) or not os.path.isfile(file_original):
			print("Check your original file- The path is wrong or the file doesn't exists\n")
			print(USO)
			System.exit()

		if not isinstance(total_points,int):
			print("Total Points is not an integer value, check your data\n")
			print(USO)
			System.exit()
		if not isinstance(minimum_points, int):
			print("Minimum points required is not an Integer value, check your data\n")
			print(USO)
			System.exit()
		if minimum_points > total_points:
			print("Total points ought to be bigger or at least equals than Minimum points\n")
			print(USO)
			System.exit()
		self.file_original=file_original
		self.total_points=total_points
		self.minimum_points=minimum_points


	def work_to_cipher(self):
		secret = Actuador.get_secret("Please type your password [We will keep it secret]")
		c= Cifrador(secret,self.file_original)
		c.cifra()
		key=c.get_key_number()
		p = Polynomio(PRIMO, self.minimum_points, self.total_points, key)
		out_list=p.generate_random_shares()
		frg_file=Actuador.change_to_new_term(self.file_original,"frg")
		Actuador.convert_list_in_file(out_list, frg_file)

class Verifier_Builder:
	def __init__(self, file_frg, encrypted_file):
		if not os.path.exists(file_frg) or not os.path.isfile(file_frg):
			print("Check your original file- The path is wrong or the file doesn't exists\n")
			print(USO)
			System.exit()
		if not os.path.exists(encrypted_file) or not os.path.isfile(encrypted_file):
			print("Check your original file- The path is wrong or the file doesn't exists\n")
			print(USO)
			System.exit(1)
		self.file_frg=file_frg
		self.encrypted_file=encrypted_file


	def work_to_descipher(self):
		list_in=Actuador.convert_file_in_list(self.file_frg)
		key= LGI.reconstruct_secret(list_in, 0) #Not Woring but is an idealization
		d=Descifrador(self.file_frg)
		d.descifra(key,self.encrypted_file, Actuador.get_original_ext(str(self.encrypted_file)))

		




















