#coding:utf-8
import numpy as np

arr = np.random.randn(5)
arr2 = np.random.randn(8).shape(2,4)

# save arr array in a file
np.save('arr_save', arr)

# save arr2 array in a file
np.save('arr2_save', arr2)

# save arr and arr2 in the file
np.savez("save_both", arr=arr, arr2=arr2)

# load file
arr_f = np.load('arr_save.npy')
arr2_f = np.load('arr2_save.npy')
arr_both = np.load('save_both.npz')

# print the data in file
print(arr_f)
print(arr2_f)
print(arr_both['arr'])
print(arr_both['arr2'])
