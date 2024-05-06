from algo1 import * 

from linkedlist import LinkedList, Node, add, printList, length, addAtTheEnd, delete 


#MERGE SORT 
def MergeSort(L):
  size = length(L) 
  if size == 1: 
    return L 
    
  #Split the linkedList in half 
  firstHalf = size // 2 
  secondHalf = size - firstHalf
  
  #Create two linkedList with the elements of the previous one 
  list1 = LinkedList() 
  list2 = LinkedList() 
  currentNode = L.head 

  for i in range(firstHalf): 
    addAtTheEnd(list1,currentNode.value) 
    currentNode = currentNode.nextNode 
  for i in range(secondHalf): 
    addAtTheEnd(list2,currentNode.value)
    currentNode = currentNode.nextNode 
  
  #Recursivly split them in half 
  list1 = MergeSort(list1) 
  list2 = MergeSort(list2)

  sorted = merge(list1,list2)
  
  return sorted 


def merge(L1,L2):
  mergedList = LinkedList() 
  currentL1 = L1.head 
  currentL2 = L2.head 

  while currentL1 is not None and currentL2 is not None: 
    if currentL1.value > currentL2.value: 
      addAtTheEnd(mergedList,currentL2.value) 
      delete(L2,currentL1.value)
      currentL2 = currentL2.nextNode 
    else: 
      addAtTheEnd(mergedList,currentL1.value) 
      delete(L1,currentL1.value) 
      currentL1 = currentL1.nextNode 

   
  #Now either L1 or L2 is None 
  while currentL1 is not None: 
    addAtTheEnd(mergedList,currentL1.value) 
    currentL1 = currentL1.nextNode 
  while currentL2 is not None: 
    addAtTheEnd(mergedList,currentL2.value) 
    currentL2 = currentL2.nextNode 
    
  return mergedList 

L = LinkedList()


add(L,4) 
add(L,9) 
add(L,6) 
add(L,7) 
add(L,8) 
add(L,1)
add(L,0) 
add(L,5)
add(L,2)
add(L,3) 
printList(L) 
print("------")
L = MergeSort(L)
printList(L)