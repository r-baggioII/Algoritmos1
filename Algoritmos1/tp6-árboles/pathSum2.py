#Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children


from binarytree import BinaryTree, BinaryTreeNode, print_tree, insert, traverseInOrder
from linkedlist import LinkedList,printList, add
from mystack import pop 


def pathSum(B,x): 
    if B.root is None: 
        return None
    L = LinkedList() #Para guardar las tayectorias que sean iguales a targetSum 
    
    global currentSum
    currentSum = 0 #Varibale contador para la suma de las keys 
   
    path = LinkedList() 
    allPaths = LinkedList()
    prevNode = None 
    pathSum_R(B.root,x,currentSum,path,allPaths,prevNode) #Función recursiva 
    add(path,B.root.key)
    return allPaths


def pathSum_R(node,x,currentSum,path,allPaths,prevNode):
    if node is None: 
        return  

    if prevNode is not None and prevNode.parent is not None: 
        print("key del nodo prev",prevNode.key)
        currentSum += node.key #Suma el valor de los nodos 
        add(path,node.key)

    #Caso base, llegamos a una hoja, entonces hemos terminado un recorrido 
    if node.leftnode is None and node.rightnode is None: 
        if currentSum == x: 
            print("suma", currentSum)
            add(allPaths,path) 
            printList(path)
            print("???")
            print("--------")
            path.head == None
            currentSum = 0
            return 
        
        print(pop(path))  #Sacar el último nodo hoja que no debería estar 
         
    
    prevNode = node #Guardar la referencia al nodo anterior 

    #Repetir recursivamente para la subrama izquierda y la subrama derecha 
    pathSum_R(node.leftnode,x,currentSum, path,allPaths,prevNode) 
    pathSum_R(node.rightnode,x,currentSum,path,allPaths,prevNode) 


    

B = BinaryTree() 

insert(B,8,8)
insert(B,10,10)
insert(B,4,4)
insert(B,0,0)
insert(B,6,6)
insert(B,2,2)
insert(B,14,14)
print_tree(B)
print("----------------")
L = pathSum(B,18) 
printList(L)




