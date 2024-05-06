
from linkedlist import LinkedList, Node, add, length, printList, delete

L = LinkedList()

add(L, 3)
add(L, 4)
add(L, 6)
add(L, 5)
add(L, 8)
print("Original List >>> ")
printList(L)


def reverse(L):
  if L.head is None or L.head.nextNode is None:
    # No need to reverse an empty list or a list with only one element
    return L

  prevNode = None
  currentNode = L.head
  while currentNode is not None:
    nextNode = currentNode.nextNode
    currentNode.nextNode = prevNode
    prevNode = currentNode
    currentNode = nextNode
  L.head = prevNode



reverse(L)
print("Reversed List >>> ")
printList(L)
