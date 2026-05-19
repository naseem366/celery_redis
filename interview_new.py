# ### Find freq for each charecter
# from collections import Counter

# text = "Farzana"
# count = Counter(text)
# for char,freq in count.items():
#     print(f"{char} is {freq}")
    

# ##### Using dict #######

# d = dict()
# for ch in text:
#     d[ch] = d.get(ch,0)+1

# for char,freq in d.items():
#     print(f"Using {char} is {freq}")


# ###### Find the duplicate and not duplicate

# a = [1,2,3,4,5,6,7,8,9,1,4,6,8,9,13,12,11,12,1,20]

# print(set([x for x in a if a.count(x)==1]))

# dup =[]
# seen =[]
# for x in a:
#     if x in seen and x not in dup:
#         dup.append(x)
#     else:
#         seen.append(x)
# print(dup)


a = [1,2,3,4,5,6,7,8,9,1,4,6,8,9,13,12,11,12,1,20]

duplicate = []
not_duplicate = []

for i in a:
    if a.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)
    else:
        not_duplicate.append(i)

print("Duplicate values:", duplicate)
print("Not duplicate values:", not_duplicate)



# d = dict()
# for x in a:
#     d[x] = d.get(x,0)+1

# for k,v in d.items():
#     if v>1:
#         print(k)


# keys = ['a','b','c','d','e','f']
# values = [1,2,4,3,5,6]

# d = dict(zip(keys,values))
# print(d)

# da = {key:value for key,value in zip(keys,values)}
# print(da)


# import sys

# x = [1, 2, 3]
# print(sys.getrefcount(x)) 

# y = x
# print(sys.getrefcount(x)) 

# y = None
# print(sys.getrefcount(x))
    

import gc

a = [1, 2, 3]
b = {"a": 1, "b": 2}
c = "Hello, world!"

del a,b,c
gc.collect()
print("Garbage collection complete.")