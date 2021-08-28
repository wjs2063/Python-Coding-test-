from collections import defaultdict
import sys
sys.setrecursionlimit(20000)
input=sys.stdin.readline
tree=[]
while True:
    std_in=input().strip()
    if std_in:
        tree.append(int(std_in))
        continue
    break
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class Tree:
    def __init__(self):
        self.root = None
    # public
    def insert(self, data):
        self.root = self.insert_value(self.root, data)
    # private
    def insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)
        return node
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
t=Tree()
for x in tree:
    t.insert(x)
t.postorder(t.root)