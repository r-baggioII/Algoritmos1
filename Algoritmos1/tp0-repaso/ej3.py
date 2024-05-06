#Elaborar un algoritmo que lea una matriz y un vector, y que verifique si es posible la
#multiplicación. En el caso de ser posible realice la operación correspondiente, caso contrario. 
#que muestre el mensaje “dimensiones incorrectas”.
#PASOS: 
#1) Pedir dimensiones de los arreglos 
#2) Leer matriz y vector, y mostrarlos por pantalla
#3) Determinar si es posible la multiplicacion de ambos

from algo1 import * 

DimVector  = 0 
FilaMatriz = 0 
ColumMatriz = 0 

#Pedir dimension vector 
def Get_Dimension_Vector(DimVector): 
  while DimVector < 1: 
    DimVector = input_int("DIMENSIÓN VECTOR: ")
    if DimVector < 1: 
      print("Dimensión no válida")
    return DimVector
DimVector = Get_Dimension_Vector(DimVector)

#Pedir Flas Matriz 
def Get_Filas(FilaMatirz): 
  print("DIMENSIONES DE LA MATRIZ: ")
  while FilaMatirz < 1: 
    FilaMatriz = input_int("NUMERO DE FILAS: ")
    if FilaMatriz < 1: 
      print("Número de filas no válido")
    return FilaMatriz
FilaMatriz = Get_Filas(FilaMatriz)

#Pedir Columnas Matriz 
def Get_Columnas(ColumMatriz): 
  while ColumMatriz < 1: 
    ColumMatriz = input_int("NÚMERO DE COLUMNAS: ")
    if ColumMatriz< 1: 
      print("Número de columnas no válido")
    return ColumMatriz
ColumMatriz = Get_Columnas(ColumMatriz)

Vector = Array(DimVector,0.0)
Matriz = Array(FilaMatriz,Array(ColumMatriz,0.0))

#Determinar si es posible el producto
def ProductoDefinido(DimVector,FilaMatriz): 
  if  FilaMatriz == DimVector: 
    EsPosible = True 
  else: 
    return False 
    print("Dimensiones Incorrectas")
  return EsPosible 
EsPosible=ProductoDefinido(DimVector,FilaMatriz)


#Si el producto es posible creamos un nuevo Array y pedimos los datos del vector y la matriz, sino terminamos el programa 

if EsPosible == True: 
  Rto = Array(ColumMatriz,0.0)
  #Leer Vector 
  def LeerVector(Vector,DimVector):
    print("VECTOR: ")
  for i in range(0,DimVector): 
    print("CELDA: [", i , "]")
    Vector[i] = input_real(" > ") 
  print(Vector)
  LeerVector(Vector,DimVector)

  #Leer Matriz 
  def LeerMatriz(Matriz,FilaMatriz,ColumMatriz): 
    if EsPosible == True: 
      print("MATRIZ: ")
    for i in range(0,FilaMatriz):
      for j in range(0,ColumMatriz): 
        print("CELDA: [", i,  "][", j, "]")
        Matriz[i][j] = input_real(" > ")
    for q in Matriz: 
      print(q)
  LeerMatriz(Matriz,FilaMatriz,ColumMatriz)
 
  #Realizar el Producto 
  def Producto(Vector,Matriz,DimVector,n,Rto):
    for q in range(len(Rto)): 
       Rto[q] = 0.0 #Inicializado en 0.0 
    for i in range(0,DimVector): 
        for j in range(0,n): 
           Rto[i] = Rto[i] + Vector[j]*Matriz[i][j]
    return Rto 
  Rto=Producto(Vector,Matriz,DimVector,ColumMatriz,Rto)
  
  #Imprimir Resultado 
  def ImprimirResultado(Rto): 
    print("Resultado: ")
    for i in range(0,len(Rto)): 
      print(Rto[i])
  ImprimirResultado(Rto)
else: 
  print("Dimensiones Incorrectas")
  