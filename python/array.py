import numpy as np
import array

# arr = np.array([1, 2, 3])
twod_array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# for x in range(2 ):
print(twod_array)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr5 = arr1.reshape(3, 3, -1)
# print(arr1[1:5:2])
print(arr1)
# print(twod_array[1][1:2])
print(twod_array[0: , 2, 1])

arr2 = array.array("i", [1, 2, 3])
print(arr2[1])

print(arr5)
