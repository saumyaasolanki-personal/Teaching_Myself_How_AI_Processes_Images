# Had to create a new document because my old one was getting very long and confusing.

# Iterating through Numpy arrays
# Iterating is when you go through each element in an array. Useful when you want to perform an operation on every element.

import numpy as np

# 1-d array
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
for x in np1:
    print(x)

np2 = np.copy(np1)
np2 = np2.reshape(2,5)

for x in np2:
    print(x) # will print each row
    for y in x:
        print(y) # will print the individual items in each array

print("====================")
print("====================")

np3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

#for x in np3:
    #print(x) prints both 2D arrays
#    for y in x: # prints each 1D array in the 2D arrays
#        for z in y:
#            print(z) # prints each individual item in the 1D arrays
            
# Too many loops

# So we use np.nditer(), which is a multi-dimensional iterator object to iterate through every element in the array.

for x in np.nditer(np3):
    print(x) # prints every single element

print("====================")

# Sorting numpy arrays
# What is sorting? Sorting is when you arrange the elements in an array in a specific order (ascending or descending).

np4 = np.array([4,5,1,6,8,3])
print(np4)
print(np.sort(np4)) # Sorts from lowest to highest (ascending order). Does not change the original array.

# Works for alphabetical sorting as well
np5 = np.array(["Hermione Granger", "Ron Weasley", "Harry Potter", "Draco Malfoy"])
print(np5)
print(np.sort(np5)) # Sorts alphabetically. Does not change the original array.

# Works for Booleans as well
np6 = np.array([True, False, True, False])
print(np6)
print(np.sort(np6)) # Sorts from False to True. Does not change the original array. False comes first because the binary value of false is 0 and true is 1.