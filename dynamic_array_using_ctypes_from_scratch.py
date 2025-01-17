# Create list [D] 
# len [D]
# append [D]
# print [D]
# indexing 
# pop 
# clear
# find 
# insert
# delete
# remove


# Building Dynamic Array/ List in Python using library of c language having all functionalities list over

import ctypes    # library of c language used to create data types of c language

# Building dynamic list using array of c -> bcoz it is faster 

class My_List:
    def __init__(self):
        self.current_size = 1
        self.n = 0

        # Now create a c type array with size = self.size -> basically size of array with size 1 
        self.A = self.__make_array(self.current_size)

    # make a method which can output the length of list -> gives max items in the lis t 
    def __len__(self):
        return self.n
    

    def __str__(self):
        # [1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'
    

    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range' 
        
    def __delitem__(self,pos):
        # delete
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1


    def append(self,item):
        if self.n == self.current_size:
            # resize
            self.__resize(self.current_size*2)

        
        # append
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1 

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'
    
    def insert(self,pos,item):
        if self.n == self.current_size:
            self.__resize(self.current_size*2)
        

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            # delete
            self.__delitem__(pos)
        else:
            return pos



    def  __resize(self,new_capacity):
        # create a new array with a new capacity
        B = self.__make_array(new_capacity)
        self.current_size = new_capacity
        # copy the content of A to B

        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A 
        self.A = B


    def  __make_array(self,capacity):
        # creates a ctype array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()
    




    # Making the object of list to access the data and methods of it
L = My_List()

# Checking initially if empty or not
print(L)





# Inserting item at the end
L.append("Hello")
L.append(3.4)
L.append(True)
L.append(100)

# checking no. of items appended -> total length of list
print(len(L))


print(L)


# Checking functions if correctly working or not 

L.remove('Hello')
L.pop()
print(L.find(True))
L.clear()







# More Functionalities can be implemented further

# sort/min/max/sum
# extend
# negative indexing
# slicing
# merge
    