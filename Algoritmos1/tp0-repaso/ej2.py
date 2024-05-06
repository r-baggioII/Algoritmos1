#Elaborar un algoritmo que lea dos vectores, verifique si tienen la #misma dimensiòn y los sume en un nuevo vector. Calcule la norma cuadràtica de este ùltimo vector. Muestre el vector resultado y su #normal cuadratica 
#1) Pedir la dimension de los vectores y leerlos
#2) Sumarlos 
#3) Calcular el mòdulo
#4) Mostrar los resultados por pantalla 

from algo1 import * 

dimension1 = 0
dimension2 = 0 

#Obtener dimension y verificar que sean iguales 
def Get_Verify_Dimension(dimension1, dimension2): 
    while dimension1 < 1: 
      dimension1 = input_int("Dimension Vector1: ")
    while dimension2 != dimension1 : 
      dimension2 = input_int("Dimension Vector2: ")
      if dimension2 != dimension1: 
        print("Las dimensiones de los vectores deben ser iguales")
      return dimension1
dimension = Get_Verify_Dimension(dimension1,dimension2)

#Declaro a los vectores con la dimension obtenida
vector1 = Array(dimension,0.0)
vector2 = Array(dimension, 0.0)

#Leer vectores
def LeerVectores(vector1, vector2, dimension): 
 for j in range(1,3):
   if j == 1: 
    for i in range(0,dimension):
        print("POSICIÓN: ", i)
        vector1[i]= input_real("Vector1: ")
    else:
     for i in range(0,dimension):
        print("POSICIÓN: ", i)
        vector2[i] =input_real("Vector2: ")
LeerVectores(vector1,vector2,dimension)

#Declaro un nuevo vector para almacenar la suma
VectorSuma= Array(dimension,0.0)

#Sumar Vectores 
def SumaVectores(vector1,vector2,dimension,VectorSuma):
  for i in range(0,dimension):
    VectorSuma[i] = vector1[i] + vector2[i]
  print(vector1, "+", vector2, "=", VectorSuma)
SumaVectores(vector1,vector2,dimension,VectorSuma)

#Calcular Módulo del Vector Suma 
def CalcularModulo(VectorSuma): 
  #norma = np.linalg.norm(VectorSuma)
  print("La norma del VectorSuma es: ", norma)
  return norma 
norma = CalcularModulo(VectorSuma)