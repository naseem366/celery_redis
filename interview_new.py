################## Convert Celsius to Fahrenheit ###################

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

################# Calculate simple interest ##################

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (years): "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)


################## Calculate area of rectangle ##################

length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area = length * width
print("Area of the rectangle:", area)


#################### Calculate area of circle ##################

import math
radius = float(input("Enter radius of the circle: "))
area = math.pi * radius ** 2
print("Area of the circle:", area)

############################################# Factorial of a number ##########################################

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)


########################################## Reverse a number ##################################################
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num //= 10
print("Reversed number:", reverse)

############################################## Fibonacci series ################################################

n_terms = int(input("Enter the number of terms: "))
a, b = 0, 1

for _ in range(n_terms):
    print(a, end=' ')
    a, b = b, a + b

############################################# Palindrome number #################################################

# A palindrome number is a number that remains the same when its digits are reversed.
# For example, 121 is a palindrome number because it reads the same forwards and backwards.

num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp //= 10
if num == reverse:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")


############################################# Armstrong Number ################################################# 

# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
# For example, 153 is an Armstrong number because it has 3 digits and \(1^3 + 5^3 + 3^3 = 153\). 

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


############################################ Perfect number #################################################
# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# For example, 6 is a perfect number because its proper divisors are 1, 2, and 3, and \(1 + 2 + 3 = 6\).

num = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")


############################################ Strong number #################################################
# A strong number is a number such that the sum of the factorials of its digits is
# equal to the number itself. For example, 145 is a strong number because \(1! + 4! + 5! = 145\).

n = int(input("Enter a number: "))
sum_of_factorials = 0
temp = n

while temp > 0:
    digit = temp % 10
    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i
    sum_of_factorials += factorial
    temp //= 10

if sum_of_factorials == n:
    print(n, "is a strong number")
else:
    print(n, "is not a strong number")


######################################## GCD of two numbers ########################################

# The GCD (Greatest Common Divisor) of two numbers is the largest positive
# integer that divides both numbers without leaving a remainder. e.g., the GCD of 12 and 18 is 6.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD of the two numbers is:", num1)


####################################### LCM of two numbers ########################################## 

# The LCM (Least Common Multiple) of two numbers is the smallest positive integer that is divisible by both numbers.
# For example, the LCM of 4 and 5 is 20.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = 1
a, b = num1, num2
while b != 0:
    a, b = b, a % b
lcm = (num1 * num2) // a
print("LCM of the two numbers is:", lcm)

######################################### Check Automorphic number #########################################

# An automorphic number is a number whose square ends with the same digits as the number itself
# For example, 5 is an automorphic number because \(5^2 = 25\) ends with 5.

n = int(input("Enter a number: "))
square = n ** 2
if str(square).endswith(str(n)):
    print(n, "is an automorphic number")
else:
    print(n, "is not an automorphic number")


######################################### Check Harshad number #########################################

# A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
# For example, 18 is a Harshad number because the sum of its digits is \(1 + 8 = 9\) and \(18\) is divisible by \(9\).

n = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(n))
if n % sum_of_digits == 0:
    print(n, "is a Harshad number")
else:
    print(n, "is not a Harshad number")


lst = [1,2,3,4,5,6]
rev = []
for i in lst:
    rev = [i]+rev

print(rev)


################################ explain logic #########################

# count how many time of each values appears 

# dictionary.get(key, default_value)
# If the key exists, return its value.
# If the key doesn't exist, return the default value
# d.get(2,0) returns 0 because 2 is not in the dictionary d
# d[2] = d.get(2, 0) + 1
# d[2] = 0 + 1

# for the first element 1 in the list, d.get(1, 0) returns 0 because 1 is not in the dictionary d
# Then we add 1 to it, so
# d[1] = d.get(1, 0) + 1
#      = 0 + 1
#      = 1
# d = {1: 1}

# d[2] = d.get(2, 0) + 1
#      = 0 + 1
# d = {1: 1, 2: 1}

# next time 2 is encountered, d.get(2, 0) returns 1 because 2 is already in the dictionary d
# d[2] = d.get(2, 0) + 1
#         = 1 + 1
#         = 2
# d = {1: 1, 2: 2}


# Equivalent code without get()
# for ch in l:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1


### Given a string s = "abcabcbb", find the length of the longest substring without duplicate characters

s = "abcabcbb"

max_len = 0

for i in range(len(s)):
    temp = ""

    for j in range(i, len(s)):
        if s[j] in temp:
            break

        temp += s[j]
        max_len = max(max_len, len(temp))

print(max_len)



def length_of_longest_substring(s: str) -> int:
    char_index = {}
    start = 0
    max_length = 0
    
    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Example
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3 (substring "abc")


##################### Most frequent element

lst = [1, 2, 3, 2, 4, 2, 3]
d = {}
max_count = 0
most_frequent = None
for ch in lst:
    d[ch] = d.get(ch,0)+1
print(d)
for key in d:
    if d[key] > max_count:
        max_count = d[key]
        most_frequent = key

print(most_frequent)


lst = [1, 2, 3, 2, 4, 5, 3, 6, 2]
count = {}
duplicates = []

for num in lst:
    count[num] = count.get(num, 0) + 1

for key, value in count.items():
    if value > 1:
        duplicates.append(key)



###################

student = {
    "name":"Naseem",
    "age":28,
    "grade":"A"
}
print(student)
student['city']='delhi'
lst1 = student.keys()
lst2 = student.values()

d = dict(zip(lst1,lst2))
print(d)  

##################### merge dictionaries


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1,**dict2}
print(merged)

##### 2nd method

dict1.update(dict2)
print(dict1)

################## invert a dictionary

d = {"a": 1, "b": 2, "c": 3}

invert = {}
for key in d:
    value = d[key]
    invert[value] = key

print(invert)
    


########## Group same values
d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

group = {}
for key in d:
    value = d[key]
    if value in group:
        group[value].append(key)    
    else:
        group[value] = [key]

print(group)
        
##  isinstance(x, list) checks if an element is a list before processing.
# isinstance(item, list) is used to check whether the current item is a list before deciding how to handle it. 
# If the item is a list, we can extend the existing list of keys; if it's not a list, we can create a new list with the current key.
# This ensures that we correctly group keys that have the same value in the original dictionary.


################################## Functions 

def factorial(n):
    if n == 0 or n == 1:           # Base case
        return 1
    return n * factorial(n - 1)    # Recursive case

n = 5
for i in range(n+1):
    print(factorial(i),end=' ')
    

def Fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
         return Fibo(n-1)+Fibo(n-2)
        
n = 10
for i in range(n):
    print(Fibo(i),end=' ')


nums = [1, 2, 3, 4]
result = map(lambda x: x * x, nums)
print(list(result))  # [1, 4, 9, 16]

nums = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, nums)
print(list(result))  # [2, 4, 6]





def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item,list):
            result.extend(flatten(item)) #### Recursively flatten nested list
        else:
            result.append(item)

    return result
    
lst = [1,2,[4,5],6,[7,8],9]
#lst = [[[1, 2]], 3]

print(flatten(lst))


def test(a = []):
    a.append(1)
    return a
    
print(test())
print(test())
print(test())
        

import copy

a = [1, [2, 3]]

a[1][1] = 99

b = copy.copy(a)
c = copy.deepcopy(a)

print(a)
print(b)
print(c)



#  gives all query for interview for 5 years of experience SQL interview queries
