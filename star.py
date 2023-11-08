         
            ################################ Print All Types of Star(*) #############################################

##################################### Print normal * ###################

n = 5
for i in range(n):
    print("*",end="")      # output *****

################################## Print star with space between two stars with i and j  ##################

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

n=5
for i in range(n):                      
    for j in range(n):
        print("*",end=" ")
    print()

#################################### Print increment star ######################

# *
# **
# ***
# ****
# *****
# ******

n=6
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

############################ Print decrement star ###################
# ******
# *****
# ****
# ***
# **
# *
n=6
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()

############################# Print Right Sided Tringle of star #####################
#       *
#      **
#     ***
#    ****
#   *****
#  ******
n=6
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()


################### Print Left Sided Tringle of star #############################

# ******
#   *****
#    ****
#     ***
#      **
#       *

n=6
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print()

 ###################### Hill Pattern ############################ 1.decreasing space,2.Increasing star,3.Increasing star

#      *
#     ***
#    *****
#   *******
#  *********

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print() 


###################### Reverse Hill Pattern ##################### 1.Increasing space,2.Decreasing star,3.decreasing star

#  *********
#   *******
#    *****
#     ***
#      *

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print() 


###################### Diamond Pattern ##################### 

#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      *

n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print() 

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print() 


################################## Pyramid Pattern ##################### 

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

################################## Reverse Pyramid Pattern ##################### 

# * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()

############################### Print All Types of Numbers #############################################

########################## Increamenting The rows(1 to 55555)  #######################
# 1
# 22
# 333
# 4444
# 55555
n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    p+=1
    print()

################## Decreament Number rows(11111 to 5)
# 11111
# 2222
# 333
# 44
# 5

n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(p,end="")
    p+=1
    print()

########################## Increamenting The rows(5 to 11111)  #######################
# 5
# 44
# 333
# 2222
# 11111

n=5
p=5
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    p-=1
    print()

########################## Decreamenting The rows(55555 to 1)  #######################
# 55555
# 4444
# 333
# 22
# 1

n=5
p=5
for i in range(n):
    for j in range(i,n):
        print(p,end="")
    p-=1
    print()


###################### Hill Pattern With Numbers ##################### 
n=5
p=1
for i in range(n):                      #      1
    for j in range(i,n):                #     222
        print(" ",end="")               #    33333
    for j in range(i):                  #   4444444
        print(p,end="")                 #  555555555  
    for j in range(i+1):
        print(p,end="")
    p+=1
    print() 

###################### Reverse Hill Pattern With Numbers ##################### 
#  111111111
#   2222222
#    33333
#     444
#      5

n=5
p=1
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n):
        print(p,end="")
    p+=1
    print() 


######################## Pattern increament by 2 #####################
# 0
# 22
# 444
# 6666
# 88888

n=5
p=0
for i in range(n):                               
    for j in range(i+1):
        print(p,end="")
    p=p+2
    print()