### Find freq for each charecter
from collections import Counter

text = "Farzana"
count = Counter(text)
for char,freq in count.items():
    print(f"{char} is {freq}")
    

##### Using dict #######

d = dict()
for ch in text:
    d[ch] = d.get(ch,0)+1

for char,freq in d.items():
    print(f"Using {char} is {freq}")


###### Find the duplicate and not duplicate

a = [1,2,3,4,5,6,7,8,9,1,4,6,8,9,13,12,11,12,1,20]

print(set([x for x in a if a.count(x)==1]))

dup =[]
seen =[]
for x in a:
    if x in seen and x not in dup:
        dup.append(x)
    else:
        seen.append(x)
print(dup)


d = dict()
for x in a:
    d[x] = d.get(x,0)+1

for k,v in d.items():
    if v>1:
        print(k)



    
