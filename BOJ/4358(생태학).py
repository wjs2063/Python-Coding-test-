from collections import defaultdict
import sys
# sys.stdin.readline 을쓰지않으면 시간초과뜬다....
input=sys.stdin.readline
tree=defaultdict(int)
total=0
while True:
    s=input().rstrip()
    if not s:
        break
    tree[s]+=1
    total+=1
tree=sorted(tree.items())
for key,value in tree:
    print("%s %.4f"%(key,value/total*100))
