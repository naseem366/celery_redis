# How will you debug a piece of code in Python?

import pdb
pdb.set_trace()

# Generate an infinite fibonaanci Series by using Generator 

def fibo():
	a,b = 0,1
	while True:
		yield a
		a,b = b,a+b

f1=fibo()
print(next(f1))
#print(next(f1))
#print(next(f1))
#print(next(f1))
#print(next(f1))
#print(next(f1))

# Find Missing Number in list 
def findMissingNumbers(n):
    numbers = set(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNumbers(listOfNumbers))


################### list using bubble sort and sort list in python without using sort function 

def bubble_sort(list1):  
    # Outer loop for traverse the entire list 
    for i in range(0,len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                temp = list1[j]  
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  

# Second Method for sorting list 

list1 = [41,2,12,6,35,8,10,1,19]
n = len(list1)
for i in range(n):
    for j in range(i+1,n):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)


###################### find the Pair with given Number in a List ###################

list1 = [8,7,2,5,3,1]
n = len(list1)
k=10
for i in range(n):
    for j in range(i+1, n):
        if (list1[i]+ list1[j]) == k:
            print(list1[i],"+",list1[j], "=" ,k)  # output - 8+2=10,7+3=10

#######################  Print Duplicate values in list  #######################


def print_duplicates(lst): 
    duplicate = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if (lst[i] == lst[j]) and not (lst[i] in duplicate):
                duplicate.append(lst[i])
    print(duplicate)
lst = ["hello",10,20,40,20,60,40,30]  # output - [20,40]
print_duplicates(lst)


################################ Print the not duplicate values ###############################

def notDuplicate(lst):
    d = []
    for i in lst:
        if lst.count(i) == 1:
            d.append(i)
    print(d)

lst = [10,20,40,20,60,40,30]
notDuplicate(lst)                          ######## OutPut [10, 60, 30]

lst = [10,20,40,20,60,40,30]

l = [i for i in lst if lst.count(i) == 1]   ######## OutPut [10, 60, 30]
     

################# Find Max,Min number in list ############################

l = [20,30,1,70,2,6,67,23]

maxi =l[0]
mini =l[0]
for i in l:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i

print('Maximum number :',maxi)  # output - 70
print('Minimum number :',mini)  # output - 1


###################### find palindrome Number in python ###################

#num=int(input("Enter a number:"))
num =123
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


################################# Segrate zeros and ones ######################################

def segregate_zeros_and_ones(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Example input array
input_array = [1, 0, 1, 1, 0, 1, 1, 0, 0]

# Segregate 0s and 1s
segregate_zeros_and_ones(input_array)

# # Output will be [0, 0, 0, 0, 1, 1, 1, 1, 1]
print("Segregated Array:", input_array)

    

##################### palindrome in strings #########################

def isPalindrome(s):
	if s == s[::-1]:
		print("Yes! This is palindrome String ")
	else:
		print("No ! This is not palindrome String")

s = "malayalam"
ans = isPalindrome(s)


################ Write a program reverse a string ? ############################
    

def reverse_string(str):  
    str1 = ""               # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1             # It will return the reverse string to the caller function  
     
str = "JavaTpoint"    # Given String       
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) # Function call  


# Function to reverse a string
def reverse(string):
	string = string[::-1]
	return string

s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))


# To reverse words in a given string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
	# appending reversed words to l
	l.append(i)
# printing reverse words
print(" ".join(l))


#######################  Remove Duplicate charcter in string  #######################
def removeDuplicate(str): 
	s=set(str) 
	s="".join(s) 
	print("Without Order:",s) 
	t="" 
	for i in str: 
		if(i in t): 
			pass
		else: 
			t=t+i 
	print("With Order:",t) 
	
str="geeksforgeeks"
removeDuplicate(str) 



# ########################## Find length of string without using any built in functions?

#string=input("Enter string:")
string = "Naseem"
count = 0
for i in string:
      count=count+1
print("Length of the string is:",count)

########################## find max number of character in (string )python ######################

s = "itininiytnnhhnn"
ch = dict()
for i in s:
    if i in ch:
        ch[i]+=1
    else:
        ch[i]=1

max_char = max(ch,key=ch.get)

print("Max_char is :",max_char)  # Max_char is : n


########################## find max number of character in (string )python ######################

s = "itininiytnnhhnn"
ch = dict()
for i in s:
    if i in ch:
        ch[i]+=1
    else:
        ch[i]=1

max_char = ch

print("Max_char is :",max_char)  # Max_char is : {'i': 4, 't': 2, 'n': 6, 'y': 1, 'h': 2}


############################ Find common string in list of string ##########################################


def longest_common_prefix(strings):
    if not strings:
        return "None"
    
    # Find the shortest string in the array
    min_str = min(strings, key=len)

    for i, char in enumerate(min_str):
        for string in strings:
            if string[i] != char:
                return min_str[:i]
    
    return min_str

# Example input array
input_array = ["flower", "flow", "fly"]

# Find the longest common prefix
result = longest_common_prefix(input_array)

# Output will be "fl"
print("Longest Common Prefix:", result)




##################################### Diamond program add,sub,mul,division #############################
    
#Python program to perform Addition, Subtraction,
#Multiplication and division of two numbers

num1= 20#int(input("Enter the first number: "))
num2= 20#int(input("Enter the second number: "))

print("Enter the operator you want to perform");

ch= '+' #input("Enter any of these operator for operation +, -, *, /  ")

result=0
if ch=='+':
    result=num1+num2;
elif ch=='-':
    result=num1-num2;

elif ch=='*':
    result=num1*num2;
elif ch=='/':
    result=num1/num2;

else:
   print("char is not supported");

print(num1,ch,num2,": ",result)

######################################## Length of longest substring in python ################

def lengthOfLongestSubstring(s: str) -> int:
    # Base condition
    if s == "":
        return 0
    # Starting index of window
    start = 0
    # Ending index of window
    end = 0
    # Maximum length of substring without repeating characters
    maxLength = 0
    # Set to store unique characters
    unique_characters = set()
    # Loop for each character in the string
    while end < len(s):
        if s[end] not in unique_characters:
            unique_characters.add(s[end])
            end += 1
            maxLength = max(maxLength, len(unique_characters))
        else:
            unique_characters.remove(s[start])
            start += 1
    return maxLength
    print(maxLength)

string = "geeksforgeeks"

print("The input string is " + string)
length = lengthOfLongestSubstring(string)

print("The length of the longest non-repeating character" + " substring is " + str(length))










