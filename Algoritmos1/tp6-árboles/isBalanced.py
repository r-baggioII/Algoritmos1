#1)Implementar función para calcular la altura de un árbol 

#2)Implementar una función que verifique si un árbol binario está balanceado. Recordar que un árbol
#balanceado es aquel en el que la altura del subárbol izquierdo y la del subárbol derecho difiera en
#como máximo 1.

#a) Calcular la altura del subArbol izquierdo 
#b) Calcular la altura del subArbol Derecho 
#c) Verificar que leftHight - rightHigh <= 1 
#d) Repetir para cada nodo del árbol 


from binarytree import BinaryTree, print_tree, insert
from binaryTreeHeight import height_R

def isBalanced(B):
    return isBalanced_R(B.root)

##Complejidad ??? O(n²)?? 
def isBalanced_R(node): 
    if node is None: 
        return True 
    
    leftHeight = height_R(node.leftnode)
    rightHeight = height_R(node.rightnode)

    if abs(leftHeight - rightHeight) > 1: 
        return False 
    
    left = isBalanced_R(node.leftnode)
    right = isBalanced_R(node.rightnode)
    
    return left and right 



B = BinaryTree() 

insert(B,10,10)
insert(B,8,8)
insert(B,7,7)
insert(B,-2,-2)
insert(B,9,9)
insert(B,8.5,8.5)
insert(B,8,8)
insert(B,12,12)
print(isBalanced(B)) 
