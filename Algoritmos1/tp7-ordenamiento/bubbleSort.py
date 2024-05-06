from algo1 import* 
from linkedlist import LinkedList, Node, add, printList, length,search,delete 

def move(L,posI,posF): 
  #Si las posiciones son iguales no es necesario mover nada 
  if posI == posF: 
    return L 

  #Special case: We delete the first element on the list 
  if posI == 0: 
    nodeToMove= L.head 
    L.head = L.head.nextNode

  else: 
    #Sino, recorremos la lista hasta la posiciòn inicial 
    currentNode = L.head 
    posIAux = 0 

    while posIAux < posI - 1 : 
      currentNode = currentNode.nextNode 
      posIAux +=1 
    #Guardamos el nodo a mover y lo iliminamos de la lista 
    nodeToMove = currentNode.nextNode  
    currentNode.nextNode = currentNode.nextNode.nextNode 


  #Special case where the final position is 0 
  if posF == 0: 
    nodeToMove.nextNode = L.head 
    L.head = nodeToMove
    return L 

  else: 
    #Recorremos la lista hasta llegar a posicion final - 1 
    currentNode = L.head 
    posFAux = 0 
    while posFAux < posF - 1: 
      currentNode = currentNode.nextNode 
      posFAux += 1 
    #Insertamos nodeToMove en esa posiciòn 
    nodeToMove.nextNode = currentNode.nextNode 
    currentNode.nextNode = nodeToMove 

#####################
def BubbleSort(L): 
  size = length(L)
  i = 0 
  while i < size:   
    posAux = 0
    currentNode = L.head 
    while currentNode is not None and currentNode.nextNode is not None: 
      if currentNode.value > currentNode.nextNode.value: 
        move(L,posAux,posAux+1) 
      posAux += 1 
      currentNode = currentNode.nextNode
    i += 1 

  return L 


L = LinkedList() 
add(L,2) 
add(L,5) 
add(L,3) 
add(L,8) 
printList(L) 
print("-------------") 

