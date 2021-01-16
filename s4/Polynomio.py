from random import random,randint
import numpy as np
import sympy as sym
import hashlib
class Polynomio:

	def __init__(self, n:int, t:int):
		if n<t:
			print("Number of members ought to be at least equals than minimum members")
			raise ValueError

		self.n=n
		self.umbral=t
		self.grado=t-1


	def generate_x_y_values(self):
		list_x_values=[]
		list_y_values=[]
		for x in range(self.grado):
			x=randint(self.umbral, self.n)
			y=randint(self.umbral,self.n)
			if x in list_x_values:
				x+=randint(self.grado, self.n)
			if y in list_y_values:
				y+=randint(self.grado, self.n)
			list_x_values.append(x)
			list_y_values.append(y)
		return (list_x_values,list_y_values)


	def generate_polynomio(self, list_xy_values:tuple, key):
		xi,yi=list_xy_values
		tamano = len(xi)
		x= sym.Symbol('x')
		polinomio=int(key, 16)
		divisorL=np.zeros(tamano, dtype=float)

		for i in range(0,tamano,1):
			num=1
			den=1
			for j in range(0,tamano,1):
				if j!=i:
					num*=x-xi[j]
					den*=xi[i]-xi[j]
		terminoLi=num/den

		polinomio+=terminoLi*yi[i]
		divisorL[i]=den

		polinomio_simplified= polinomio.expand()
		px = sym.lambdify(x,polinomio_simplified)
		self.px=px

	def calculate_point(self, x):
		return self.px(x)


p = Polynomio(30,15)
x,y=p.generate_x_y_values()
key="Hola"
key_sha=hashlib.sha256(key.encode()).hexdigest()
p.generate_polynomio((x,y), key_sha)

print("Key:")
print(int(key_sha,16))

print((x,y))
for xi in x:
	print(xi)
	print(p.calculate_point(xi))

y_entero=p.calculate_point(0)
y_hexa=hex(y_entero)

print(int(y_hexa,16))

