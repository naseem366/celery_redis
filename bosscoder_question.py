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


### Implement a program that finds the largest number in the list 
lst = [2,4,1,55,6,9]
max_val = lst[0]
for val in lst:
    if val > max_val:  
        max_val = val
print ("The maximum value is :", max_val)


## Create a program that takes a year as input and checks if it is a leap year or not)
year = int(input("Enter year "))
def checkLeapYear(year):
    if ((year % 4 == 0 and year % 100 != 0)or (year % 400 == 0)):
        print(year,"is leap year")
    else:
        print(year,"is not a leap year")

checkLeapYear(year)


