from binarytree import insert, print_tree, BinaryTree, BinaryTreeNode
from algo1 import * 

#minimalTree(array): 
    #Crear una estructura de tipo BinaryTree 
    #Buscar el elemento del centro del array (dependerá si tiene dimensión par o impar) 
    #Crear un nodo de tipo BinaryTreeNode cuya key va a ser el "midElement" que encontramos 
    #A partir del midElement dividimos el arreglo en dos subArreglos (leftArray, rightArray)
    #Llamamos a una función wrapper minimalTree_R(currentNode,leftArray,rightArray)
    # ---- recursividad ----# 
    # Devolver el árbol binario de búsqueda B 

#minimalTree_R(currentNode,leftArray,rightArray): 
    #Crear dos nodos de tipo BinaryTreeNode (nodo izquierdo y derecho)
    #Buscar el elemento central de ambos arrays y asignarlos respectivamente como las keys de los nodos 
    #Asignar ambos nodos como hijos izquierdo y derecho de currentnode respectivamente 
    #Repetir el proceso recursivamente para el nodo izquierdo (leftNode) y el nodo derecho (rightNode)
    #El caso base recursividad ocurre cuando el arreglo tenga longitud 1 

#Time complexity O(nlogn)

def minimalTree(array): 
    
    B = BinaryTree()
    node = BinaryTreeNode()
    B.root = node #El nodo creado es la raiz del árbol 
    
    #Buscamos la posición en la que se encuentra el elemento del medio 
    position = midElementPos(array)
    
    #Asigamos como key el elemento del array en esa posición
    node.key = array[position]

    #Llamamos a una función para obtener el array izqueirdo y array derecho 
    leftArray, rightArray = splitArray(array,position)

    #Pasamos a la función wrapper y usamos la recursividad
    #Devolver el árbol 
    minimalTree_R(B.root,leftArray,rightArray)
    return B 

    


#Funcion wrapper 
def minimalTree_R(currentNode,leftArray,rightArray): 

    
    #Crear dos nodos de tipo BinaryTreeNode 
    leftChild = BinaryTreeNode()
    rightChild = BinaryTreeNode()
    #Caso base 
    
    #Ambos arreglos tienen longitud 1 
    if len(leftArray) == 1 and len(rightArray) == 1: 
        leftChild.key = leftArray[0] 
        currentNode.leftnode = leftChild

        rightChild.key = rightArray[0]
        currentNode.rightnode = rightChild
        return currentNode


    #Buscamos el elemento central de cada array y lo asignamos como key a cada nodo respectivamente 
    leftChild.key = leftArray[midElementPos(leftArray)]

    rightChild.key = rightArray[midElementPos(rightArray)]

    #Insertarmos los nodos como hijos de currentNode 
    currentNode.leftnode = leftChild
    currentNode.rightnode = rightChild

    #Crear nuevos subArreglos 
    newLeftArray, newRightArray = splitArray(leftArray,midElementPos(leftArray))

    #Repetir recursivamente hasta el caso base 
    minimalTree_R(currentNode.leftnode,newLeftArray,newRightArray)

    newLeftArray, newRightArray = splitArray(rightArray,midElementPos(rightArray))
    minimalTree_R(currentNode.rightnode, newLeftArray, newRightArray)
  

  
#Devuelve la posición en la que se encuentra el elemento central
def midElementPos(array): 
    if len(array) % 2 == 0: 
        position = int(len(array)/2) - 1 
    else: 
        position = int(len(array)/2) 
    return position


#Dado un array lo divide a la mitad y separa sus elemenentos en dos subArreglos 
def splitArray(array,position): 
    
    leftArray = []
    rightArray = []

    for i in range (len(array)): 
        if i == position: 
            pass 
        elif i < position: 
            leftArray.append(array[i])
        else: 
            rightArray.append(array[i])
    
    return leftArray,rightArray


array = [2,4,6,8,10,12,14]
B = minimalTree(array)
print_tree(B)




        




