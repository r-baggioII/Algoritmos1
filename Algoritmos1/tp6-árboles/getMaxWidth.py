#Logica para abordar el problema: 
    #1) Vamos a recorrer el árbol el amplitud (usando BFS), así recorreremos el árbol por niveles, de arriba hacia abajo
    #2) A medida que recorremos el árbol vamos a ir agregando la cantidad de nodos por nivel a una LinkedList auxiliar. 
        #Esta nos ayudará a determinar la cantidad de nodos que hay por nivel 
    #3) Usamos una variable contador para los niveles 
    #4) Cuando hayamos recorrido todo el árbol solo faltará determinar el mayor el elemento de nuestra lista auxiliar, pues ese será el ancho del árbol 

# getMaxWidth(B): 
    #Creamos una lista L donde guardaremos la cantidad de nodos por nivel (levelWidth)
    #Creamos una QUEUE de tipo LinkedList() para realizar el recorrido Breadth First Search
    #Usamos una función wrapper que llamaremos getMaxWidth_R(node,queue,L,levelWidth)
    #Llamamos a la funcion getMaxWidth_R(B.root,queue,L,levelWidth) y pasamos como uno de los parámetros a la raiz del árbol 
    #---Recusividad ---# 

    #Buscamos el mayor elemento en la lista L, ese será nuestro max width 



from binarytree import insert, print_tree, BinaryTree, BinaryTreeNode
from myqueue import LinkedList, enqueue, dequeue
from linkedlist import addAtTheEnd, printList,add, length

def getMaxWidth(B): 
    
    if B.root is None: 
        return None 
    
    queue = LinkedList() #queue 
    L = LinkedList()

    enqueue(queue,B.root)
    
    getMaxWidth_R(B.root,queue,L,length(queue))

    print(greatestElement(L))
    
    return L 
    

def getMaxWidth_R(node,queue,L,levelWidth): 
    if queue.head is None: 
        return 
    if node is None: 
        return 

    node = dequeue(queue)

    if node.leftnode is not None: 
        enqueue(queue,node.leftnode) 
    if node.rightnode is not None: 
        enqueue(queue,node.rightnode)
    
    levelWidth = length(queue)
    add(L,levelWidth)

    getMaxWidth_R(node.leftnode,queue,L,levelWidth)
    getMaxWidth_R(node.rightnode,queue,L,levelWidth)
    
    

def greatestElement(L): 
    currentNode = L.head 
    maxElement = currentNode.value 
    while currentNode: 
        if currentNode.value > maxElement: 
            maxElement = currentNode.value 
        currentNode = currentNode.nextNode 
    return maxElement
    




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
L = getMaxWidth(B)
print("-------------------")
printList(L)


