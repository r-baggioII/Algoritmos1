from linkedlist import LinkedList,Node, add, length, printList, delete
from algo1 import * 
import random 

class fechaIngreso(): 
  dia = None 
  mes = None 
  año = None 
class Empleado(): 
  nombre = None 
  edad = None 
  nroLegajo = None 
  fechaIngreso = fechaIngreso()
 
#---------------------------------------
E = LinkedList()

nombres = Array(10,"c")
legajos = Array(10,0)
#Nombres de los empleados 
nombres[0] = "Juan"
nombres[1] = "Carlos"
nombres[2] = "Taylor Swift"
nombres[3] = "Katy Perry"
nombres[4] = "Maradona"
nombres[5] = "Messi"
nombres[6] = "Mariana"
nombres[7] = "Steve"
nombres[8] = "Jason"
nombres[9] = "Diego"

#Legajos de los empleados 


#Cargamos los empleados en la linkedlist 
def addEmpleado(lista, nombres): 
  legajos = Array(10,0)
  edad = random.randint(20,60)
  i = 0 
  while i < len(legajos): 
    nroLegajo = random.randint(1,1000)
    if nroLegajo not in legajos:
      legajos[i] = nroLegajo
      i += 1 
  #Creamos una variable de tipo Empleado() y cargamos los atributos 
  newEmpleado = Empleado() 
  newEmpleado.nombre = random.choice(nombres)
  newEmpleado.edad = edad 
  newEmpleado.nroLegajo = random.choice(legajos)
  
  #Fecha random 
  dia = random.randint(1,31)
  mes = random.randint(1,12)
  año = random.randint(1983,2023)
  
  
  newEmpleado.fechaIngreso.dia = dia 
  newEmpleado.fechaIngreso.mes = mes 
  newEmpleado.fechaIngreso.año = año 
  
  #Creamos un nuevo nodo para agregar a la lista 
  newNode = Node() 
  newNode.value = newEmpleado 
  #Agregamos el elemento newEmpleado a la lista 
  add(lista,newEmpleado) 
#------------------------------------------

#Función para imprimir la linkedList 
def imprimirLista(L): 
  currentNode = L.head 
  while currentNode is not None: 
    empleado = currentNode.value 
    print("Empleado:", empleado.nombre)
    print("Edad: ", empleado.edad)
    print("NroLegajo: ", empleado.nroLegajo) 
    print("Fecha Ingreso: ")
    print(" ", "Dia: ", empleado.fechaIngreso.dia)
    print(" ", "Mes: ", empleado.fechaIngreso.mes)
    print(" ", "Año: ", empleado.fechaIngreso.año)
    print("------------------------------")
    currentNode = currentNode.nextNode 

def deleteEmpleados(L): 
  #Buscar el nro de legajo mas chico en la lista 
  currentNode = L.head 
  lowestLegajo = L.head.value.nroLegajo 
  while currentNode is not None: 
    if currentNode.value.nroLegajo <= lowestLegajo: 
      lowestLegajo = currentNode.value.nroLegajo 
    currentNode = currentNode.nextNode 

  currentNode = L.head

  while currentNode is not None and currentNode.value.nroLegajo == lowestLegajo:
    L.head = currentNode.nextNode
    currentNode = L.head

  while currentNode is not None:
    if currentNode.nextNode is not None and currentNode.nextNode.value.nroLegajo == lowestLegajo:
        currentNode.nextNode = currentNode.nextNode.nextNode
    else:
        currentNode = currentNode.nextNode

#Agregar 15 empleados 
for i in range(0,15): 
  addEmpleado(E,nombres)

imprimirLista(E) 

print("------------------------")
print("Lista - legajos eliminados") 

deleteEmpleados(E)
deleteEmpleados(E)
deleteEmpleados(E)
deleteEmpleados(E)
deleteEmpleados(E)

imprimirLista(E) 

