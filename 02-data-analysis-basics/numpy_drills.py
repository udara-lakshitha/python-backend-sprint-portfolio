import numpy as np

# The core difference: Speed and Vectorization
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

# This is slow in python (using a loop)
list_times_two = [x * 2 for x in my_list]

# That is FAST in numpy (a single C level operation)
array_times_two = my_array * 2

print(f"Original NumPy array: {my_array}")
print(f"Array * 2 (Vectorized): {array_times_two}")

# Create an array of 10 zeros
zero = np.zeros(10)

# Create a (3 x 3) matrix of ones
ones_matrix = np.ones((3, 3))

# Create an array of numbers from 0 to 9
sequence = np.arange(10)

print(f"Shape of matrix: {ones_matrix.shape}")
print(f"Data type of sequence: {sequence.dtype}")

# Find all numbers greater than 5
greater_than_5_mask = sequence > 5 # This creates a boolean array [F, F, F, F, F, F, T, T, T, T]

# Use mask for select only True elements
result = sequence[greater_than_5_mask]
print(f"Numbers in sequence > 5: {result}")

# One line solution
print(f"Even numbers in sequence: {sequence[sequence % 2 == 0]}")


