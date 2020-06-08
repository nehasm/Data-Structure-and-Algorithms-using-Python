'''
Python doesn’t have explicit array data structure.
It’s because we can do the same things with the List.
The list contains a collection of items and it supports add/update/delete/search operations.
That’s why there is not much use of a separate data structure in Python to support arrays.
An array contains items of the same type but Python list allows elements of different types. 
This is the only feature wise difference between an array and a list.
In Python you can use list for all the operation involve array.
However you can create array with programming tricks and also by using a module name array.
We will see how to generate array with programming tricks as well as using built in module array.
'''

#Array implementation using programming tricks
class Array(object):
    "This will create array of given size with all element equal to 0"
    def __init__(self,sizeofarray,arraytype = int):
        self.sizeofarray = len(list(map(arraytype,range(sizeofarray))))
        self.arrayitems = [arraytype(0)]*sizeofarray

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayitems])
    
    #search function to search element using giving input of keytosearch
    def search(self,keytosearch):
        for i in range(self.sizeofarray):
            if (self.arrayitems[i] == keytosearch):
                return i
        return -1
    
    #insert function to insert element using the given input of postion and keytoinsert
    def insert(self,keytoinsert,position):
        if (self.sizeofarray > position):
            for i in range(self.sizeofarray-2,position-1,-1):
                self.arrayitems[i+1]=self.arrayitems[i]
            self.arrayitems[position] = keytoinsert
        else:
            print("Array size is not sufficient1")
    
    #delete function to delete element using the given input of position and keytodelete  
    def delete(self,keytodelete,position):
        if (self.sizeofarray > position):
            for i in range(position,self.sizeofarray-1):
                self.arrayitems[i]=self.arrayitems[i+1]

#search operation
a=Array(10,int)
index=a.search(0)
print("Element found at",index)

#insert operation
a.insert(1,2)
a.insert(3,4)
print(a)

#delete operation
a.delete(1,2)
print(a)


#Array implementation using built in module array.
import array
arr = array.array('i',[1,2,3,4,5,6,7,8])

print("The new created array is:",end="")
for i in range(0,8):
    print(arr[i],end=" ")

arr.append(9)
print("\nArray after appending 9 into it: ",end="")
for i in range(0,9):
    print(arr[i],end=" ")

arr.insert(2,10)
print("\nArray after inserting 10 at second position: ",end="")
for i in range(0,10):
    print(arr[i],end=" ")

arr.remove(1)
print("\nArray after removing 1 it: ",end="")
for i in range(0,9):
    print(arr[i],end=" ")
