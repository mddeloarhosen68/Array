from array import *
#Ex:1
values = array('i',[24, 78, 1, 25, -8])

print(values.buffer_info())

#Ex:2
values = array('i',[24, 78, 1, 25, -8])

print(values.typecode)

#Ex:3
values = array('i',[24, 78, 1, 25, -8])
values.reverse()
print(values)

#Ex:4
values = array('i',[24, 78, 1, 25, -8])

for i in range(5):
    print(values[i])


#Ex:5
values = array('i',[24, 78, 1, 25, -8])

for i in range(len(values)):
    print(values[i])

#Ex:6
values = array('i',[24, 78, 1, 25, -8])

for e in values:
    print(e)

#Ex:7
values = array('u',['a','e','i','o','u'])

for e in values:
    print(e)

#Ex:8
values = array('i',[24, 78, 1, 25, 8])

newArr = array(values.typecode, (a for a in values))
for e in newArr:
    print(e)

#Ex:9
values = array('i',[24, 78, 1, 25, 8])

newArr = array(values.typecode, (a*a for a in values))
for e in newArr:
    print(e)



#Ex:10
values = array('i',[24, 78, 1, 25, 8])

newArr = array(values.typecode, (a*a for a in values))

i = 0
while i< len(newArr):
    print(newArr[i])
    i += 1

#Ex:11 without function
arr = array('i',[])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

values = int(input("Enter the value you search: "))

k = 0
for e in arr:
    if e == values:
        print(k)
        break

    k += 1


#Ex:12 With function
arr = array('i',[])
n = int(input("Enter the length of the array: "))

for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)

values = int(input("Enter the value you search: "))

print(arr.index(values))

