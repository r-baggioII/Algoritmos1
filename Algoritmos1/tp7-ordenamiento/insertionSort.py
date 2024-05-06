from algo1 import* 
from linkedlist import LinkedList, Node, add, printList, length, search,delete 

####################
def InsertionSort(L): 
  #start from position 1 (secondNode)
  currentNode = L.head.nextNode 
  prevNode = L.head  
  while currentNode is not None: 
    #If the element is not sorted 
    if currentNode.value <= prevNode.value: 
      #Store the reference to currentNode 
      nodeToInsert = currentNode
      delete(L,currentNode.value)
      auxNode = L.head 
      while nodeToInsert.value > auxNode.nextNode.value: 
        auxNode = auxNode.nextNode 

      #We insert it at the correct position 
      if auxNode == L.head: 
        nodeToInsert.nextNode = L.head 
        L.head = nodeToInsert
      else: 
        nodeToInsert.nextNode = auxNode.nextNode 
        auxNode.nextNode = nodeToInsert 
    prevNode = currentNode
    currentNode = currentNode.nextNode 

  return L 

L = LinkedList() 
add(L,2) 
add(L,5) 
add(L,3) 
add(L,8) 
printList(L) 
print("-------------") 
L = InsertionSort(L)
printList(L)
