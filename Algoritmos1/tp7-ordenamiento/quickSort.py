from algo1 import *
from linkedlist import LinkedList, Node, add, printList, length, delete,access 

#Chose the last element as the pivot 
#Keep count of the indexes (i - j)
#Initialize i = -1, j = 0 

#compare each nove.value to the pivot 
## If node.value > pivot ------> only increase j 
### If node.value < pivot ------> increase i and swap values between j and i 
#Repeat with each node on the list 

def swap(L, posA, posB):
  if posA == posB:
      return  # Nothing to do, as the nodes are the same

  prevA, prevB = None, None
  currentA, currentB = L.head, L.head
  indexA, indexB = 0, 0

  # Traverse the list to find the nodes at positions posA and posB
  while currentA is not None:
      if indexA == posA:
          break
      prevA, currentA = currentA, currentA.nextNode
      indexA += 1

  while currentB is not None:
      if indexB == posB:
          break
      prevB, currentB = currentB, currentB.nextNode
      indexB += 1

  if currentA is None or currentB is None:
      return  # One of the positions is out of range

  # Update the previous nodes to point to the new nodes
  if prevA is None:
      L.head = currentB
  else:
      prevA.nextNode = currentB

  if prevB is None:
      L.head = currentA
  else:
      prevB.nextNode = currentA

  # Swap the next nodes of A and B
  currentA.nextNode, currentB.nextNode = currentB.nextNode, currentA.nextNode

  return L 

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
  
def QuickSort_R(L,posI,posF): 
  if posI == posF: 
    return L 
  
  j = posI
  i = posI -1 
  pivot = access(L,posF)
  swaped = False 
  currentNode = L.head 
  
  while j < posF:  
    if currentNode.value <= pivot: 
      i += 1  
      if j > i: 
        L = swap(L,j,i) 
        currentNode = currentNode.nextNode.nextNode
        swaped = True
    j+= 1 
    if not swaped: 
      currentNode = currentNode.nextNode 
    swaped = False 
  #move the pivot to its correct position (i+1)
  L = move(L,posF,i+1)
  #Sort right and left side recursivly 
  #left side 
  L = QuickSort_R(L,0,i)
  L = QuickSort_R(L,i+2,length(L)-1)
  return L 
  
def QuickSort(L): 
  #Choose the last element as the pivot 
  L = QuickSort_R(L,0,length(L)-1)
  return L 
  
L = LinkedList()
add(L,4) 
add(L,5) 
add(L,3) 
add(L,6) 
add(L,8) 
add(L,1)
add(L,2) 
add(L,7) 
printList(L) 
QuickSort(L)
print("------") 
print("después de QuickSort")
printList(L)

