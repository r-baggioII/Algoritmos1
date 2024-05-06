from algo1 import *
from linkedlist import printList

class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None
Q = LinkedList()


#-------------------------------------------------------------
#Agrega un elemento al comienzo de Q, siendo Q una estructura de tipo LinkedList
def enqueue(Q,element): 
  newNode = Node()
  newNode.value = element
  if Q.head is None:
    Q.head = newNode
  else:
    newNode.nextNode = Q.head
    Q.head = newNode
  return Q  

#-------------------------------------------------------------
#extrae el último elemento de la cola Q, siendo Q una estructura de tipo LinkedList.
def dequeue(Q): 
  if Q.head is None: 
    #Devuelve None si Queue esta vacia   
    return None 

  currentNode = Q.head 
  previousNode = None 

  while currentNode.nextNode is not None: 
    #Recorremos la lista de tipo Queue  hasta su ùltimo elemento 
    previousNode = currentNode 
    currentNode = currentNode.nextNode
  lastElement = currentNode.value 
  #Si hay un solo elemento, lo eliminamos y desvinculamos su nodo
  if previousNode is None: 
    Q.head = None 
  #Si hay màs de un elemento 
  else: 
    previousNode.nextNode = None 
  return lastElement
