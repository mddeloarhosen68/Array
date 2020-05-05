from array import *
#Quiz 1
#without function

x = array('i',[1,2,3,4,5])
y = array('i',[])
n = int(input('enter Index no:'))
for i in range(len(x)):
  if i == n:
    continue
  y.append(x[i])
x = y
print(x)

# With function

arr = array('i', [1, 2, 3, 4, 5])
print("Delete the value at index number 2")
arr.pop(1)
print(arr)

# Quiz 2
arr = array('i', [2, 4, 56, 23, 46])
k = len(arr) - 1
while k > -1:
    print(arr[k])
    k -= 1



