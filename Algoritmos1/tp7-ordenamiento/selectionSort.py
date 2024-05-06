from algo1 import* 
from linkedlist import LinkedList, Node, add, printList, length, search,delete 

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

def smallestElement(L,posF): 
  #Find the new first node in order to find the smallest element 
  i = 0
  currentNode = L.head
  while i < posF: 
    currentNode = currentNode.nextNode 
    i += 1 
  
  #Find the smallest element on the list 
  smallest = currentNode.value 
  while currentNode is not None: 
    if currentNode.value < smallest: 
      smallest = currentNode.value 
    currentNode = currentNode.nextNode 
  return search(L,smallest)

####################
def SelectionSort(L): 
  posF = 0 
  size = length(L) 
  while posF < size: 
    #Find the smallest element on the list and its position 
    posSmallest = smallestElement(L,posF) 
    #Place it at the beggining 
    move(L,posSmallest,posF)
    #Repeat the process with the rest of the list until it's sorted 
    posF +=1 
  return L 

