from binarytree import BinaryTree, BinaryTreeNode, print_tree, insert, traverseInOrder 


def invertBinaryTree(B): 
    if B.root is None:
        return None 
    
    inverBinaryTree_R(B.root)
    return B 


def inverBinaryTree_R(node): 
    if node is None: 
        return 
    
    #Store the reference to left and right subtrees
    leftRef = node.leftnode 
    rightRef = node.rightnode 
    
    #Delete both subtrees
    node.leftnode = None 
    node.rightnode = None 
    
    #Exchange them and add them to the tree 
    node.leftnode = rightRef
    node.rightnode = leftRef 

    inverBinaryTree_R(node.leftnode)
    inverBinaryTree_R(node.rightnode)


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
B = invertBinaryTree(B)
print("----------------")
print_tree(B)