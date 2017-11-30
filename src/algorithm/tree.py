class BinaryTree(object):
    def __init__(self, item):
        self.key = item
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, item):
        if self.leftChild is None:
            self.leftChild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insetRight(self, item):
        if self.rightChild is None:
            self.rightChild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.rightChild = self.rightChild
            self.rightChild = t
