import re
new_id="=.="
new_id=new_id.lower()
p=re.compile('[a-z0-9]+|[.]+|[_]+|[-]+')
new_id=p.findall(new_id)
new_id="".join(new_id)
p=re.compile('[.]+')
new_id=p.sub(".",new_id)
try:
    if new_id[0]==".":
        new_id=new_id[1:]

    if new_id[-1]==".":
        new_id=new_id[0:-1]
except:
    if new_id=="":
        new_id+="a"
if len(new_id)>=16:
    new_id=new_id[:15]
    if new_id[-1]==".":
        new_id=new_id[:-1]
if len(new_id)<=2:
    last=new_id[-1]
    while len(new_id)!=3:
        new_id+=last
        
print(new_id)