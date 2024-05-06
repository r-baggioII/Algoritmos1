#Elaborar un algoritmo que lea un vector, busque el mayor #elemento en valor absoluto y
#muestre el resultado 

from algo1 import * 
import math 

#1) Pedir la dimensión del vector al usuario y validarlo
def ValidarDimensionVector(): 
  while True: 
        n = input_int("Ingrese las dimenisones del vector: ")
        if n > 0:  
         break 
  return n
dim = ValidarDimensionVector()

#2) Definir al vector con dicha dimensión
vector = Array(dim,0.0)

#3) Leer vector 
def LeerVector(vector,dim): 
  for x in range(0, dim): 
    vector[x] = input_real("Ingrese un valor real: ")
LeerVector(vector,dim)

#4) Determinar el mayor elemento en valor absoluto 
def DeterminarMayorEnAbs(vector,dim):
  for x in range(0,dim): 
    if math.fabs(vector[0]) > math.fabs(vector[x]):
      MayorAbsoluto = vector[0]
      Posicion = 0
    else: 
      MayorAbsoluto = vector[x]
      Posicion = x
  print("Elemento: ", math.fabs(MayorAbsoluto))
  print("Posición: ", Posicion)
DeterminarMayorEnAbs(vector,dim) 
