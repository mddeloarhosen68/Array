from numpy import *
#Ex:1
arr = array([1, 2, 3, 4, 5])
arr = arr + 5

print(arr)


#Ex:2
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])

arr3 = arr1 + arr2
print(arr3)

#Ex:3
arr1 = array([6, 1, 9, 3, 2])

print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
print(unique(arr1))

#Ex:4
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])


print(concatenate([arr1,arr2]))

#Ex:5
#Copying an Array
arr1 = array([1, 2, 3, 4, 5])
#arr2 = arr1.view()   #shallow copy
arr2 = arr1.copy()   #Deep copy
arr1[1] = 7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))