# Slicing Numpy arrays
import numpy as np
np1 = np.array([1,2,3,4,5,6,7,8,9])

# To return numbers 2,3,4,5, we use slicing.
print("====================")
print(np1[1:5]) # This will return the elements from index 1 to index 4 (index 5 is not included). Last index is never included when slicing.
print(np1[3:]) # This will return the elements from index 3 to the end of the array.

# Returning negative slices
print(np1[-3:-1]) # This will return elements from the third last index and does not include the last index, which is negative one.

print(np1[-3:]) # This will return the last three elements of the array.

# Printing with steps
print(np1[1:6:2]) # returns numbers 2 to 6 and skip counts by two.

# Steps on theh entire array
print(np1[::2]) # This will return every second element of the array.


# Slicing a 2D array

np2 = np.array(([1,2,3,4,5],
                [6,7,8,9,10]))

print(np2[1,2]) # The first number is the row (0 meaning the first row and 1 meaning the second row) and the second number is the column (0 meaning the first column and so on). With this statement, we are saying that we want to pull the item at index two of the second row/list.

print(np2[0:1, 1:3]) # This will return items from the index 1 to index two of the first row.

print(np2[1:2, 3:5]) # This will return items from the index 3 to index 4 of the second row.

print(np2[0:2, 1:4]) # This will return items from the index 1 to index 3 of both rows.

print("====================")

# Universal functions in Numpy - These operate on every element in an array.

print(" ")
print("====================")
np3 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
print(np3)

# Square root
print(np.sqrt(np3)) # This will return the square root of each element in the array.

# Absolute value
print(np.abs(np3)) # This will return the absolute value of each element in the array

# Exponents
print(np.exp(np3)) # This will return the exponential of each element in the array. This means it will calculate e^(-3) first, then e^(-2), then e^(-1) and so on. e is a mathematical constant that is approximately equal to 2.71828.

# Why do we call it finding the "exponential" of the array?
# Answer - While "an" exponential function can use any constant base, "e^x" is universally known as "the" exponential function—and used by default in NumPy's `np.exp()`—because its mathematically perfect rate of continuous growth makes it the standard for advanced math and programming.

# Min/Max
print(np.min(np3)) # This will return the minimum value in the array.
print(np.max(np3)) # This will return the maximum value in the array.

# Sign (positive or negative)
print(np.sign(np3)) # This will return the sign of each element in the array. Returns -1 for negative numbers, 0 for zero, and 1 for positive numbers.
print("====================")

# Trig functions (sin, cos, log, tan, etc etc)
# Basically ALL these things do is finding the sin/cos/tan/log/etc of each element. Returns "nan" if the domain of the function is not defined for that element. For example, tan(0) is defined, but tan(90) is not defined. So if you try to find the tan of 90, it will return "nan" (not a number).

# Copy vs view
# copy makes a copy of an array: both are completely separated arrays
# View not only creates a copy of an array but ensures that both will always be the same/intertwined. If the second array is changed, the first will also be changed, and vice versa.
print("====================")

np4 = np.array([1,2,3,4,5])
np5 = np4.copy() # This creates a copy of the array np4 and assigns it to np5. np4 and np5 are now completely separate arrays.
np4[0] = 100 # This changes the first element of np4 to 100. np5 is not affected because it is a copy of np4 and is completely separate.
print(np4)
print(np5)

np6 = np4.view()
np4[0] = 200 # This changes the first element of np4 to 200. np6 is also affected because it is a view of np4 and is intertwined with it.
print(np6) # This will print the array np6, which is now [200, 2, 3, 4, 5] because it is a view of np4 and is intertwined with it.
print(np4)
print("====================")

# Shaping and Reshaping numpy arrays

print("=====================")
np7 = np.array([1,2,3,4,5,6,7,8,9,10,12,13,14,15])
# call the shape
print(np7.shape) # returns the shape of an array as (14,) which means it is a 1D array with 14 elements.

np8 = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np8.shape) # returns the shape of an array as (2,5) which means it is a 2D array with 2 rows and 5 columns.

# Returns in this format for virtually everything.

# Reshaping
np9 = np7.reshape(2,7) # This reshapes the array np7 into a 2D array with 2 rows and 7 columns. The total number of elements must remain the same (14 in this case).
print(np9)
print(np9.shape) # returns the shape as usual

np10 = np7.reshape(7,2) # This reshapes the array np7 into a 2D array with 7 rows and 2 columns. The total number of elements must remain the same (14 in this case).

# How to flatten a numpy array to 1D
np11 = np7.flatten() # This flattens the array np10 into a 1D array. The total number of elements must remain the same (14 in this case).\

# OR
np11 = np7.reshape(-1) # Flattens the array into a 1D array. The -1 tells python to calculate the number of rows automatically based on the total number of elements.