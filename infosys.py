
### 4. regular expression for email validation
import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
# Define a function for
# for validating an Email
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
        



#### 6.convert list to pandas dataframe
import pandas as pd 
# List1 
lst = [['apple', 'red', 11], ['grape', 'green', 22], ['orange', 'orange', 33], ['mango', 'yellow', 44]] 
df = pd.DataFrame(lst, columns =['Fruits', 'Color', 'Value']) 
print(df) 


import pandas as pd 
# list of name, degree, score 
n = ["apple", "grape", "orange", "mango"] 
col = ["red", "green", "orange", "yellow"] 
val = [11, 22, 33, 44] 
# dictionary of lists 
dict = {'fruit': n, 'color': col, 'value': val}  
df = pd.DataFrame(dict) 
print(df) 


## program to reverse dictionary key to value and value to key
def reverse_dictionary(dic):
    reversed_dic = {v: k for k, v in dic.items()}
    return reversed_dic
my_dict = {"a": 1, "b": 2, "c": 3}
print(reverse_dictionary(my_dict))




#### 3. What are decorators
Decorator is a design pattern that allows you to modify the behavior of existing code (classes or functions) without changing its structure.




### 5. How to define private and public variables
In Python, there is no explicit way of defining private or protected members like in other programming languages such as C++ or Java. However, we can



