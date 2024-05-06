from binarytree import insert, print_tree, BinaryTree, BinaryTreeNode
from linkedlist import add, printList, LinkedList,addAtTheEnd, delete

#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

def hasPathSum(B): 
    path = 0 
    sum = 30
    return hasPathSum_R(B.root,sum,path)

def hasPathSum_R(node,sum,path): 
    if node is None: 
        return  
    
    path += node.key
    if node.leftnode is None and node.rightnode is None: #Si llegamos a una hoja entonces hemos terminado un recorrido 
        return path == sum 
    
    left = hasPathSum_R(node.leftnode,sum,path)
    right = hasPathSum_R(node.rightnode,sum,path)
    
    return left or right 



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
print(hasPathSum(B))