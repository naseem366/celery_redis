# dict1 = {575:"Apple",876:"Mango",132:"Grapes",782:"Banana"}

# d = sorted(dict1.values())
# print("Sorted keys:", d)

######################################## Find occurence of each character in string #################################

s = 'wwwwwfffrrraaerwrwraarrrraaeeerrrr'
d = {}
for ch in s:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print('{} occures {} times '.format(k,v))


# ################################# Find occurence of vowel present in given string ######################################

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