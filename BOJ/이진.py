from collections import defaultdict
import sys
input=sys.stdin.readline
tree=[]
while True:
    std_in=input().strip()
    if std_in:
        tree.append(std_in)
        continue
    break

class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Tree:
    def __init__(self):
        self.root=None

    # pulbic 메소드
    def push(self,val):
        self.root = self.__push_val(self.root,val)

    # private 메소드
    def __push_val(self,node,val):
        # none인 곳을 찾을 때 까지 삽입 위치 확인 하면서 재귀 함수
        if (node==None):
            node = Node(val)
        else:
            if (val<node.val):
                node.left=self.__push_val(node.left,val)
            else:
                node.right=self.__push_val(node.right,val)
        return node

    def print_root(self):
        print(self.root)

    def postorder(self,root):
        if (root==None):
            pass
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val,end=' ')
t=Tree()

for x in tree:
    t.push(x)
    t.postorder(t.root)
    print("\n")
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
        print(root.data,end=' ')
t=Tree()
print(tree)
for x in tree:
    t.insert(x)
    print(t.root.data)
t.postorder(t.root)