import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print("Original Array: ")
# print(arr)
# print(arr[1:3])
# print(arr[:3])
# print(arr[2:])

array1 = np.array([(1,2,3)])
array2 = np.array([(4,5,6)])

vertical_stack = np.vstack((array1, array2))
print("Vertical Stack: ")
print(vertical_stack)

horizontal_stack = np.hstack((array1, array2))
print("Horizontal Stack: ",horizontal_stack)

result=np.concatenate((array1, array2), axis=0)
print(result)