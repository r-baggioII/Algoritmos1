#Elaborar un algoritmo que lea una matriz y determine si es triangular superior. En caso
#afirmativo el algoritmo debe calcular el determinante de dicha matriz.

from algo1 import * 
N = 0 
#Pedir dimensiones de la matriz 
def Leer_Dimension(N): 
  print("Ingrese las dimensiones de la matriz NxN: ")
  while N < 1: 
    N = input_int(" > ")
    if N < 1: 
      print("Dimensión no válida")
  return N 
N = Leer_Dimension(N)

Matriz = Array(N,Array(N,0.0))

#Leer y Mostrar Matriz 
def Leer_Mostrar_Matriz(Matriz): 
  for i in range(len(Matriz)): 
    for j in range(len(Matriz)): 
      print("Celda: [", i, "] [", j,"]")
      Matriz[i][j] = input_real(" > ")
  print("MATRIZ: ")
  for i in Matriz: 
    print(i)
Leer_Mostrar_Matriz(Matriz)

#Determinar si es triangular Superior 
def Es_Triangular_Superior(Matriz): 
  es_triangular_superior = True
  for i in range(len(Matriz)):
    for j in range(i):
      if Matriz[i][j] != 0:
        es_triangular_superior = False
        break
  return es_triangular_superior   
EsTriangular = Es_Triangular_Superior(Matriz)

if EsTriangular: 
  print("La Matriz es triangular superior")
  def CalcularDeterminate(Matriz): 
    determinante = 0 
    for i in range(len(Matriz)): 
      for j in range(len(Matriz)): 
        if i == j: 
          determinante += Matriz[i][j] * Matriz[i+1][j+1]
      
      return determinante 
  determinante = CalcularDeterminate(Matriz)
  print("El determinante de la matriz es: ", determinante)
else: 
  print("La matriz no es triangular superior") 