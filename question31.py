class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root is None:
            return root
        self.inorder(root.left)
        print(root.data, end="")
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return root
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end="")

    def preorder(self, root):
        if root is None:
            return root
        print(root.data, end="")
        self.preorder(root.left)
        self.preorder(root.right)

    def height(self, root):
        if root is None:
            return 0
        lt = self.height(root.left)
        rt = self.height(root.right)
        return max(lt, rt) + 1

    def totalNode(self, root):
        if root is None:
            return 0
        lt = self.totalNode(root.left)
        rt = self.totalNode(root.right)
        return lt + rt + 1

    def level_order(self, root):
        if root is None:
            return root
        q = []
        q.append(root)
        while len(q):
            t = q.pop(0)
            print(t.data, end="")
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)


t = Tree()
n1 = TreeNode(1)
t.root = n1
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(7)
n5 = TreeNode(6)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
t.inorder(n1)
print()
t.postorder(n1)
print()
t.preorder(n1)
print()
print(t.height(n1))
print(t.totalNode(n1))
t.level_order(n1)
