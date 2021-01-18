import random
import numpy as np
import sympy as sym
import hashlib
import matplotlib.pyplot as plt
from Cifrador import Cifrador 

NUM=208351617316091241234326746312124448251235562226470491514186331217050270460481

class Polynomio:

	def __init__(self, n:int, t:int, key):
		if n<t:
			print("Number of members ought to be at least equals than minimum members")
			raise ValueError

		self.n=n
		self.umbral=t
		self.grado=t-1
		self.key=key


	def generate_x_y_values(self):
		list_x_values=[]
		list_y_values=[]
		for x in range(self.grado):
			x=random.getrandbits(256)
			y=random.getrandbits(256)

			list_x_values.append(x%NUM)
			list_y_values.append(y%NUM)
			list_x_values.append(0)
			list_y_values.append(self.key)
		return (list_x_values,list_y_values)


	def generate_polynomio(self, list_values_x, list_values_y):
		"""
		"""
		polinomio=0
		for i in range(len(list_values_x)):

			polinomio+=list_values_y[i]*self.multiplicador(i,list_values_x)

		print(polinomio)
		pxi=sym.expand(polinomio)
		sym.sympify(pxi)
		px=sym.lambdify(x,pxi)
	

	@staticmethod
	def multiplicador(i,list_values_x):
		num=1
		den=1
		x=sym.Symbol('x')
		div=np.zeros(len(list_values_x), dtype=float)
		for j in range(i):
			if(i!=j):
				num*=x-list_values_x[j]
				den*=list_values_x[i]-list_values_x[j]
		div=num/den
		return div

c=Cifrador("Hola")
key_value=c.cifra_contrasena()
p=Polynomio(10,5, key_value)
x,y=p.generate_x_y_values()
p.generate_polynomio(x,y)