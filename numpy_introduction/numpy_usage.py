import numpy as np

_0d_array = np.array(43)
print("Zero dimensional array: ", _0d_array)
print(_0d_array.ndim)

_1d_array = np.array([1, 2, 3, 4, 5])
print("One dimensional array: ", _1d_array)
print(_1d_array.ndim)
print(type(_1d_array))
print("First element: ", _1d_array[1])

_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Two dimensional array: ", _2d_array)
print(_2d_array.ndim)
print("Second element of first array: ", _2d_array[0, 1])

_3d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Three dimensional array: ", _3d_array)
print(_3d_array.ndim)
print("Third element of Second matrices 2nd array: ", _3d_array[1, 1, 2])

example_array = np.array([1, 2, 3, 4, 5, 4, 6, 4, 7, 8, 4])
target = np.where(example_array == 4)
print(target)


