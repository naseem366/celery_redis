### Implement a program that finds the largest number in the list 
lst = [2,4,1,55,6,9]
max_val = lst[0]
for val in lst:
    if val > max_val:  
        max_val = val
print ("The maximum value is :", max_val)


### Calculate the compound interest for a given principal amount, interest rate, and time period
# The formula used is: The formula is : CI = P(1+R/100)^T - P
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
compound_interest = principal * ((1 + rate/100) ** time) - principal
print("The compound interest is:", compound_interest)


### Write a program that converts a given number of days into years, weeks, and days
days = int(input("Enter the number of days: "))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
remaining_days = remaining_days % 7
print("{} years {} weeks {} days".format(years, weeks, remaining_days))



# Create a program that takes a sentence as input and counts the number of words in it 
s = "Hello how are you "
l = s.split()
print(f"The total word count is {len(l)}")


## Create a program that takes a year as input and checks if it is a leap year or not)
year = int(input("Enter year "))
def checkLeapYear(year):
    if ((year % 4 == 0 and year % 100 != 0)or (year % 400 == 0)):
        print(year,"is leap year")
    else:
        print(year,"is not a leap year")

checkLeapYear(year)


# Implement a program that swaps the values of two variables
def swap_values(a, b):
    temp = a
    a = b
    b = temp
    return a, b
x = 5
y = 10
print(swap_values(x,y))


# Given a list of numbers, find the sum and average
def SumAndAvg(numbers):
    list_sum = sum(numbers)
    avg = list_sum / len(numbers)
    return list_sum, avg
numbers = [1, 2, 3, 4, 5]
print(SumAndAvg(numbers))


################################# Print Prime Number 1 to 50  ######################################
def PrimeNumbers(n):
    for num in range(n):
        if num>1:
            for i in range(2,num):
                if (num%i==0):
                    break
            else:
                print(num)
n=50                                 # output - 2 3 5 7 11 13 17 19
PrimeNumbers(n)


## Write a program to check if a number is prime.
a = 100
#for num in range(a):
if a>1:
    for i in range(2,a):
        if(a%i==0):
            print(a,"is not prime number")
            break
    else:
        print(a,"is prime number")


### Create a program that generates the Fibonacci sequence up to a given number of terms 
def fibonacci_sequence(n):
    if n<=0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)

n=19
for i in range(n):
    print(fibonacci_sequence(i),end=" ")


## Given a list of names, print all names starting with the letter 'A'
names = ['Adam', 'Bob', 'Charlie', 'David', 'Eve','amir']
for name in names:
    if name[0].lower() == 'a':
        print(name,end=" ")


### Implement a program that prints the multiplication table of a given number 
def multiplyTable():
    num = int(input('Enter a number to get its multiplication table :'))
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

multiplyTable()
       

### Write a program that calculates the factorial of a given number
def calculateFactorial(number):
    if number<=1:
        return 1
    else:
        return number*calculateFactorial(number-1)

print("The factorial of5 is",calculateFactorial(5))


### Given a list of words, count the number of words with more than five characters 
def word_length(words):
    counter = 0
    for word in words:
        if len(word) > 5:
            counter += 1
    return counter
print(word_length(['apple', 'banana', 'cherry']))


### Create a function to find the square of each element in a given list 
def squared_elements(lst):
    lst_squared = []
    for x in lst:
        lst_squared.append(x**2)
    return lst_squared
print(squared_elements([1, 2, 3,67]))


### Calculate the area of a triangle given its base and height using a function
def calculate_area(base,height):
    return ((base * height)/2)
print(calculate_area(5,9))


### Create a function that takes a list of strings and returns the list sorted alphabetically
def sort_strings(lst):
    lst.sort()
    return lst
print(sort_strings(['apple','cherry','banana']))

## Write a function that takes two lists and returns their intersection (common elements)
def find_intersection(list1,list2):
    common_elements = [value for value in list1 if value in list2]
    return common_elements
print(find_intersection([1,2,3,4],[3,4,5]))


### Write a function to count the number of vowels in a given string
def CountVowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count
print(CountVowel('hello world'))


## Given a list of words, concatenate them into a single string separated by spaces
def ConcatenateString(words_list):
    result=" ".join(words_list)
    return result
   
words_list = ["Hello", "World"]
print(ConcatenateString(words_list))


## Given a string, write a function to remove all vowels from it and return the modified string 
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    newString = ""
    for char in string:
        if char.lower() not in vowels:
            newString += char
    return newString
print(remove_vowels('hello world'))


## Write a Python program to find the length of the longest word in a sentence
def maxLengthWord(sentence):
    words = sentence.split()
    maxLen = len(words[0])
    for word in words:
        if len(word) > maxLen:
            maxLen = len(word)
    return maxLen
print(maxLengthWord('The quick brown fox jumps over the lazy dog.'))


## Create a function that takes a sentence as input and returns the sentence in reverse order
def reverseSentence(sentence):
    words = sentence.split()
    reversedWords = [word[::-1] for word in words]
    reversedSentence = ' '.join(reversedWords)
    return reversedSentence
print(reverseSentence('Hello World!'))


## Given a list of names, count the number of names that start with a vowel
def countVowelNames(names):
    vowels = ['A','E','I','O','U']
    count = 0
    for name in names:
        if name[0].upper() in vowels:
            count+=1
    return count
print(countVowelNames(['Alex','Bob','Charlie','David','owl']))


# Create a program that finds the common elements between two lists and stores them in a new list 
def common_element(list1,list2):
    output = []
    for values in list1:
        if values in list2:
            output.append(values)
    return output

print(common_element([1,2,3,6,8,9,0,4],[3,4,5,0,6,8]))


# Given a list of words, find the word with the maximum length and its length 
def MaxlengthWord(list1):
    words = list1.split()
    maxLen = len(list1[0])
    for word in words:
        if len(word)>maxLen:
            maxLen = len(word)
    return maxLen
list1 = 'Given a list of words find the word with the maximum length and its length'
print(MaxlengthWord(list1))
print(max(list1.split(),key=len))


# Given a list of names, remove all duplicate names and print the unique names
def RemoveDuplicateNames(names):
    seen = set()
    result = []
    for name in names:
        if name not in seen:
            result.append(name)
            seen.add(name)
    return result

fruits = ['mango','apple','pipeapple','banana','grape','orange','cherry','apricot','mango','apple','pipeapple']
print(RemoveDuplicateNames(fruits))


## Create a function that takes a list of strings and returns the list sorted by the length of the strings 
def sort_by_length(lst):
    return sorted(lst,key=len)
# Testing the function
fruits = ["apple", "pineapple", "banana", "kiwi"]
print(sort_by_length(fruits))


## Write a program that checks if a given list is sorted in ascending order 
def check_sorted(lst):
    return lst == sorted(lst)
# Testing the function
numbers = [4,1,3,5,7]
print(check_sorted(numbers))


## Implement a function that takes two lists and returns their union (all unique elements from both lists 
def union(list1,list2):
    return list(set(list1 + list2))
# Testing the function
a=[1,2,3,4,6,8]
b=[3,4,9,10,11]
print(union(a,b))


## Create a dictionary to store information about a person  (name, age, address)
personInfo = {'name':'naseem','age':34,'address':'sangam vihar'}
print(personInfo)

## Add a new key-value pair to an existing dictionary.
personInfo['gender'] = 'male'
print(personInfo)


## Add a new key-value pair more than one to an existing dictionary.
personInfo.update({'dist':34,'colleage':'mera h '})
print(personInfo)


## Create a set of unique numbers from a list of numbers
numList = [1,5,7,8,9,6,5,4]
uniqueNumSet = set(numList)
print(uniqueNumSet)


## Given two dictionaries, merge them into a single dictionary
d1 = {"a":1,"b":2} 
d2 = {"c":3,"d":4}
d1.update(d2)
print(d1)


## Write a program that finds the most frequent element in a list
myList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','i']
ch = {}
for i in myList:
    if i in ch:
        ch[i]+=1
    else:
        ch[i]=1
print(ch)
max_char = max(ch,key=ch.get)
print("Max_char is :",max_char)  # Max_char is : n


## Implement a function that removes a key-value pair from a dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
def removeKeyValuePair(dictionary, key):
    del dictionary[key]
    return dictionary
newDict = removeKeyValuePair(dict1,'a')
print(newDict)


## Create a program that checks if two sets have any elements in common
setA = {1,2,3,4,5}
setB = {4,5,6,7,8}
if setA & setB == {}:
    print("No Common Elements")
else:
    print("Common Elements are present")


## Given a list of dictionaries, find the dictionary with the highest value for a specific key
listOfDictionaries = [{'name':'John', 'age':20},{'name':'Jane', 'age':25}]
keyToFind = "age"
highestAgeDictionary = None
currentHighestAge = -1
for eachDictionary in listOfDictionaries:
    currentAge = eachDictionary[keyToFind]
    if currentAge > currentHighestAge:
        currentHighestAge = currentAge
        highestAgeDictionary = eachDictionary
print("The Dictionary with the Highest Age is :",highestAgeDictionary)


## Given two sets, find the union, intersection, and difference between them
def set_operations(setA,setB):
    unionAB = setA.union(setB)
    intersectionAB = setA.intersection(setB)
    differenceAB = setA.difference(setB)
    return unionAB,intersectionAB,differenceAB
setA = {1,3,5,7}
setB = {4,6,8,7}
print(f"Union of A and B is :{set_operations(setA,setB)[0]}")
print(f"Intersection of A and B is :{set_operations(setA,setB)[1]}")
print(f"Difference of A and B is :{set_operations(setA,setB)[2]}")


## Create a function that takes a list of dictionaries and sorts them based on a specified key
def sort_dicts(lst,key):
    return sorted(lst,key=lambda x:x[key])
data = [{'age':34,'name':'John'},{'age':56,'name':'Jimmy'},{'age':2,'name':'zoya'}]
print(sort_dicts(data,"age"))


## Write a program that finds the average value of all the elements in a list of dictionaries
def avg_list_of_dicts(lst):
    total = sum([i['value'] for i in lst])
    count = len(lst)
    return total/count
data = [{"value":1},{"value":2},{"value":3}]
print(avg_list_of_dicts(data))




##########################################################  File Handling Question Start ################################################################ 


## Write a program that reads a text file and prints its  contents.
f=open('/home/naseem/naseem_github/celery_redis/archive/filehandling.txt','r')
print(f.read())              ## read full file 
print(f.read(20))            ## read 20 charcter
print(f.readline())          ## read one line 
print(f.readlines())         ## read with slace \n if lines change hoti h to 
f.close()
def readFile(filename):
    try:
        f = open(filename,'r')
        lines = f.readlines()
        return lines
    except FileNotFoundError as e:
        print ("The file was not found")
filename = '/home/naseem/naseem_github/celery_redis/archive/filehandling.txt'
print(readFile(filename))



# # Create a new text file and write some content into it.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

def createNewFile(content, filename):
    with open(filename, 'w') as f:
        f.write(content)
        print ('Content written to the file successfully\n')
filename = '/home/naseem/naseem_github/celery_redis/archive/testfile.txt'
content = 'Python is an object oriented programming language Almost everything in Python is an object, with its properties and methods A Class is like an object constructor, or a  blueprint for creating objects.'
createNewFile(content, filename)



## Write a Python program to copy the contents of one text file into another
def copy_file():
    try:
        with open("/home/naseem/naseem_github/celery_redis/archive/testfile.txt", "r") as source:
            lines = source.readlines()
            with open("/home/naseem/naseem_github/celery_redis/archive/destination.txt","w+") as destination:
                for line in lines:
                    destination.write(line)
                    print("File copied successfully!")
    except IOError:
        print ("Unable to read or write files.")
copy_file()



## Implement a program that reads a text file and counts the number of words and lines in it.
filename = "/home/naseem/naseem_github/celery_redis/archive/filehandling.txt"
def count_words_and_lines(filename):
    with open(filename,"r") as f:
        content = f.read().split("\n")
        num_of_lines = len(content)
        word_count = sum([len(line.split()) for line in content])
        return num_of_lines,word_count
    
num_of_lines,word_count = count_words_and_lines(filename)
print("Number of Lines :",num_of_lines)
print("Word Count :",word_count)



## Create a function that takes a list of sentences and writes them to a new text file, each on a new line 
filename = "/home/naseem/naseem_github/celery_redis/archive/output.txt"

sentences = ["This is first sentence","Second Sentence","Third Sentence"]
def write_to_new_file(sentences,filename):
    with open(filename,'w+') as f:
        for sentence in sentences:
            f.write("%s\n"%sentence)

write_to_new_file(sentences,filename)



## Given a text file with a list of numbers, write a function that finds the sum of all numbers in the file 
def find_sum_of_numbers(filename):
    try:
        total = 0
        with open(filename, 'r') as fp:
            #print(fp.readlines())
            for line in fp:
                line = line.strip()
                if line.isdigit():
                    print(line)
                    num = int(line)
                    total += num
        return total
    except Exception as e:
        print("Error occurred", e)

result = find_sum_of_numbers(filename)
print(result)
