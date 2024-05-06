#Elaborar un algoritmo que lea dos matrices, calcule la diferencia de las mismas y almacene el
#resultado en una tercera matriz.
#PASOS: 
#1) Pedir las dimensiones de la matriz
#2) Leer Matrices
#3) Restarlas 
#4) Almacenar el resultado en una nueva matriz 

from algo1 import * 

M = 0
N = 0 

#Pedir dimensiones para las matrices y validar entradas
print("Ingrese las dimensiones de las matrices(MxN): ")

def Leer_Dimension_M(M): 
  while M < 1: 
    M = input_int("N° Filas > ")
    if M < 1: 
      print("Número de filas no válido")
  return M 
M = Leer_Dimension_M(M) 

def Leer_Dimension_N(N): 
  while N < 1: 
    N = input_int("N° Columnas > ")
    if N < 1: 
      print("Número de columnas no válido")
  return N 
N = Leer_Dimension_N(N)

Matriz1 = Array(M,Array(N,0.0))
Matriz2 = Array(M,Array(N,0.0))
Resultado = Array(M,Array(N,0.0))

#Leer Datos y mostrar matriz 
def Leer_Datos_Y_Mostrar(Matriz,M,N): 
  
  print("INGRESE LOS DATOS DE LA MATRIZ")
  for i in range(0,M): 
    for j in range(0,N): 
      print("Celda: [", i, "] [", j, "]")
      Matriz[i][j] = input_real(" > ")
  for i in Matriz: 
    print(i)

Leer_Datos_Y_Mostrar(Matriz1,M,N)
Leer_Datos_Y_Mostrar(Matriz2,M,N)

#Restar Matrices 
def Restar_Matrices(Matriz1, Matriz2,M,N,Resultado): 
  for i in range(0,M): 
    for j in range(0,N): 
      Resultado[i][j]= Matriz1[i][j] - Matriz2[i][j]
  return Resultado 
Resultado=Restar_Matrices(Matriz1,Matriz2,M,N,Resultado)

#Mostrar Matriz Resultado 
def Mostrar_Resultado(Resultado): 
  print("")
  print("MATRIZ RESULTADO: ")
  print("")
  for i in Resultado: 
    print(i)
Mostrar_Resultado(Resultado)
