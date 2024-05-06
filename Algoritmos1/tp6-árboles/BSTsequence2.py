from binarytree import print_tree,insert,traverseInOrder, BinaryTree
from linkedlist import LinkedList, printList,addAtTheEnd, delete,add,length,insertList


def BSTsequence(B): 
    if B.root is None:
        return 
    

    left_1 = LinkedList() 
    right_1 = LinkedList() 
    #Crear una lista Sequences para guardar todas las secuencias 
    sequences = LinkedList() 

    left_1 = preOrderLeftRight_R(B.root.leftnode,left_1)
    right_1 = preOrderLeftRight_R(B.root.rightnode,right_1)

    sequences =  combine_lists(left_1,right_1,sequences)

    if length(left_1) > 1: 
        left_2 = LinkedList()
        left_2 = preOrderRightLeft_R(B.root.leftnode,left_2)

    if length(right_1) > 1: 
        right_2 = LinkedList() 
        right_2 = preOrderRightLeft_R(B.root.rightnode,right_2)

    return sequences



def combine_lists(list1, list2, result):
    if list1 is None: 
        add(result,list2) 
    
    if list2 is None: 
        add(result,list) 

    current_1 = list1.head 
    current_2 = list2.head 
    aux = 0 

    while current_1: 
        while current_2: 
            insertList(list1,current_2.value,aux)
            current_2 = current_2.nextNode 
        add(result,list1)
        current_1 = current_1.nextNode 
        aux = aux +1 
    return result


def preOrderLeftRight_R(node,L): 
    if node is None: 
        return 
    
    add(L,node.key) 
    #Visitamos primero el nodo a izquierda y luego a la derecha 
    preOrderLeftRight_R(node.leftnode,L)
    preOrderLeftRight_R(node.rightnode,L)
    return L 
    


def preOrderRightLeft_R(node,L): 
    if node is None: 
        return 
    
    add(L,node.key) 
    #Visitamos primero el nodo a la derecha y luego a la izquierda 
    preOrderLeftRight_R(node.rightnode,L)
    preOrderLeftRight_R(node.leftnode,L)
    return L 

B = BinaryTree()
insert(B,2,2)
insert(B,1,1)
insert(B,3,3)
print_tree(B) 
print("-----------------")
L = BSTsequence(B)
