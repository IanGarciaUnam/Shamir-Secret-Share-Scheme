import sys as system
from Cifrador import Cifrador
from Actuador import Actuador
class Main:

	@staticmethod
	def main_exe_c_notStandard():
		"""
		Allows the user to enter his own data to crypt the file
		"""
		arch_frg=str(input("Nombre del archivo para fragmentos: | File for frg\n"))
		eva_max:int=0
		eva_min:int=0
		arch_original:str=""
		secret:str=""
		while True:
			try:
				eva_max=int(input("Número de evaluaciones máximas / Total de integrantes: \n"))
				if eva_max>2:
					break;
			except:
				print("Tu dato debe ser un  valor entero |Mayor que 2/ Your data should be an integer, integer must be greater than 2 i>2\n")
		while True:
			try:
				eva_min=int(input("Número de evaluaciones mínimas / Mínimo de integrantes para descifrar el archivo\n"))
				if eva_min>1 and eva_min <= eva_max:
					break;
			except:
				print("Tu dato debe ser un  valor entero| Mayor que 1 y Menor que evaluaciones máximas / Your data should be an integer, integer must be 1<i<=n\n")

		arch_original=str(input("Archivo claro: \n"))
		secret = Actuador.get_secret("Ingresa tu contraseña | Password for :\t")
		sys.clear()
		c=Cifrador(secret, arch_original, file_frg)
		c.cifra()






