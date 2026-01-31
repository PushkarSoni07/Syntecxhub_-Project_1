# Learned NumPy fundamentals – array creation, indexing, and slicing.
import numpy as np
arr = np.array([10, 20, 30, 40, 50]) 
print (arr)         
print(arr[3])      
print(arr[1:4])    
print("\n")

# Performed mathematical, axis-wise, and statistical operations on datasets.

import numpy as np
data = np.array([[1,2,3],
                 [4,5,6]])
print(data + 2)
print(data * 3)
print(data.sum())    
print(data.mean())      
print(data.min()) 
print(data.max())
print(data.mean())   
print("\n")     

#Applied reshaping and broadcasting techniques for efficient computation.

import numpy as np
a = np.array([1,2,3,4,5,6])
reshaped = a.reshape(2,3)
print(reshaped)
print(reshaped + 10)  
print("\n") 

#Implemented save/load operations for NumPy arrays.

import numpy as np
np.save("data.npy", reshaped)
loaded = np.load("data.npy")
print(loaded)
print("\n") 

#Compared NumPy’s performance with standard Python lists.
import numpy as np
import time
lst = list(range(1000000))
arr = np.array(lst)
start = time.time()
[x*2 for x in lst]
print("List:", time.time() - start)
start = time.time()
arr * 2
print("NumPy:", time.time() - start)
