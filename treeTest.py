import sys

class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        newNode = Node(data)
        root = self
        trailing = None
        while root != None:
            trailing = root
            if data < root.data:
                root = root.left
            else:
                root = root.right
        if trailing == None:
            trailing = newNode
        elif data < trailing.data:
            trailing.left = newNode
        else:
            trailing.right = newNode
        return trailing


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

with recursionlimit(10000000):
    print(sys.getrecursionlimit())

    root = Node(1000)
    for i in range(1, 1000):
        root.insert(i)
    for i in range(1001,2001):
        root.insert(i)

    root.PrintTree()