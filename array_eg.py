#print an array by taking the input from the user and find the index value of the element in an array

from array import *
arr=array('i',[])
arr_length=int(input("enter the length of the array: "))
for i in range(arr_length):
    x=int(input("enter a number:"))
    arr.append(x)

print(arr)

find_index=int(input("enter a element in an array: "))
k=0
for e in arr:
    if e==find_index:
        print("the index value is",k)
    k+=1
