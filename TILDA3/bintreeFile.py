class Bintree:
    def __init__(self):
        self.root = None

    def store(self, key):
        self.root = recstore(self.root, key)

    def __contains__(self, key):
        return recsearch(self.root, key)

    def write(self):
        # Skriver ut trädet i inorder
        recwrite(self.root)
        print("\n")


def recstore(old, newword):
    if old is None:
        return Node(newword)

    if newword < old.val:
        if old.left is None:
            old.left = Node(newword)
        else:
            recstore(old.left, newword)

    elif newword > old.val:
        if old.right is None:
            old.right = Node(newword)
        else:
            recstore(old.right, newword)

    return old



def recsearch(old, value):
    if old is None:
        return False
    if value == old.val:
        return True
    if value < old.val:
        return recsearch(old.left, value)
    if value > old.val:
        return recsearch(old.right, value)


def recwrite(tree):
    if tree != None:
        recwrite(tree.left)
        print(tree.val)
        recwrite(tree.right)

class Node():
    def __init__(self, value):
        self.left=None
        self.right=None
        self.val=value


