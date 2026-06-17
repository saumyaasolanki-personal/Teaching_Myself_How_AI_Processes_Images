# Notes:
# Numpy is a special type of array which deals with matrices (array is a list consisting of the same datatype)
# Python lists allow multiple data types in one list, unlike other programming languages (but it's very slow and not cost efficient for machine learning)
# data type of numpy array - ndarray = n-dimensional array

import numpy as np
np1 = np.array([1, 2, 3, 4, 5]) # 1 dimensional array
np2 = np.array([2,5,1,7,3])

np1.shape # tells the number of items in an array
print(np1)
print(np1.shape)

np2 = np.arange(10) # This creates an array from 1 to 9
print(np2)

# How to create steps (skip counting) in numpy -
np3 = np.arange(0, 10, 2) # This creates an array from 1 to 9 with a step of 2. Last number is never included in the array
print(np3)


np4 = np.zeros(10)
print(np4) # This creates an array of 10 zeros

# multidimensional 0 arrays
np5 = np.zeros((3, 4)) # This creates a 3x4 array of zeros. The first number is the number of rows, the second number is the number of columns
print(np5)

# Full arrays - their sole purpose is to create arrays of a specific size and fill them with ONE specific value
np6 = np.full((4), 7) # This creates a list of 4 sevens
print(np6)

# Multidimensional full arrays
np7 = np.full((3, 4), 9) # This creates a 3x4 array of nines
print(np7)

# How to convert python lists to numpy arrays
list1 = [1, 2, 3, 4, 5]
np8 = np.array(list1) # This converts the python list to a numpy array
print(np8)

# What actually happens when you convert a list to a numpy array?
# When you convert a Python list to a numpy array, numpy creates a new array object that contains the same elements as the original list. However, unlike Python lists, numpy arrays are homogeneous, meaning all elements must be of the same data type. If the original list contains mixed data types, numpy will upcast the elements to a common data type that can accommodate all values. This conversion allows for more efficient storage and faster computations compared to standard Python lists.

list2 = [1, 2, 3, 4, 5, "hello"]
np9 = np.array(list2) # This converts the python list to a numpy array.
print(np9) # This will print the array with all elements as strings because of the presence of the string "hello" in the list. Numpy upcasts all elements to a common data type (in this case, string) to accommodate all values in the array.
# It won't print them all as ints because there is a string present that you can't convert to an int. Numpy will upcast all elements to a common data type (in this case, string) to accommodate all values in the array. Upcasting = process of converting a data type into a more general data type to avoid data loss.