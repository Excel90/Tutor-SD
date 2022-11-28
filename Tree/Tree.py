class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.flag = key

def insert(root, key, a = 0):
    level = a
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key , level + 1)
        else:
            root.left = insert(root.left, key, level + 1)
    return root

def inorder(root, val = []):
    vals = val
    if root:
        inorder(root.left, vals)
        vals.append(root.val)
        inorder(root.right, vals)
    return vals

def getLevels(root, a = 1, lvldata = {}):
    _lvldata = lvldata
    lvl = a
    if lvl not in _lvldata.keys():
        _lvldata[lvl] = set()
    if root:
        if root.left:
            _lvldata[lvl].add(root.val)
            getLevels(root.left, lvl + 1, _lvldata)
        if root.right:
            getLevels(root.right, lvl + 1, _lvldata)
        
        _lvldata[lvl].add(root.val)
        print(_lvldata)

# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

r = Node(2)
r = insert(r, 1)
r = insert(r, 3)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inoder traversal of the BST
print(inorder(r))
print("---------")
getLevels(r)
# print(countLevels(r))