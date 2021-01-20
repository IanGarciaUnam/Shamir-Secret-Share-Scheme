from Manager import Manager,Verifier_Builder
import sys as System

USO="Usage python main.py [c|d] <file-original | file frg>  <total-points required >1 | encrypted file> <total \"minimum points required\" >1> "
__author__="David Hernández Uriostegui-, Ian Israel García Vázquez-317097364"
__version__="0.1.0"
__license__= "GNU"
DESCRIPTION = "Shamir Secret  Share Scheme"


class Main:

	def __init__(self, args:list):
		self.args=args

	def main(self):
		if len(self.args)==1 or self.args==None:
			print(USO)
			System.exit()

		if self.args[1]=='c' and len(self.args)<4:
			print(USO)
			System.exit()

		if self.args[1]=='c':
			m=Manager(self.args[2], int(self.args[3]), int(self.args[4]))
			m.work_to_cipher()

if __name__ == "__main__":
	ma=Main(System.argv)
	ma.main()

		




