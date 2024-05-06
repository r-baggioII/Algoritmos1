#Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. 
#Return the answer in any order.
from binarytree import print_tree,insert,traverseInOrder, BinaryTree
from linkedlist import LinkedList, printList,addAtTheEnd, delete


def weave_lists(first, second, results, prefix):
    """Recursively Weave the first list into the second list and append 
    it to the results list.  The prefix list grows by an element with the 
    depth of the call stack.  Ultimately, either the first or second list will 
    be exhausted and the base case will append a result."""
    # base case
    if not first or not second:
        results.append(prefix + first + second)
        return

    # recursive case
    first_head, first_tail = first[0], first[1:]
    weave_lists(first_tail, second, results, prefix + [first_head])

    second_head, second_tail = second[0], second[1:]
    weave_lists(first, second_tail, results, prefix + [second_head])



def BSTsequences(B): 
    if B.root is None: 
        return 
    prefix = LinkedList() 
    return BSTsequences_R(B.root)


def BSTsequences_R(node): 
    """Splits the tree into three lists: prefix, left, and right."""
    if node is None:
        return []

    answer = []
    
    prefix = [node.value]
    
    leftResult = BSTsequences_R(node.leftnode) 
    if not leftResult: 
        left = [[]]
    else: 
        left = leftResult

    rightResult = BSTsequences_R(node.rightnode) 
    if not rightResult: 
        right = [[]]
    else: 
        right = rightResult 


    # At a minimum, left and right must be a list containing an empty list
    # for the following nested loop
    for i in range(len(left)):
        for j in range(len(right)):
            weaved = []
            weave_lists(left[i], right[j], weaved, prefix)
        answer.extend(weaved)

    return answer


    
B = BinaryTree() 

insert(B,8,8)
insert(B,4,4) 
insert(B,12,12)
insert(B,2,2)
insert(B,6,6)
print_tree(B)
print("--------After entering funciton---------")
answer = BSTsequences(B) 
print("------------")
print(answer)

