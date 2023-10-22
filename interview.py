# How will you debug a piece of code in Python?

import pdb
pdb.set_trace()

# Generate an infinite fibonaanci Series by using Generator 
# fibo - 0,1,1,2,3,5,8,13,21

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

#################################### Fibo series with recursion ######################################

def fibo(n):
    if n<=0:
        return 0
    elif n==1 or n == 2 :
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=10
for i in range(n):
    print(fibo(i))



# Find Missing Number in list 
def findMissingNumbers(n):
    numbers = set(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
    
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16,4]
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

################################# Print Prime Number 1 to 20  ######################################

def PrimeNumbers(n):
    for num in range(n):
        if num>1:
            for i in range(2,num):
                if (num%i==0):
                    break
            else:
                print(num)
n=20                                 # output - 2 3 5 7 11 13 17 19
PrimeNumbers(n)

################################# Factorial of number  ######################################

def FactorialNumber(n):
    if n<1:
        return 1
    else :
        return (n*FactorialNumber(n-1))
    
print(FactorialNumber(5))     # output - 120

################################# Check Number is Armstrong or not   ######################################
#Armstrong number = 371,153,1634

n=153
output = []
str1 = str(n)
cout = len(str1)
for i in str1:
    output.append(int(i))
x=[x**cout for x in output]
sumlist=sum(x)
if sumlist == n:
    print("number is Armstrong")
else:
    print("number is not armstrong ")

################################# Swap two  number  ######################################

def SwapNumbers(a,b):
    temp = a
    a = b
    b=temp
    print(a,b)
SwapNumbers(4,7)

################################# Sum of Natural number  ######################################
def NaturalNumberSum(n):
    if n==0:
        return 0
    else :
        return (n+NaturalNumberSum(n-1))
    
print(NaturalNumberSum(5))

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

################################## print average of number ################################################

n = int(input("Number of Elements to take average of: "))
element = int(input("Enter the element: "))
l = []
for i in range(1,n+1):
    l.append(element)
average = sum(l)/n
print("Average of the elements in list",round(average,2))
    

      ############################### Strings Program start ###################################################

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


####################### (1-Method) Remove Duplicate charcter in string  #######################

s = 'AZZZZBCDABBCDSDJKFSDJFDJJJHHGHGFHDHJFGDGFUEWRUEWRHIWERFJ'
output = []
for ch in s:
    if ch not in output:
        output.append(ch)
output=''.join(output)

print(output)

####################### (2-Method) Remove Duplicate charcter in string  #######################

s = 'AZZZZBCDABBCDSDJKFSDJFDJJJHHGHGFHDHJFGDGFUEWRUEWRHIWERFJ'
output = ''
for ch in s:
    if ch not in output:
        output=output+ch

print(output)


###################### (3-Method) Remove Duplicate charcter in string  #######################

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

########################## (1-Method) find occurence of each character present in string #########################

s = 'wwwwwfffrrraaerwrwraarrrraaeeerrrr'
output = []
for ch in s:
    if ch not in output:
        output.append(ch)
for ch in sorted(output):
        #print(s.count(ch))
        print('{} occurs {} times '.format(ch,s.count(ch)))
        
########################## (2-Method) find occurence of each character present in string #########################

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


############################################ reserverd every secound element in the string ########################

s = "one two three four five"
l=s.split()
i=0
l1=[]
while i<len(l):
    if i%2 ==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
output = ' '.join(l1)
print(output)                    ########### output - one owt three ruof five


######################### Print even and odd index in string ################

s = "abcdefgh"
i=0
print("Even Index ")
while i<len(s):
    print(s[i])
    i=i+2
i = 1
print("Odd Index ")
while i<len(s):
    print(s[i])
    i=i+2

print("Even Index = ",s[0::2])  ##### output -  aceg
print("Odd Index = ",s[1::2])   ###### output -  bdfh 


################################ Merge the two string ########################
s1 = "AAAAAAAAAAAAAAAAAA"
s2 = "BBBBBBBBBB"
output = ""
i,j = 0,0

while i<len(s1) or j<len(s2):
    if i<len(s1):
        output = output+s1[i]
        i=i+1
    if j<len(s2):
        output = output+s2[j]
        j=j+1
print(output)                    # output - ABABABABABABABABABABAAAAAAAA


##################### Sort character of the string first alphabet symbols followed by digits ####################

s = "B4A1D3"
alphabets = []
digits = []
for i in s:
    if i.isalpha():
        alphabets.append(i)
    else:
        digits.append(i)
output = ''.join(sorted(alphabets)+sorted(digits))
print(output)                                         ########### output - ABD134


#### input a4b3c2 and expected output aaaabbbcc

s = "a4b3c2"
output=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d = int(ch)
        output = output+x*d

print(output)


############################### input aaaabbbccz and excepted output 4a3b2c1z ############################################

s = 'aaaabbbccz'
previous = s[0]
output = ''
c = 1
i = 1
while i<len(s):
    if s[i] == previous:
        c=c+1
    else:
        output = output+str(c)+previous
        previous=s[i]
        c=1
    if i==len(s)-1:
        output = output + str(c) + previous
    i = i+1
print(output)


############################### input a4k3b2 and excepted output aeknbd ############################################

s = 'a4k3b2'
output = ''
for ch in s:
    if ch.isalpha():
        output = output+ch
        x=ch
    else:
        d = int(ch)
        newchar = chr(ord(x)+d)
        output = output + newchar
print(output)


                 ################### Dictionary Program #############

######################################## Find occurence of each character in string #################################

s = 'wwwwwfffrrraaerwrwraarrrraaeeerrrr'
d = {}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print('{} occures {} times '.format(k,v))


################################## Find occurence of vowel present in given string ######################################

s = input("Enter Any string to search for the vowels: ")
v = {'a','e','i','o,','u','A','E','I','O','U'}
d = {}
for ch in s:
    if ch in v:
        d[ch] = d.get(ch, 0) + 1
for k,v in sorted(d.items()):
    print('{} occurs {} times'.format(k,v))


#################################### Check Whether string are anagrams or not #########################################

s1=input("Enter first string ")
s2=input("Enter secound string ")
if sorted(s1)==sorted(s2):
    print("both are Anagrams string ")
else:
    print("string are not Anagrams  ")


############################### show output is ax1,by2,cz3,d4,e5,f,g ##############################################

s1 = "abcdefg"
s2 = "xyz"
s3 = '12345'
i=j=k= 0

while i<len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i<len(s1):
        output = output+s1[i]
        i=i+1
    if j<len(s2):
        output = output+s2[j]
        j=j+1
    if k<len(s3):
        output = output+s3[k]
        k=k+1
    print(output)       

################################# Input = ABAABBCA and output = 4A3B1C  ######################################

s = 'ABAABBCA'
d={}
output = ''
for ch in s:
    d[ch] = d.get(ch,0) + 1
for k,v in sorted(d.items()):
    output = output + str(v) + k
print(output)        

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
