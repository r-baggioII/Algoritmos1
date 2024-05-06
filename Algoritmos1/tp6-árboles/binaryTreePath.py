from binarytree import BinaryTree, print_tree, insert
from linkedlist import addAtTheEnd, printList, LinkedList, add



def binaryTreePaths(B): 
    
    if B.root is None: 
        return None 
    L = LinkedList()
    
    if B.root.leftnode is None and B.root.rightnode is None: 
        add(str(B.root.key))
        return L 
    path = ""

    binaryTreePaths_R(B.root,L,path)
    return L 


def binaryTreePaths_R(node,L,path): 
    if node is None: 
        return 
    path += str(node.key) + ","
    #El nodo es una hoja 
    if node.leftnode is None and node.rightnode is None: 
        addAtTheEnd(L,path)
        return
    binaryTreePaths_R(node.leftnode,L,path)
    binaryTreePaths_R(node.rightnode,L,path)




B = BinaryTree() 

insert(B,8,8)
insert(B,12,12)
insert(B,4,4)
insert(B,10,10)
insert(B,6,6)
insert(B,2,2)
insert(B,14,14)
print_tree(B)
print("----------------")
L = binaryTreePaths(B)
printList(L)

