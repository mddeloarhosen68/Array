from array import *
#Ex:1
a = array('i', [1, 2, 3])
for i in range(len(a)):
    b = array('i', [4, 5, 6])
    print(a[i]+b[i],end='')

#Ex:2     with function
a = ([1,3,5,2])
a.sort()
print(a[-1])
print(a)


#Ex:3     without function
list1 = []
num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

print("Largest element is:", max(list1))
