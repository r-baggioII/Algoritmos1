from binarytree import insert, print_tree, BinaryTree, BinaryTreeNode
from myqueue import LinkedList, enqueue, dequeue
from linkedlist import addAtTheEnd, printList,add 

#Implementación recursiva 
def breadthFirstSearch(B):
    Q = LinkedList
    L = LinkedList()
    enqueue(Q,B.root)
    breadthFirstSearch_R(B.root,Q,L)
    return L 

def breadthFirstSearch_R(node,Q,L): 
    
    if Q.head is None: 
        return 
    if node is None: 
        return 

    node = dequeue(Q)
    addAtTheEnd(L,node.key)

    if node.leftnode is not None: 
        enqueue(Q,node.leftnode) 
    if node.rightnode is not None: 
        enqueue(Q,node.rightnode)
    
    breadthFirstSearch_R(node.leftnode,Q,L)
    breadthFirstSearch_R(node.rightnode,Q,L)



#Implementación Iterativa
def BFS(B): 
    queue = LinkedList() 
    L = LinkedList()
    enqueue(queue,B.root)
    while queue.head:
        node = dequeue(queue)
        addAtTheEnd(L,node.key)
        if node.leftnode is not None:  
            enqueue(queue,node.leftnode)
        if node.rightnode is not None: 
            enqueue(queue,node.rightnode)
    return L 



B = BinaryTree()
insert(B,8,8)
insert(B,4,4)
insert(B,12,12)
insert(B,2,2)
insert(B,6,6)
insert(B,10,10)
insert(B,14,14)




print_tree(B)
print("-------------------")
L = BFS(B)
printList(L)


