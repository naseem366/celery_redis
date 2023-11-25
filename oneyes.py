              
                 ################### Dictionary Program #############

#1 Find occurence of each character in string
#2 Find occurence of vowel present in given string
#3 Check Whether string are anagrams or not
#4 show output is ax1,by2,cz3,d4,e5,f,g
#5 Input = ABAABBCA and output = 4A3B1C


########################## List program ##########################

#1 How will you debug a piece of code in Python? 
#2 Generate an infinite fibonaanci Series by using Generator
#3 print fibonacci series 
#3 Find Missing Number in list 
#4 list using bubble sort and sort list in python without using sort function 
#5 find the Pair with given Number in a List 
#6 Print Duplicate values in list 
#7 Print the not duplicate values
#8 Find Max,Min number in list
#9 find palindrome Number in python 
#10 Segrate zeros and ones 
#11 print average of number
#13 print Prime number 
#14 Swap two number 
#15 factorial of number 
#16 sum of natural number 
#19 Armstrong number checker ,371,153,1634
#28 Linear search algorithm
#27 Binary search algorithm

              ########################## String program Start ##########################

# palindrome in strings
# Write a program reverse a string
# reversed string world of string 
# (1-Method) Remove Duplicate charcter in string
# (2-Method) Remove Duplicate charcter in string
# (3-Method) Remove Duplicate charcter in string
# Find length of string without using any built in functions?
# find max number of character in (string )python
# (1-Method) find occurence of each character present in string
# (2-Method) find occurence of each character present in string
# Find common string in list of string                          ####### After
# reserverd every secound element in the string                
# Print even and odd index in string
# Merge the two string s1="abcde",s2="1234567"
# Sort character of the string first alphabet symbols followed by digits
# input a4b3c2 and expected output aaaabbbcc
# input aaaabbbccz and excepted output 4a3b2c1z
# input a4k3b2 and excepted output aeknbd


# # Convert given numbers of days into years,week and days
# # Given: 365 days
# # Expected Output : 1 year(s), 4 week(s), 1 day(s)

# def ConvertDays(nums):
#     num_days = int(nums)
#     num_years = num_days // 365
#     num_weeks = num_days // 7
#     num_days =  num_days
#     return f'{num_years} year(s), {num_weeks} week(s), {num_days} day(s)'

# print(ConvertDays(59444))


         ################################ Find the Sum and Average ####################################
         
# l1 = [1,2,3,4,5]
# count=0
# sum_nums = sum(l1)
# for i in l1:
#     count+=i
# print("sum of ",count)
# avg = count/len(l1)
# print("Sum of",count,"Average",avg)

         ##################### Temperature in Celsius convert to Kelvin ###########################

# Celsius to Kelvin = celsius + 273.15 
# celsium to Fahenheit = celsius*9/5+32 

# temp_celsius = float(input('Enter temperature in celsius '))
# kelvin = temp_celsius + 273.15 
# print(f'Temperature in Kelvin is {kelvin}')

############### Given a list of names concatenate them into a single string separated by space ######################

# l1 = ['geeks', 'for', 'geeks']
# l2 = ' '.join(l1)
# print(l2)

# ############### Check string is pangram(Contains all letters of thr alphabet) ######################

# s1 = 'abcdefghijklmnopqrstuvxyz'
# pangram = "The quick brown fox jumps over the lazy dog"
# if sorted(pangram.upper())==sorted(s1.upper()):
#     print("string is pangram ")
# else:
#     print("Not a pangram")



# def lengthOfLongestSubstring(s: str) -> int:
#     # Base condition
#     if s == "":
#         return 0
#     # Starting index of window
#     start = 0
#     # Ending index of window
#     end = 0
#     # Maximum length of substring without repeating characters
#     maxLength = 0
#     # Set to store unique characters
#     unique_characters = set()
#     # Loop for each character in the string
#     while end < len(s):
#         if s[end] not in unique_characters:
#             unique_characters.add(s[end])
#             end += 1
#             maxLength = max(maxLength, len(unique_characters))
#         else:
#             unique_characters.remove(s[start])
#             start += 1
#     return maxLength
#     print(maxLength)

# string = "geeksforgeeks"

# print("The input string is " + string)
# length = lengthOfLongestSubstring(string)

# print("The length of the longest non-repeating character" + " substring is " + str(length))


# import _thread # import the thread module  
# import time # import time module  
  
# def cal_sqre(num): # define the cal_sqre function  
#     print(" Calculate the square root of the given number")  
#     for n in num:   
#         time.sleep(0.3) # at each iteration it waits for 0.3 time  
#         print(' Square is : ', n * n)  
  
# def cal_cube(num): # define the cal_cube() function  
#     print(" Calculate the cube of  the given number")  
#     for n in num:   
#         time.sleep(0.3) # at each iteration it waits for 0.3 time  
#         print(" Cube is : ", n * n *n)  
  
# arr = [4, 5, 6, 7, 2] # given array  
  
# t1 = time.time() # get total time to execute the functions  
# cal_sqre(arr) # call cal_sqre() function  
# cal_cube(arr) # call cal_cube() function  
  
# print(" Total time taken by threads is :", time.time() - t1) # print the total time



# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i*2+1):
#         if i%2 == 0:
#             print("#",end="")
#         else:
#             print("$",end="")
#     print() 


# n = 5
# i = 0

# while i < n:
#     j = i
#     while j < n:
#         print(" ", end="")
#         j += 1

#     j = 0
#     while j < i * 2 + 1:
#         if i % 2 == 0:
#             print("#", end="")
#         else:
#             print("$", end="")
#         j += 1

#     print()
#     i += 1


# def lengthOfLongestSubstring(s):
#         maxLen = 1
#         if s == '':
#             return 0                      # Dealing with one edge case
#         for i in range(len(s)):
#             substring = s[i]              # Initialising the substring
#             for j in range(i+1, len(s)):  # Starting to append characters to substring from i+1
#                 if s[j] not in substring: # As long as its not repeating. "not in" can be used to check if the character isn't already there in the substring
#                     substring = substring + s[j]
#                     #print(substring)
#                     maxLen = max(maxLen, len(substring)) # Updating maxLen if it is greater than the existing maxLen
#                     maxSubstring = max(substring,key=len)
#                 else:
#                     break
#         return maxLen #maxSubstring


# print(lengthOfLongestSubstring('abcabcdbb'))


# def SortNumber(numList):
#     for i in range(len(numList)):
#         for j in range(i+1,len(numList)):
#             if numList[i]>numList[j]:
#                 numList[i],numList[j]=numList[j],numList[i]
#                 # temp = numList[i]
#                 # numList[i]=numList[j]
#                 # numList[j]=temp
#     return numList
# numList = [34,67,89,12,345,76,890,12]
# print(SortNumber(numList))

# def missing(num):
#     n=set(num)
#     output=[]
#     for i in range(1,num[-1]):
#         if i not in n:
#             output.append(i)
#     return output

# num=[1,2,3,4,10]
# print(missing(num))

# def SortNumber(numList):
#     duplicate = []
#     for i in range(len(numList)):
#         for j in range(i+1,len(numList)):
#             if (numList[i] == numList[j])  and not (numList[i] in duplicate):
#                 duplicate.append(numList[i])
#     print(duplicate)
# list1 = [8,7,2,3,5,6,7,8,8,8,8,8,4,5,5,3,1]
# SortNumber(list1)


# s = 'AZZZZBCDABBCDSDJKFSDJFDJJJHHGHGFHDHJFGDGFUEWRUEWRHIWERFJ'
# output = []
# for ch in s:
#     if ch not in output:
#         output.append(ch)
# for ch in sorted(output):
#     print("{} occured {} time ".format(ch,s.count(ch)))


# s = "one two three four five"
# l=s.split()
# print(l)
# out = []
# i=0
# while i<len(l):
#     if i%2==0:
#         out.append(l[i])
#     else:
#         out.append(l[i][::-1])
#     i=i+1
# print(out)


## Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence
#fruits = ['mango','apple','pipeapple','banana','grape','orange','cherry','apricot']
# if 'mango' in fruits:
#     print(fruits)

# Create a list of fruits and add a new fruit to the list.
# fruits = ['mango','apple','pipeapple','banana','grape']
# fruits.append('cherry')
# print(fruits)

# Access elements in a tuple using indexing.
# fruits = ('mango','apple','pipeapple','banana','grape')
# print(fruits[2])



# ## Given two dictionaries, merge them into a single dictionary
# dict1 = {'name':'John', 'age':25}
# dict2 = {'city':'New York', 'country':'USA'}
# merged_dict = {**dict1, **dict2}
# print(merged_dict)

# dict1.update(dict2)
# print(dict1)

# # Implement a function that removes a key-value pair from a dictionary 
# # def removeKeyValuePairFromDict(dictionary,key):
# #     del dictionary[key]
# #     return dictionary
# myDictionary = {"a":1,"b":2,"c":3,"d":4}
# myDictionary.pop('b')
# print(myDictionary)

# ## Given a list of dictionaries, find the dictionary with the highest value for a specific key
# def getMaxValInListOfDictionaries(listofDict):
#     sort_values = sorted(listofDict)
#     return sort_values

# data = [{"name":"Alice","age":30},{"name":"Bob","age":28},{"name":"Charlie","age":26}]
# maxAgePerson = max(getMaxValInListOfDictionaries(data,key=lambda k:k['age']))
# #maxAgePerson = getMaxValInListOfDictionaries(data)
# print(maxAgePerson['name'])

# ##Given two sets, find the union, intersection, and difference between them
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# unionSet = set1.union(set2)
# intersectionSet = set1.intersection(set2)
# differenceSet = set1.difference(set2)
# print("Union Set is : ",end="")
# for i in unionSet:
#     print("%s " %i, end=" ")
# print("\nIntersection Set is : ",end="")
# for i in intersectionSet:
#     print("%s " %i, end=" ")
# print("\nDifference Set is : ",end="")
# for i in differenceSet:
#     print("%s " %i, end=" ")


# list1 = [1,2,3,45,5,66,77,89]
# x = list(filter(lambda n:n%2==0,list1))
# print("Filter Values ",x)

# y = list(map(lambda n:n*2,list1))
# print("Map Values ",y)

# z = list(reduce(lambda a,b:a+b,list1))
# print(z)

# def UserDetails(**kwargs):
#     for val,key in kwargs.items():
#         print("{}:-{}".format(val,key))
# UserDetails(name='naseem',id=7412)

# res = lambda *args:sum(args)
# print("args function = ",res(20,30,50))

# res1 = lambda **kwargs:sum(kwargs.values())
# print("kwargs function = ",res1(a=10,b=30,c=60))


# def product(nums):
#     total = 1
#     for i in nums:
#         total*=i
#     return total
# res = lambda **kwargs : product(kwargs.values())
# print(res(a=20,b=30,c=40))

# ### Multi-threading 
# from time import sleep
# from threading import Thread

# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Naseem")
#             sleep(2)
# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("saima")
#             sleep(2)

# t1 = A()
# t2 = B()

# t1.start()
# t2.start()

# ### Exception Handling in python 
# a = 10
# b = 0
# try: 
#     c = a/b
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# finally:
#     # this block is always executed 
#     # regardless of exception generation. 
#     print('This is always executed') 




# class Overloading():
#     def func(self,name=""):
#         self.name = name
#         print(name)
    
# t1= Overloading()
# t1.func()

#1 to 100

# n = 100
# for num in range(n):
#     if num>1:
#         for i in range(2,num):
#             if(num%i==0):
#                 break
#         else:
#             print(num)

# print(5/2) ## 2.5
# print(5//2) ## 2   # beacause floor division remove from this 


# d = {str(i):i for i in range(1,4)}
# print(d)


# def mygen():
#     print("first item")
#     yield 10
#     print("second item")
#     yield 20
#     print("third item")
#     yield 30
    
    
# gen = mygen()
# print(gen.__next__())

# def TopFiveNum():
#     try:
#         n=1
#         while n<=5:
#             yield n
#             n=n+1
#     except StopIteration as e:
#         print("StopIteration error handled successfully")

# gen = TopFiveNum()
# print(gen.__next__())

# def TopFiveNum():
#     n = 1
#     while n <= 5:
#         yield n
#         n = n + 1

# gen = TopFiveNum()

# try:
#     while True:
#         value = next(gen)
#         print(value)
# except StopIteration:
#     print("End of the generator.")

# gen = (x**2 for x in range(1,11))
# print(list(g for g in gen))

# def decor_function(result_function):
#     def distinction_function(marks):
#         for i in marks:
#             if i >= 75:
#                 print("Distinction")
#         result_function(marks)        
#     return distinction_function

# @decor_function
# def result(marks):
#     for i in marks:
#         if i>=33:
#             pass
#         else:
#             print("Fail")
#             break
#     else:
#         print("Pass")
# result([78,35,34,55,89])

# ######## Single Inheritance 

# class Parent():
#     def __init__(self,name):
#         self.name = name
#     def func1(self):
#         print("Parent Function invoke so Name is = ",self.name)

# class Child(Parent):
#     def __init__(self, name,age):
#         Parent.__init__(self,name)
#         self.age = age
#     def func2(self):
#         print("Child function invoke so Age is ",self.age)

# obj = Child('Naseem',24)
# obj.func1()
# obj.func2()


##### Multiple Inheritance 

# class Mother():
#     def motherfunc(self):
#         print("Mother function invoke")

# class Father():
#     def fatherfunc(self):
#         print("Father function invoke")

# class Child(Mother,Father):
#     def parent(self):
#         self.motherfunc()
#         self.fatherfunc()
#         print("Parent function invoke")

# obj = Child()
# obj.parent()


#### Multilevel Inheritance 

# class GrandFather():
#     def __init__(self,grandfathername):
#         self.grandfathername = grandfathername
# class Father(GrandFather):
#     def __init__(self, grandfathername,fathername):
#         super().__init__(grandfathername)
#         self.fathername = fathername

# class Son(Father):
#     def __init__(self, grandfathername, fathername,sonname):
#         super().__init__(grandfathername, fathername)
#         self.sonname = sonname
#     def display(self):
#         print("GrandFather Name is = ",self.grandfathername)
#         print("Father Name is = ",self.fathername)
#         print("Son Name is = ",self.sonname)
    
# obj = Son("CSJMUK","RKTIC","PTNIC")
# obj.display()


### Heirarical Inheritance 

# class Parent():
#     def parent(self):
#         print("parent function invoke")

# class Child1(Parent):
#     def childfunc(self):
#         print("Parent function invoke")
# class Child2(Parent):
#     def childfunc2(self):
#         print("GrandChild function invoke")
# obj = Child1()
# obj1 = Child2()
# obj1.childfunc2()


### Encapsulation 

# class Emp():
#     def __init__(self,name,project):
#         self.name = name          
#         self.project  = project
#     def work(self):
#         print(self.name,"Working on project ",self.project)
    
# obj = Emp('MakeMyPath','Lucknow')
# obj.work()


# ## PolyMorphism Function 

# class Car():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def display(self):
#         print("Drive Car ",self.brand,self.model)

# class Boat():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def display(self):
#         print("Sail Boat ",self.brand,self.model)

# class Plane():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def display(self):
#         print("Fly Plane ",self.brand,self.model)

# car1 = Car('Ford','Mustang')
# boat1 = Boat('Ibiza','toring 20')
# plane1 = Plane('Boing','776')

# # car1.display()
# # boat1.display()
# # plane1.display()

# for x in (car1,boat1,plane1):
#     x.display()


### Overriding in python 
class Overriding():
    def __init__(self,name=""):
        self.name = name
    def display(self):

        print("welcome to ",self.name)

obj = Overriding()
obj.display()