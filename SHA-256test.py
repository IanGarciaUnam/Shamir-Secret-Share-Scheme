import hashlib


chain:str="I don't know"

result = hashlib.sha256(chain.encode())

print("Value of:" + chain+"\n")

print(result.hexdigest())

print("Valor entero:\n")

numerote:int= int(result.hexdigest(),16)
constante_primo:int= 2083516173160912412343267463121244482
51235562226470491514186331217050270460
481
print(numerote)

print("Modulo primo")

print(numerote%constante_primo)

