#!/usr/bin/env python
# coding: utf-8

# <h2 style = "color : Brown"> Creating NumPy Arrays </h2 >
# 
# 

#  The following ways are commonly used when you know the size of the array beforehand:
# * ```np.ones()```: Create array of 1s
# * ```np.zeros()```: Create array of 0s
# * ```np.random.random()```: Create array of random numbers
# * ```np.arange()```: Create array with increments of a fixed step size
# * ```np.linspace()```: Create array of fixed length

# In[1]:


import numpy as np


# ##### Tip: Use help to see the syntax when required

# In[2]:


help(np.ones)


# ##### Creating a 1 D array of ones

# In[3]:


arr = np.ones(5)
arr


# ##### Notice that, by default, numpy creates data type = float64
# 
# 

# In[4]:


arr.dtype


# ##### Can provide dtype explicitly using dtype
# 

# In[5]:


arr = np.ones(5, dtype=int)
arr


# In[6]:


arr.dtype


# ##### Creating a 5  x 3 array of ones
# 

# In[7]:


np.ones((5,3))


# ##### Creating array of zeros

# In[8]:


np.zeros(5)


# In[9]:


# convert the type into integer.
np.zeros(5, dtype=int)


# In[12]:


# Create a list of integers range between 1 to 5.
list(range(1,5))


# In[13]:


np.arange(3)


# In[14]:


np.arange(3.0)


# ##### Notice that 3 is included, 35 is not, as in standard python lists
# 
# From 3 to 35 with a step of 2

# In[20]:


np.arange(3,35,2)


# ##### Array of random numbers 
# 

# In[21]:


np.random.randint(2, size=10)


# In[24]:


np.random.randint(3,5, size=10)


# ##### 2D Array of random numbers 
# 

# In[25]:


np.random.random([3,4])


# ###### Sometimes, you know the length of the array, not the step size
# 
# Array of length 20 between 1 and 10

# In[27]:


np.linspace(1,10,20)


# <h2 style = "color : Sky blue"> Exercises </h2>

# 
# 
# Apart from the methods mentioned above, there are a few more NumPy functions that you can use to create special NumPy arrays:
# 
# -  `np.full()`: Create a constant array of any number ‘n’
# -  `np.tile()`: Create a new array by repeating an existing array for a particular number of times
# -  `np.eye()`: Create an identity matrix of any dimension
# -  `np.random.randint()`: Create a random array of integers within a particular range

# In[ ]:




