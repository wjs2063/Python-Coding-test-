class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self,data):
        self.head=Node(data)
    def add(self,data):
        if self.head=='':
            self.head=Node(data)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=Node(data)

string="aaaabbbccddefg"
print(string.count('aaa'))
print(string.replace('a','h'))
#원래 리스트는 변하지않고 새로운 list 를 반환

dict={1:"1",
      2:"2",
      3:"3",
      4:"4",
      5:"5",
      6:"6"  }
a=list(dict.keys())
print(a)
print(type(a))
a=dict.items()
print(a)

print(dict.get(6))
# dict.get(x) key값이 x인 value 를 불러옴 없을시 None 반환
array_2d=[[1,2,3],[4,5,6]]
print(len(array_2d[0]))

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
def solution(board,moves):
    def find_row(board,column):
        max_row=len(board)
        row=max_row
        j=0
        while board[row][column]!=0:
            j-=1
        if j==0:
            return -1
        else :
            return j+1
    table=[]
    row_len=len(board) #행 길이
    column_len=len(board[0]) # 열길이
    for i in moves:
        j=solution(board,moves)
        if j<0:
            continue
        board[]
print(solution(board,moves))



