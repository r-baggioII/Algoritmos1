
class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None
S = LinkedList()


#-------------------------------------------------------------
#Agrega un elemento al comienzo de S, siendo S una estructura de tipo LinkedList
def push(S, element):
  newNode = Node()
  newNode.value = element
  if S.head is None:
    S.head = newNode
  else:
    newNode.nextNode = S.head
    S.head = newNode
  return S 
 
#-------------------------------------------------------------
def pop(S): 
  if S.head is None: 
    #Devuelve None si la pila esta vacia   
    return None 
  currentNode = S.head 
  element = currentNode.value 
  S.head  = currentNode.nextNode 
  #Devuelve el elemento a elimnar 
  return element 





