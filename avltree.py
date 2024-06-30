class Node:
    def _init_(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.height = 1

def insert(root, bly):
    if not root:
        return Node(bly)
    if bly < root.val:
        root.left = insert(root.left, bly)
    else:
        root.right = insert(root.right, bly)
        
    root.height = 1 + max(ght(root.left), ght(root.right))
        
    BF = getBF(root)
    
    # Left Left (LL)
    if BF > 1 and bly < root.left.val:
        return rightRotate(root)
    
    # Left Right (LR)
    if BF > 1 and bly > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    
    # Right Right (RR)
    if BF < -1 and bly > root.right.val:
        return leftRotate(root)
    
    # Right Left (RL)
    if BF < -1 and bly < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    
    return root

def ght(root):
    if not root:
        return 0
    return root.height

def getBF(root):
    if not root:
        return 0
    return ght(root.left) - ght(root.right)

def leftRotate(A):
    B = A.right
    temp = B.left
    
    B.left = A
    A.right = temp
    
    A.height = 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))
    return B

def rightRotate(A):
    B = A.left
    temp = B.right
    
    B.right = A
    A.left = temp
    
    A.height = 1 + max(ght(A.left), ght(A.right))
    B.height = 1 + max(ght(B.left), ght(B.right))
    return B    
    
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

if __name__== "_main_":
    vl = [19, 99, 75, 7, 21, 34, 38, 27, 134, 100, 29, 0, 12, 17, 143]
    root = None
    for i in vl:
        root = insert(root, i)
        inorder(root)



    

