#Write an algorythm that decides if a given tree is a BST. Use a function called is BST that returns True or False 
#Verify that for each node that all the nodes on the left are less and that all the nodes on the right are more 
 
from binarytree import BinaryTree, BinaryTreeNode, print_tree, insert, traverseInOrder
from linkedlist import LinkedList,printList 

#O(n) approach 
def checkBST(B): 
    validBST = isBST_R(B.root,float('-inf'),float('inf')) 
    return validBST


def isBST_R(node,minVal,maxVal):
    if node is None: 
        return True 
    
    if node.key >= maxVal or node.key <= minVal: 
        return False
    
    return isBST_R(node.rightnode,node.key,maxVal) and isBST_R(node.leftnode,minVal,node.key)


#O(n) approach 

#1) Traverse InOrder 
#2) Check if the keys are InOrder (from smallest to greatest)

def is_ordered_linked_list(L):
    if L.head is None or L.head.nextNode is None: 
        return True 
    currentNode = L.head
    while currentNode.nextNode is not None: 
        if currentNode.value >= currentNode.nextNode.value: 
            return False 
        currentNode = currentNode.nextNode 
    return True 










B = BinaryTree() 

D = BinaryTree()

