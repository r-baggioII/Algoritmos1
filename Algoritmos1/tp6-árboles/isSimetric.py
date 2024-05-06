#Un árbol tiene una estructura simétrica si los subárboles izquierdo y derecho se reflejan entre sí: 

#Lógica para abordar el problema: 
    #Primero hago una lista de todos los posibles casos en los que árbol será simétrico. Cualquiera de los casos que no se cumpla hace que el árbol no sea simétrico
    
    #Caso 1: El árbol está vacío (considero True)
    #Caso 2: El árbol es solo la raíz (considero True)
    #Caso 3: Si la raiz tiene un hijo derecho también tiene que haber un hijo izquierdo 
    
    #Para los casos 4 y 5 usamos recursividad 
    #Caso 4: Si el nodo tiene un solo hijo hay que verificar que su hermano tenga las conexiones contrarias. Ej: Si un nodo (que no es la raíz) tiene
    #un hijo derecho, luego, su hermano necesariamente tiene que tener un hijo izquierdo 
    #Caso 5: Si el nodo tiene dos hijos entonces hay que verficiar que su hermano también tenga dos hijos 

    #Si se cumplen todas estas condiciones para cada nodo del árbol entonces devolvemos True, sino, devolvemos False 

#Implementación en pseudoPython 
#def isSimetricTree(B): 
    #Chequeamos los casos 1, 2 y 3 

    #Llamamos a la función wrapper isSimetricTree(node) 
    # return isSimetricTree_R(B.root.leftnode) and isSimetricTree_R(B.root.rightnode) 

from binarytree import BinaryTree, BinaryTreeNode, print_tree, insert, traverseInOrder
from linkedlist import LinkedList,printList 


def isSimetricTree(B):

    if B.root is None: #Caso 1 
        return True 
    if B.root.leftnode is None and B.root.rightnode is None: #Caso 2 
        return True 
    
    if B.root.leftnode is not None and B.root.rightnode is None: 
        return False 
    if B.root.rightnode is not None and B.root.leftnode is None: 
        return False
        
        
    return isSimetricTree_R(B.root.leftnode) and isSimetricTree_R(B.root.rightnode) 
      
    


def isSimetricTree_R(node): 
    
    if node is None:
        return True 
    
    #Caso 4 
    if node.leftnode is not None and node.rightnode is None: #nodo tiene hijo izquierdo
        
        #Verificar si es hijoo izquierdo o derecho del padre (para encontrar su hermano)
        if node.parent.rightnode == node: #Es hijo derecho del padre 
            if node.parent.leftnode is None: 
                return False 
            if node.parent.leftnode.rightnode is None: 
                return False 
        else: #Es hijo izquierdo del padre 
            if node.parent.rightnode is None:
                return False 
            if node.parent.rightnode.leftnode is None:
                return False
    elif node.rightnode is not None and node.leftnode is None : # nodo tiene un hijo derecho 
        if node.parent.rightnode == node:  #Es hijo derecho del padre 
            if node.parent.leftnode is None: 
                return False  
            if node.parent.leftnode.leftnode is None:
                return False
        else: #Es hijo izquierdo del padre 
            if node.parent.rightnode is None: 
                return False 
            if node.parent.rightnode.leftnode is None:
                return False 
    
    #Caso 5 - dos hijos 
    elif node.leftnode is not None and node.rightnode is not None:
        if node.parent.rightnode == node: 
            if node.parent.leftnode is None:
                return False 
            if node.parent.leftnode.leftnode is None or node.parent.leftnode.rightnode is None: 
                return False 
        else: 
            if node.parent.rightnode is None: 
                return False 
            if node.parent.rightnode.leftnode is None or node.parent.rightnode.leftnode is None:
                return False 

    
    return isSimetricTree_R(node.leftnode) and isSimetricTree_R(node.rightnode)




B = BinaryTree() 

insert(B,8,8)
insert(B,12,12)
insert(B,4,4)
insert(B,10,10)
insert(B,6,6)
insert(B,2,2)
insert(B,14,14)




print_tree(B)
print(isSimetricTree(B))


    