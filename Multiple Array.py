from numpy import *
#Array
arr = array([1, 2, 3, 4, 5, 6])
print(arr.dtype)
print(arr)

#Linspace
arr = linspace(0,15,20)
print(arr)

#Logspace
arr = logspace(1,40,5)
print('%.2f' % arr[4])


#Arange
arr = arange(1,15,2)
print(arr)


#Zeros
arr = zeros(5,int)
print(arr)

#Ones
arr = ones(5,int)
print(arr)