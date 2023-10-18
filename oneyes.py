# dict1 = {575:"Apple",876:"Mango",132:"Grapes",782:"Banana"}

# d = sorted(dict1.values())
# print("Sorted keys:", d)

################################## print average of number ################################################
n = int(input("Number of Elements to take average of: "))
element = int(input("Enter the element: "))
l = []
for i in range(1,n+1):
    l.append(element)
average = sum(l)/n
print("Average of the elements in list",round(average,2))

list1 = [8,7,2,5,3,1]
n = len(list1)
k=10
for i in range(n):
    for j in range(i+1, n):
        if (list1[i]+ list1[j]) == k:
            print(list1[i],"+",list1[j], "=" ,k)