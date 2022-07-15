import sys
sys.setrecursionlimit(10**6)
class TreeNode:
    def __init__(self,x,y,val=0,left=None,right=None):
        self.x=x
        self.y=y
        self.val=val
        self.left=left
        self.right=right
def postorder(root,path):
    if root==None:
        return
    postorder(root.left,path)
    postorder(root.right,path)
    path.append(root.val)
    return path
def preorder(root,path):
    if root==None:
        return
    path.append(root.val)
    preorder(root.left,path)
    preorder(root.right,path)
    return path

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x:(-x[1],x[0]))
    start=root=TreeNode(x=nodeinfo[0][0],y=nodeinfo[0][1],val=nodeinfo[0][2])
    for i in range(1,len(nodeinfo)):
        x,y,z=nodeinfo[i]
        head=root
        while head:
            if x<head.x:
                if head.left==None:
                    head.left=TreeNode(x=x,y=y,val=z)
                    break
                else:
                    head=head.left
            else:
                if head.right==None:
                    head.right=TreeNode(x=x,y=y,val=z)
                    break
                else:
                    head=head.right
    pre=preorder(root,[])
    post=postorder(root,[])
    
                    
    
    return [pre,post]
