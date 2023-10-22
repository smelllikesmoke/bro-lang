class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, records): # root -> left -> right
        if start is not None:
            records.append(start.value)
            records = self.preorder(start.left, records = records)
            records = self.preorder(start.right, records = records)
        return records
    
    def postorder(self, start, records): # left -> right -> root
        if start is not None:
            records = self.postorder(start.left, records = records)
            records = self.postorder(start.right, records = records)
            records.append(start.value)
        return records
    

tree = Tree(5)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)

# print(tree.preorder(tree.root, []))
print(tree.postorder(tree.root, []))






















