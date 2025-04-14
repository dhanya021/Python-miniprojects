class BST:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addHelper(self, root, data):
        # Base case: reached a leaf node
        if data > root.val and root.right is None:
            root.right = BST(data)
            return "Insertion completed"
        elif data < root.val and root.left is None:
            root.left = BST(data)
            return "Insertion completed"

        # Continue traversing the tree
        if data > root.val:
            return self.add(root.right, data)
        elif data < root.val:
            return self.add(root.left, data)
        else:
            return "Insertion failed: duplicate value"

    def add(self, root, data):
        if root is None:
            return "Insertion failed: empty root"
        return self.addHelper(root, data)

    def restructureData(self, root):
        # Base case: root is null or a leaf node
        if root is None or (root.left is None and root.right is None):
            return "Restructure finished"

        # Determine child values
        leftVal = root.left.val if root.left else float('-inf')
        rightVal = root.right.val if root.right else float('inf')

        originalVal = root.val

        # Swap values based on which child has the higher priority
        if leftVal > rightVal or root.right is None:
            root.val = root.left.val
            root.left.val = originalVal
            return self.restructureData(root.left)
        else:
            root.val = root.right.val
            root.right.val = originalVal
            return self.restructureData(root.right)

    def removeHelper(self, root, data):
        if root is None:
            return "Deletion failed: value not found"

        if data > root.val:
            return self.removeHelper(root.right, data)
        elif data < root.val:
            return self.removeHelper(root.left, data)
        else:
            # Node found - prepare for restructuring
            originalVal = root.val
            leftVal = root.left.val if root.left else float('-inf')
            rightVal = root.right.val if root.right else float('inf')

            if leftVal > rightVal or root.right is None:
                root.val = root.left.val
                root.left.val = originalVal
                return self.restructureData(root.left)
            else:
                root.val = root.right.val
                root.right.val = originalVal
                return self.restructureData(root.right)

    def remove(self, root, data):
        if root is None:
            return "Deletion failed: empty tree"
        return self.removeHelper(root, data)
