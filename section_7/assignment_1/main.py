import numpy as np

# Part A: Array creation and properties

# 1: A 1D array of all odd numbers from 1 to 19
arr1d = np.arange(1, 20, 2)
print(f"1D: {arr1d}")
print("--------------------------------------------------")

# 2: A 4X4 identity matrix
identity_matrix = np.eye(4)
print(f"identity matrix: {identity_matrix}")
print("--------------------------------------------------")


# 3: A 3X5 array filled entirely with the value 7
arr3x5 = np.full((3, 5), 7)
print(f"3x5: {arr3x5}")
print("--------------------------------------------------")

# 4: An array of 8 evenly spaced values between 0 to 1
evenly_spaced = np.linspace(0, 1, 8)
print(f"evenly_spaced: {evenly_spaced}")
print("--------------------------------------------------")

# 5: A 2D array of shape (3, 4) filled with zeros
arr2d = np.full((3,4), 0)
print(f"2d_array: {arr2d}")
print("--------------------------------------------------")

# Part B:
# 1: Create an array [1.7, 2.9, 3.1, 4.8, 5.5] and print its default dtype
arr3 = np.array([1.7, 2.9, 3.1, 4.8, 5.5])
print(f"arr3: {arr3.dtype}") # prints float64
print("--------------------------------------------------")

# 2: Convert it to int32 and print the result — what happened to the decimals?
converted_arr3 = arr3.astype('int32')
print(f"converted_arr3: {converted_arr3.dtype}")
print("--------------------------------------------------")

# 3: Create two identical arrays of 10,000 elements — one as int64, one as int32. Print the memory usage (.nbytes) of both and calculate how much memory you saved
arr_int64 = np.array(list(range(10000)), dtype='int64')
arr_int32 = np.array(list(range(10000)), dtype='int32')
mem_int64 = arr_int64.nbytes
mem_int32 = arr_int32.nbytes
print(f"memory int32: {mem_int32}")
print(f"memory int64: {mem_int64}")
print(f"memory_saved: {mem_int64 - mem_int32}") # saved 40000 bytes
print("--------------------------------------------------")

# 4: Create a complex number array [2+3j, 4+5j, 6+7j] and print its dtype
complex_num_array = np.array([2+3j, 4+5j, 6+7j])
print(f"dtype of complex_array: {complex_num_array.dtype}") # prints complex128 dtype
print("--------------------------------------------------")

# Part C:
# You've received a flat array of 12 sensor readings:
readings = np.arange(1, 13)

# 1: Reshape it into a (3, 4) matrix representing 3 days × 4 time slots
reshaped_readings = readings.reshape(3, 4)
print(f"reshaped readings: {reshaped_readings}")
print("--------------------------------------------------")

# 2: Extract only the readings from day 2 (second row)
day2 = reshaped_readings[1, :] # 1 row, : signifies all columns
print(f"day2: {day2}")
print("--------------------------------------------------")

# 3: Extract the readings from the last 2 time slots of all days (last 2 columns)
last2 = reshaped_readings[:, -2:]
print(f"last2: {last2}")
print("--------------------------------------------------")

# 4: Flatten it back to 1D
flattened = reshaped_readings.flatten()
print(f"flattened to 1d: {flattened}")
print("--------------------------------------------------")

# 5: Slice every alternate reading from the flat array
alternate_readings = flattened[::2]
print(f"alternate_readings: {alternate_readings}")
print("--------------------------------------------------")

# Part D:
# This is the most important part of this assignment.
arr_d = np.array([10, 20, 30, 40, 50, 60])
# sliced = arr[2:5]
# sliced[0] = 999

# 1: Print arr after the above code — explain in a comment why it changed
'''
    because sliced only view the arr[2:5] and not copy it, and now because we changed the sliced[0] to 999 that will reflect into the arr itself
    so to fix or prevent this we can use .copy() method and by this way we can manipulate the sliced dataset without worrying about changing arr by mistake
'''
# 2: Now fix it so that modifying sliced does not affect arr
sliced = arr_d[2:5].copy()
sliced[0] = 999
print("--------------------------------------------------")

# 3: Prove it worked by modifying the fixed slice and printing arr again
print(f"sliced: {sliced}")
print(f"arr: {arr_d}")
print("--------------------------------------------------")

# Part E:
# You have daily temperature readings (in °C):
temps = np.array([22, 35, 18, 41, 29, 15, 38, 27, 44, 12])

# 1: Use fancy indexing to extract temperatures at positions [1, 3, 6, 8]
index = [1, 3, 6,8]
positions = temps[index]
print(f"indexed_positions: {positions}")
print("--------------------------------------------------")

# 2: Use boolean masking to find all temperatures above 30°C
masks = temps > 30
print(f"all temp greater than 30: {temps[masks]}")
print("--------------------------------------------------")

# 3: Use boolean masking to find temperatures that are between 20°C and 35°C (inclusive)
masks_v2 = (temps <= 35) & (temps >= 20)
print(f"temp between 20-35: {temps[masks_v2]}")
print("--------------------------------------------------")

# 4: Replace all temperatures above 40°C with exactly 40 (cap them) — do this in one line using boolean masking
cap = temps > 40
temps[cap] = 40
print(f"replaced temp above 40 to 40: {temps}")