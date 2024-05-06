from algo1 import *
from linkedlist import LinkedList, Node, add, insert, delete, length, printList, access, update, search 
from mystack import pop, push 

#Ejercicio 1
def fibonacci(n): 
  if n == 0: 
    return 0 
  if n == 1: 
    return 1
  else: 
    return fibonacci(n-1) + fibonacci(n-2)

#Ejercicio 2
def nPrimerosEnteros(n): 
  #caso base
  if n == 1: 
    return 1 
  else: 
    return n + nPrimerosEnteros(n-1)
    

#Ejericio 3
def sumaEnterosPares(n): 
  if n % 2 != 0: 
    print("Eror, n debe ser par")
    return 
  if n == 2: 
    return 2 
  else: 
    return n + sumaEnterosPares(n-2) 


#Ejercicio 4: 
def move(L,posI,posF): 
    #Si las posiciones son iguales no es necesario mover nada 
    if posI == posF: 
      return 
   
    #Sino, recorremos la lista hasta la posiciòn inicial 
    currentNode = L.head 
    posIAux = 0 
   
    while posIAux < posI - 1 : 
      currentNode = currentNode.nextNode 
      posIAux +=1 
    #Guardamos el nodo a mover y lo iliminamos de la lista 
    nodeToMove = currentNode.nextNode  
    currentNode.nextNode = currentNode.nextNode.nextNode 

    if posF == 0: 
      nodeToMove.nextNode = L.head 
      L.head = nodeToMove
      return 
    
  #Recorremos la lista hasta llegar a posicion final - 1 
    currentNode = L.head 
    posFAux = 0 
    while posFAux < posF - 1: 
      currentNode = currentNode.nextNode 
      posFAux += 1 
    #Insertamos nodeToMove en esa posiciòn 
    nodeToMove.nextNode = currentNode.nextNode 
    currentNode.nextNode = nodeToMove 
  
      
def ordenarRecursivamente(L,posF,currentNode):
  #Caso base de recursión 
  if currentNode is None: 
    return
  
  #Buscar el menor elemento en la lista 
  menor = currentNode.value 
  while currentNode is not None: 
    if currentNode.value < menor: 
      menor = currentNode.value
    currentNode = currentNode.nextNode 
  minPosition = search(L,menor)
  
  #Movemos el nodo 
  move(L,minPosition,posF)
  
  #Buscamos el nuevo primer nodo de la lista 
  posF+= 1 
  aux = 0 
  currentNode = L.head 
  while aux < posF: 
    currentNode = currentNode.nextNode 
    aux += 1 
  #Llamamos a la función usando recursividad 
  ordenarRecursivamente(L,posF,currentNode)

L = LinkedList()

add(L,5)
add(L,6) 
add(L,10)
add(L,1) 
add(L,8) 
add(L,3) 
add(L,0)


printList(L) 
print("--------------------")
ordenarRecursivamente(L,0,L.head)
printList(L)
 
print("--------------------")

#Ejercicio 5: 
S = LinkedList() 
push(S,0)
push(S,1) 
printList(S)
print("--------")
n = input_int("Ingrese cantidad de términos a calcular >> ") 
#Cantidad de terminos que vamos a agregar a Stack (S): (n-2)
#Recorremos la lista hasta los dos primeros elementos
for i in range(n-2): 
  i = 0
  currentNode = S.head   
  while i < 1: 
    prevNode = currentNode
    currentNode = currentNode.nextNode 
    i += 1 
  newFibo = prevNode.value + currentNode.value #Sumamos los dos primeros números 
  push(S,newFibo)
printList(S)

