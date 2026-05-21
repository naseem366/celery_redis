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


# a = [1,2,3,4,5,6,7,8,9,1,4,6,8,9,13,12,11,12,1,20]

# duplicate = []
# not_duplicate = []

# for i in a:
#     if a.count(i) > 1:
#         if i not in duplicate:
#             duplicate.append(i)
#     else:
#         not_duplicate.append(i)

# print("Duplicate values:", duplicate)
# print("Not duplicate values:", not_duplicate)



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
    

# import gc

# a = [1, 2, 3]
# b = {"a": 1, "b": 2}
# c = "Hello, world!"

# del a,b,c
# gc.collect()
# print("Garbage collection complete.")


# import threading
# import time

# def worker():
#     print("Worker thread is starting.")
#     time.sleep(2)
#     print("Worker thread is ending.")

# t1 = threading.Thread(target=worker)
# t2 = threading.Thread(target=worker)

# t1.start() # Start the first thread
# t2.start() # Start the second thread

# t1.join() ## Wait for t1 to finish before proceeding
# t2.join() ## Wait for t2 to finish before proceeding

# print("Main thread is ending.")

# from multiprocessing import Process
# import time

# def task(name):
#     print(f"Process {name} is starting.")
#     time.sleep(2)
#     print(f"Process {name} is ending.")

# if __name__ == "__main__":
#     p1 = Process(target=task, args=("A",))
#     p2 = Process(target=task, args=("B",))

#     p1.start() # Start the first process
#     p2.start() # Start the second process

#     p1.join() ## Wait for p1 to finish before proceeding
#     p2.join() ## Wait for p2 to finish before proceeding

#     print("Main process is ending.")


gives all query for interview for 5 years of experience SQL interview queries