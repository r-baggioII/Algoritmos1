from algo1 import * 
import random 

arrayS = Array(4,0)
arrayT = Array(5,0)

for i in range(0,4): 
  print("POSICIÓN: ",i)  
  arrayS[i] = input_int(" >> ")
print(arrayS)

for i in range(0,5): 
  print("POSICIÓN: ",i)  
  arrayT[i] = input_int(" >> ")
print(arrayT)

#Crea un TAD de tipo set desde un arreglo recibido como parámetro 

def Create_Set(array):
    array_aux = Array(len(array),0)
    length_aux = 0 
   #Si el elemento no está en array_aux, se le asginará el elemento de array 
    for i in range(len(array)): 
      if array[i] not in array_aux: 
        array_aux[i] = array[i]
        length_aux = length_aux + 1 
    FinalSet = Array(length_aux,0)
    index = 0 
  #Si la posición del array_aux no es None le asignamos los elementos al conjunto FinalSet
    for i in range(len(array)):
      if array_aux[i] is not None: 
        FinalSet[index] = array_aux[i]
        index += 1 
    return FinalSet


# Chequea si hay duplicados y muestra un mensaje
def check_duplicates(array): 
  duplicates = False 
  for i in range(len(array)): 
    for j in range(i+1,len(array)): 
      if array[i] == array[j]: 
        duplicates = True
  if duplicates: 
    print("Se hallaron duplicados en el Set")
  else: 
    print("No se hallaron duplicados en el Set")
  return duplicates

#Aplica la operación unión sobre dos conjuntos 
def Union(arrayS,arrayT): 
   
  #Definimos la longitud del SetUnion
    SetUnion = Array(len(arrayS) + len(arrayT),0)
  
  #Juntamos los elementos de ambos conjuntos en el SetUnion 
    for i in range(len(arrayS)): 
        SetUnion[i] = arrayS[i]
    for j in range(len(arrayT)):
        SetUnion[len(arrayS) + j] = arrayT[j]
    return SetUnion
SetUnion = Union(arrayS,arrayT)

#Chequemos si quedaron elementos duplicados en el set
duplicates = check_duplicates(SetUnion)
if duplicates == True:
  SetUnion = Create_Set(SetUnion)
print("CONJUNTO UNION")
print(SetUnion)

def Intersection(arrayS,arrayT): 
  size = 0 
  index = 0 
  #Conseguimos el tamaño del conjunto Interseccion
  for i in range(len(arrayS)): 
    if arrayS[i] in arrayT: 
      size = size + 1 
  SetIntersection = Array(size,0)
  for i in range(len(SetIntersection)): 
    if arrayS[i] in arrayT: 
      SetIntersection[index] = arrayS[i]
      index = index + 1 
  return SetIntersection
SetIntersection=Intersection(arrayS,arrayT)

#Chequeamos si quedaron elelemtnos duplicados en el Set 
duplicates = check_duplicates(SetIntersection)
if duplicates == True: 
  SetIntersection = Create_Set(SetIntersection)
print("CONJUNTO INTERSECCION")
print(SetIntersection)

def Difference(arrayS,arrayT): 
  size = 0  
  index = 0 
  #Conseguimos el tamaño del conjunto Diferencia 
  for i in range(len(arrayS)): 
    if arrayS[i] not in arrayT: 
      size += 1 
  SetDifference = Array(size,0)
  for i in range(len(SetDifference)): 
    if arrayS[i] not in arrayT: 
      SetDifference[i] = arrayS[i]
      index = index + 1 
  return SetDifference
SetDifference = Difference(arrayS,arrayT)

#Chequeamos si quedaron elelemtnos duplicados en el Set 
duplicates = check_duplicates(SetDifference)
if duplicates == True: 
  SetDifference = Create_Set(SetDifference)
print("CONJUNTO DIFERENCIA")
print(SetDifference)
