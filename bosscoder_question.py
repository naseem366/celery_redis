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

