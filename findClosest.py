class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
    
    def insert(self, value):
# Compare the new value with the parent node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

def findClosestValueInBst(tree, target):
    curr = tree
    closest = 0
    while (curr):
        if target > curr.value:
            if curr.right != None:
                curr= curr.right
            else:
                closest=curr.value
                break
        elif target < curr.value:
            if curr.left != None:
                curr = curr.left
            else:
                closest = curr.value
                break
        else:
            closest = curr.value
            break
    return closest


root = Node(10)
root.insert(5)
root.insert(2)
root.insert(1)
root.insert(5)
root.insert(15)
root.insert(13)
root.insert(22)
root.insert(14)


root.PrintTree()
target=6
closest = findClosestValueInBst(root, target)
print("Closest to taget %d is %d" %(target, closest))


