#!/usr/bin/env python
# coding: utf-8

# <h2 style = "color : Brown"> Operations on NumPy Arrays</h2>
# 
# The learning objectives of this section are:
# 
# * Manipulate arrays
#     * Reshape arrays
#     * Stack arrays
# * Perform operations on arrays
#     * Perform basic mathematical operations
#     * Apply built-in functions 
#     * Apply your own functions 
#     * Apply basic linear algebra operations 
# 

# In[12]:


import numpy as np


# <h4 style = "color : Sky blue"> Example - 1 (Arithmatric Operations)</h4>  
# 

# In[13]:


array1 = np.array([10,20,30,40,50])
array2 = np.arange(5)


# In[14]:


array1


# In[16]:


array2


# In[17]:


# Add array1 and array2.
array3 = array1 + array2


# In[18]:


array3


# <h4 style = "color : Sky blue"> Example - 2</h4>  

# In[20]:


array4 = np.array([1,2,3,4])


# In[21]:


array4 + array1


# In[22]:


print (array1.shape)


# In[23]:


print (array4.shape)


# <h4 style = "color : Sky blue"> Example - 3</h4>  

# In[24]:


array = np.linspace(1, 10, 5)
array


# In[25]:


array*2


# In[26]:


array**2


# <h4 style = "color : Sky blue"> Stacking Arrays</h4> 

# ####  ```np.hstack()``` and ```n.vstack()```
# 
# Stacking is done using the ```np.hstack()``` and ```np.vstack()``` methods. For horizontal stacking, the number of rows should be the same, while for vertical stacking, the number of columns should be the same.

# In[27]:


# Note that np.hstack(a, b) throws an error - you need to pass the arrays as a list
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

np.hstack((a,b))


# In[28]:


np.vstack((a,b))


# In[29]:


np.arange(12)


# In[30]:


np.arange(12).reshape(3,4)


# In[31]:


array1 = np.arange(12).reshape(3,4) #3x4
array2 = np.arange(20).reshape(5,4) #5x4


# In[33]:


print (array1, '\n', array2)


# In[34]:


np.vstack((array1,array2))


# <h4 style = "color : Sky blue"> Example - 4 (Numpy Built-in functions)</h4>  

# In[35]:


array1


# In[36]:


np.power(array1, 3)


# In[38]:


np.arange(9).reshape(3,3)


# In[39]:


x = np.array([-2,-1, 0, 1,2])
x


# In[40]:


abs(x)


# In[41]:


np.absolute(x)


# <h4 style = "color : Sky blue"> Example - 5 (Trignometric functions)</h4>  

# In[42]:


np.pi


# In[43]:


theta = np.linspace(0, np.pi, 5)


# In[44]:


theta


# In[45]:


np.sin(theta)


# In[46]:


np.cos(theta)


# In[47]:


np.tan(theta)


# <h4 style = "color : Sky blue"> Example - 6 (Exponential and logarithmic functions)</h4>  

# In[48]:


x = [1, 2, 3, 10]
x = np.array(x)


# In[49]:


np.exp(x) # e=2.718...


# In[50]:


# 2^1, 2^2, 2^3, 2^10
np.exp2(x)


# In[51]:


np.power(x,3)


# In[52]:


np.log(x)


# In[53]:


np.log2(x)


# In[54]:


np.log10(x)


# In[ ]:


np.log


# <h4 style = "color : Sky blue"> Example - 7</h4>  

# In[57]:


x = np.arange(5)
x


# In[59]:


y = x * 10
y


# In[58]:


y = np.empty(5)
y


# In[61]:


np.multiply(x, 12, out=y)


# In[62]:


y


# In[63]:


y = np.zeros(10)
y


# In[65]:


np.power(2, x, out=y[::2])


# In[66]:


y


# <h4 style = "color : Sky blue"> Example - 8 (Aggregates)</h4>  

# In[67]:


x = np.arange(1,6)
x


# In[69]:


sum(x)


# In[68]:


np.add.reduce(x)


# In[70]:


np.add.accumulate(x)


# In[72]:


np.multiply.accumulate(x)


# In[ ]:





# #### Apply Basic Linear Algebra Operations
# 
# NumPy provides the ```np.linalg``` package to apply common linear algebra operations, such as:
# * ```np.linalg.inv```: Inverse of a matrix
# * ```np.linalg.det```: Determinant of a matrix
# * ```np.linalg.eig```: Eigenvalues and eigenvectors of a matrix
#     
# Also, you can multiple matrices using ```np.dot(a, b)```. 
# 

# In[73]:


# np.linalg documentation
help(np.linalg)


# In[74]:


A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])


# In[75]:


A


# ##### Rank of a matrix

# In[76]:


np.linalg.matrix_rank(A)


# ##### Trace of matrix A

# In[77]:


np.trace(A)


# ##### Determinant of a matrix

# In[78]:


np.linalg.det(A)


# ##### Inverse of matrix A

# In[87]:


A


# In[79]:


np.linalg.inv(A)


# In[84]:


B = np.linalg.inv(A)


# In[85]:


np.matmul(A,B) #actual matrix multiplication


# In[86]:


A * B


# ##### Matrix A raised to power 3

# In[88]:


np.linalg.matrix_power(A,3) # matrix multiplication A A A


# In[ ]:




