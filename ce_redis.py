
################################################## Celery Concept  ###############################################


Programming Languages: Python (Proficient)
Asynchronous Task Processing: Celery 
Celery is a task queue based on asynchronous message passing. It can be used as a background task processor for your application in which you dump your tasks to
execute in the background or at any given moment. It can be configured to execute your tasks synchronously or asynchronously

Task Scheduling: Celery Beat = to scheduled task as a particular time based like you want send a message after two days 



Install Celery: First, you need to install the Celery library. You can do this using pip:

pip install celery 

Create a Celery Application: creating a Python file, such as celery.py, and configuring your Celery app there.

from celery import Celery

app = Celery(
    'your_app_name',
    broker='redis://localhost:6379/0',  # Use your preferred message broker
    backend='db+sqlite:///results.sqlite',  # Use your preferred result backend
)

# Additional configuration settings can be added here

@app.task
def my_background_task(arg1, arg2):
    # Task logic here
    result = arg1 + arg2
    return result
Run the Celery Worker: Start a Celery worker to process tasks. In the same directory as your celery.py, run:

celery -A celeryapp:app worker --loglevel=info


Schedule the Task with Celery Beat: You can schedule tasks by configuring Celery Beat

{
    "my-scheduled-task": {
        "task": "your_module.my_background_task",
        "schedule": crontab(minute=0, hour=0),  # This example runs the task daily at midnight
        "args": (3, 5)  # Arguments for the task
    }
}
Start Celery Beat: Run the Celery Beat scheduler using the following command:

celery -A celeryapp:app beat --loglevel=info



################################### if-elif-else Statement #########################################

if  = A check condition is used to decide whether a certain statement or a block of statement will be executed:
    
if <conditional expression >:
   statement
   [statements]
elif <conditional expression>
    statement
   [statements]

else:
   statement
   [statements]


# Buzz Numbers = which numbers divisible by 7 or end with 7 :
n = int(input("Enter a number:"))
if(n%7==0 or n % 10==7):
    print ("Buzz Number")
else:
    print ("Not a buzz number")


################################### for loop Statement ##################################################
for loop = Used for iterating over a sequence (list,string,tuple etc.)
    
for variable in sequence:    
    statements
else:           # is optinal 
    statements


################################### range function Statement #########################################

range([start,] stop [,step])
start = [defalut 0],step = [default 1]
1.Works only with integers values
2.Arguments can be postitive or negative 
3.Step values must not be Zero

# iterate string with index (x)
s = "code"
for x in range(len(s)):
    print(s[x])

# iterate through python for 
s = "code"
for x in s:
    print(x)


################################### Break Statement #########################################
break =  used to exit the loop when condition meets

for i in range(10):
    print(i)
    if (i==4):
        break


################################### Continue Statement #########################################
continue = used to skip current iteration and move on to next one

for i in range(5):
    if (i == 2):
        continue
    print(i)
################################### While Statement #########################################
while = Used to iterate over a block of code as long as the test expression is true 

<initialization>
while check_expression :
    <body of while>
    <counter changes>
else:
    <optional else clause>

################################### Convert to while loop #########################################
for i in range(25,500,40):
    print(i)

# convert it into while loop
i = 25
while i <= 500:
    print(i)
    i += 40

# Question 2........

for i range(10):
    for j in range(i):
        print("$",end="")
    print()

# convert it into while loop 
i=0
while i<=10:
    for j in range(i):
        print("*",end="")
    print()
    i+=1

i=0
while i<=10:
    j=0
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1