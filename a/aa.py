from collections import defaultdict,Counter
string="asda"	
toss=""
rest=""
string=string.lower()
strings=list(string)
string_dict=defaultdict(int)
for strs in strings:
    string_dict[strs]+=1
count_string=Counter(string_dict).most_common()
count_string.sort(key=lambda x:(x[1],x[0]),reverse=True)
max_val=count_string[0][1]
print(count_string,max_val)
# T,O,S 순서부터
for key,value in count_string:
    if key=='t' and value==max_val:
        toss+='T'
for key,value in count_string:
    if key=='o' and value==max_val:
        toss+='O'
for key,value in count_string:
    if key=='s' and value==max_val:
        toss+='SS' 
for key,value in count_string:
    if key=='t' or key=='o' or key=='s':
        continue
    if value==max_val:
        rest+=key
answer=toss+rest[::-1]
print(answer)



