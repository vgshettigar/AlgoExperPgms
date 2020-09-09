from binarytree import build
class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

def calulateSum(root, sum, mySumlist):
    if root == None:
        return    
    sum += root.value

    if root.left == None and root.right == None:
        mySumlist.append(sum)
    
    calulateSum(root.left, sum, mySumlist)
    calulateSum(root.right, sum, mySumlist)


def branchSums(root):
    mySumlist =[]
    sum = 0
    calulateSum(root, sum, mySumlist)
    print(mySumlist)
    return mySumlist

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)

root.right.left = Node(6) 
root.right.right = Node(7) 

branchSums(root)
