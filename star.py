#                         ASCII Characters -         ASCII Codes -
#                           A-Z                        [65-90]
#                           a-z                        [97-122]
#                           0-9                        [48-57]


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

############################# Print this type of star ##########################
# 1
# 22
# 111
# 2222
# 11111

n=5
for i in range(n):
    for j in range(i+1):
        if (i%2==0):
            print("1",end="")
        else:
            print("2",end="")
    print()


########################### Print this type of pattern 
#      1
#     222
#    33333
#   4444444
#  111111111
#   2222222
#    33333
#     444
#      5

n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    for j in range(i+1):
        print(p,end="")
    p +=1
    print() 

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n):
        print(p,end="")
    p +=1
    print() 

############################################ Print this type of pattern ###############

#      1
#     222
#    33333
#   4444444
#  555555555
#   4444444
#    33333
#     222
#      1


n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
    for j in range(i+1):
        print(p,end="")
    p +=1
    print() 

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print(p,end="")
    for j in range(i,n):
        print(p,end="")
    p -=1
    print() 

############################################ Print this type of pattern ###############

# 1
# 12
# 123
# 1234
# 12345

n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p,end="")
        p+=1
    print()

############################################ Print this type of pattern ###############
# 5
# 54
# 543
# 5432
# 54321

n=5
for i in range(n):
    p=5
    for j in range(i+1):
        print(p,end="")
        p-=1
    print()


############################################ Print this type of pattern ###############
#  12345
#   1234
#    123
#     12
#      1

n=5
for i in range(n):
    p=1
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print(p,end="")
        p+=1
    print()

############################################ Print this type of pattern ###############
# 54321
#   5432
#    543
#     54
#      5

n=5
for i in range(n):
    p=5
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print(p,end="")
        p-=1
    print()

############################################ Print this type of pattern ###############

#      1
#     123
#    12345
#   1234567
#  123456789

n=5
for i in range(n):  
    p=1                  
    for j in range(i,n):                
        print(" ",end="")               
    for j in range(i):                 
        print(p,end="")   
        p+=1            
    for j in range(i+1):
        print(p,end="")
        p+=1
    p+=1
    print() 

############################################ Print this type of pattern ###############
# 54321
#  4321
#   321
#    21
#     1

n=5
k=5
for i in range(n):
    p=k
    for j in range(i):
        print(" ",end="")
    for j in range(i,n):
        print(p,end="")
        p-=1
    k-=1
    print()

############################################ Print this type of pattern ###############
#      1
#     121
#    12321
#   1234321
#  123454321

n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
        p+=1
    for j in range(i+1):
        print(p,end="")
        p-=1
    print()

############################################ Print this type of pattern ###############
# 1
# 23
# 456
# 78910

n=4
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end="")
        p+=1
    print()

############################################ Print this type of pattern ###############
# A
# AA
# AAA
# AAAA
# AAAAA

n=5
for i in range(n):
    for j in range(i+1):
        print(chr(65),end="")
    print()


############################################ Print this type of pattern ###############
# A
# BC
# DEF
# GHIJ
# KLMNO

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end="")
        p+=1
    print()

############################################ Print this type of pattern ###############
# A
# BB
# CCC
# DDDD
# EEEEE

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end="")
    p+=1
    print()

############################################ Print this type of pattern ###############

# E
# DD
# CCC
# BBBB
# AAAAA

n=5
p=69
for i in range(n):
    for j in range(i+1):
        print(chr(p),end="")
    p-=1
    print()

############################################ Print this type of pattern ###############
# A
# CC
# EEE
# GGGG
# IIIII

n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end="")
    p+=2
    print()

############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################# Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############


############################################ Print this type of pattern ###############