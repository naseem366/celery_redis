# dict1 = {575:"Apple",876:"Mango",132:"Grapes",782:"Banana"}
# d = sorted(dict1.values())
# print("Sorted keys:", d)

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

#binary = [10,20,30,40]
# def Binary(array,target):
#     low=0
#     high=len(array)-1
#     while (low<=high):
#         mid=(low+high)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#             return -1
        
# print(Binary([10,20,30,40],40))

#28 Linear search algorithm

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         print(i)
#         if arr[i] == target:
#             return i
#         return 1

# print(linear_search([27, 13, 32, 20,40],20))


# def findMissingNumbers(n):
#     output = []
#     for i in range(1,n[-1]):
#         if i not in n:
#             output.append(i)
#     return output

# listOfNumbers = [3, 5, 50,7,23,16,4,44,24,33,1]
# sortedlist = sorted(listOfNumbers)
# print(sortedlist)
# print("The missing numbers are :",findMissingNumbers(sortedlist))


                 
                 ################### Dictionary Program #############

#1 Find occurence of each character in string
#2 Find occurence of vowel present in given string
#3 Check Whether string are anagrams or not
#4 show output is ax1,by2,cz3,d4,e5,f,g
#5 Input = ABAABBCA and output = 4A3B1C

# s = 'QWERTYUIOPZXCVBNMPOIUYTREWQZMNBVCXZCVXNYIEIYOETRMB'
# d = {}
# for ch in s:
#     d[ch] = d.get(ch, 0) + 1
# for k,v in sorted(d.items()):
#     print('{} occured {} times'.format(k,v))

# s = 'uuuuuiiiooouuaaaaaeeeeeiiiQWERTYUIOPZXCVBNMPOIUYTREWQZMNBVCXZCVXNYIEIYOETRMB'
# s1 = s.upper()
# v = {'a','e','i','o,','u','A','E','I','O','U'}
# d = {}
# for ch in s1:
#     if ch in v:
#         d[ch] = d.get(ch, 0) + 1
# for k,v in sorted(d.items()):
#     print('{} occured {} times'.format(k,v))

# Input = ABAABBCA and output = 4A3B1C

# s = 'ABAABBCA'
# d = {}
# output = ''
# for ch in s:
#     d[ch ]= d.get(ch,0)+1
# for k,v in d.items():
#     output = output + k + str(v)
# print(output)

# show output is ax1,by2,cz3,d4,e5,f,g
s1 = "abcdefg"
s2 = "xyz"
s3 = '12345'
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i<len(s1):
        output = output + s1[i]
        i += 1
    if j<len(s2):
        output = output + s2[j]
        j += 1
    if k<len(s3):
        output = output + s3[k] 
        k += 1
    print(output)
