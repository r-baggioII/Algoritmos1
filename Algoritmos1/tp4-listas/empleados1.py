
from linkedlist import LinkedList,Node, add, length, printList, delete, addAtTheEnd



class Empleado(): 
  nombre = None 
  edad = None 
  nroLegajo = None 
#---------------------------------------
E = LinkedList()

#Cargamos los empleados en la linkedlist 
def agregarEmpleado(lista, nombre, edad,nroLegajo): 
  #Creamos una variable de tipo Empleado() y cargamos los atributos 
  newEmpleado = Empleado() 
  newEmpleado.nombre = nombre
  newEmpleado.edad = edad 
  newEmpleado.nroLegajo = nroLegajo 

  #Creamos un nuevo nodo para agregar a la lista 
  newNode = Node() 
  newNode.value = newEmpleado 
  #Agregamos el elemento newEmpleado a la lista 
  add(lista,newEmpleado) 
#------------------------------------------
agregarEmpleado(E, "Eduardo Ángel", 34, 2) 
agregarEmpleado(E, "Juan Carlos", 23, 5) 
agregarEmpleado(E, "Luis Esteban", 32, 7) 
agregarEmpleado(E, "Juan Carlos", 23, 5) 
agregarEmpleado(E, "Pedro Augusto", 40, 9) 
agregarEmpleado(E, "Luis Esteban", 32, 7) 
agregarEmpleado(E, "Pedro César", 45, 8)
agregarEmpleado(E, "Eduardo Ángel", 34, 2) 
agregarEmpleado(E, "Luis Esteban", 32, 7) 


#Función para imprimir la linkedList 
def imprimirLista(L): 
  currentNode = L.head 
  while currentNode is not None: 
    empleado = currentNode.value 
    print("Empleado:", empleado.nombre)
    print("Edad: ", empleado.edad)
    print("NroLegajo: ", empleado.nroLegajo) 
    print("------------------------------")
    currentNode = currentNode.nextNode 
imprimirLista(E) 

#3)--------------------------
#a) Eliminar los elementos donde "nroLegajo" se encuentren duplicado 
def eliminarDuplicados(L):
    currentNode = L.head

    while currentNode is not None:
        empleado = currentNode.value
        currentNextNode = currentNode.nextNode
        prevNode = currentNode  # Guardamos el nodo actual como prevNode

        while currentNextNode is not None:
            nextEmpleado = currentNextNode.value

            if empleado.nroLegajo == nextEmpleado.nroLegajo:
                # Eliminamos el nodo siguiente
                prevNode.nextNode = currentNextNode.nextNode
            else:
                prevNode = currentNextNode  # Actualizamos prevNode

            currentNextNode = currentNextNode.nextNode

        currentNode = currentNode.nextNode
eliminarDuplicados(E)
print("LISTA DE  EMPLEADOS SIN DUPLICADOS >>>> ")
imprimirLista(E) 

#b) Agregar antes del legajo número 7 el siguiente: Ernesto Andrés, 55, 6
def addEmpleado(L): 
  newEmpleado = Empleado()
  newEmpleado.nombre = "Ernesto"
  newEmpleado.edad = 55 
  newEmpleado.nroLegajo = 6 

  newNode = Node() 
  newNode.value = newEmpleado
  add(L,newEmpleado)
addEmpleado(E)
print("------------------------------")
print("LISTA CON EMPLEADO NUEVO AGREGADO >>>")
imprimirLista(E) 

