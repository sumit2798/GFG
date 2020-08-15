class Node:

    def __init__(self,item):
        key = item;
        self.left=None
        self.right = None;

class Tree:
    def __int__(self):
        self.left=None
        self.right=None
        self.data=data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def inorder(self,root):
        if root is None:
            return
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    def preorder(self,root):
        if root is None:
            return

        print(root.key)

        preorder(root.left)


        preorder(root.right)
    def PostOrder(self,node):
        if node is None
            return
        Postorder(node.left)

        Postorder(node.right)

        print(node.key )

c=Tree()
