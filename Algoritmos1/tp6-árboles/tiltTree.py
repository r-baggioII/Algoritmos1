from binarytree import BinaryTree, print_tree, insert
from linkedlist import LinkedList, add, printList

#Time complexity --->> O(n)

def tilt_tree(B): 
    if B.root is None: 
        return 0 
    L = LinkedList()
    tilt_tree_R(B.root,L)
    #Sumamos todos los tilts en nuestra LinkedList 
    return sumTilts(L)
    

def tilt_tree_R(node,L):
    
    if node is None: 
        return 0 
    
    left = tilt_tree_R(node.leftnode,L) 
    right = tilt_tree_R(node.rightnode,L)

    #Calculamos el tilt de cada nodo (valor absoluto de la diferencia entre el subárbol izquierdo y el subrábol derecho)
    tiltNode = abs(left - right)
    #Agregamos el tilt de cada nodo a una linkedList 
    add(L,tiltNode)

    return left + right + node.value 
   

def sumTilts(L): 
    currentNode = L.head 
    tiltTree = 0 
    while currentNode: 
        tiltTree += currentNode.value 
        currentNode = currentNode.nextNode 
    return tiltTree



B = BinaryTree()
insert(B,8,8)
insert(B,12,12)
insert(B,4,4)
insert(B,10,10)
insert(B,2,2)
insert(B,14,14)


print_tree(B)
print("-------------------")
tiltTree = tilt_tree(B)
print("_----------------")
print(tiltTree)