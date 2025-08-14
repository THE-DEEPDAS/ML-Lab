#!/usr/bin/env python
# coding: utf-8

# ## Practice Exercise 2

# In this assignment, you will try to find some interesting insights into a few movies released between 1916 and 2016, using Python. You will have to download a movie dataset, write Python code to explore the data, gain insights into the movies, actors, directors, and collections, and submit the code.

# #### Some tips before starting the assignment
# 
# 1. Identify the task to be performed correctly, and only then proceed to write the required code. Don’t perform any incorrect analysis or look for information that isn’t required for the assignment.
# 2. In some cases, the variable names have already been assigned, and you just need to write code against them. In other cases, the names to be given are mentioned in the instructions. We strongly advise you to use the mentioned names only.
# 3. Always keep inspecting your data frame after you have performed a particular set of operations.
# 4. There are some checkpoints given in the IPython notebook provided. They're just useful pieces of information you can use to check if the result you have obtained after performing a particular task is correct or not.
# 5. Note that you will be asked to refer to documentation for solving some of the questions. That is done on purpose for you to learn new commands and also how to use the documentation.

# In[ ]:


# Import the numpy and pandas packages

import numpy as np
import pandas as pd


# ### Task 1: Reading and Inspection
# 
# **Subtask 1.1: Import and read**
# 
# Import and read the movie database. Store it in a variable called `movies`.

# In[ ]:


# Write your code for importing the csv file here
movies = 
movies


# **Subtask 1.2: Inspect the dataframe**
# 
# Inspect the dataframe's columns, shapes, variable types etc.

# In[ ]:


# Write your code for inspection here


# #### <font color='red'>Question 1: How many rows and columns are present in the dataframe? </font>
# -  <font color='red'>(3821, 26)</font>
# -  <font color='red'>(3879, 28)</font>
# -  <font color='red'>(3853, 28)</font>
# -  <font color='red'>(3866, 26)</font>

# #### <font color='red'>Question 2: How many columns have null values present in them? Try writing a code for this instead of counting them manually.</font>
# 
# -  <font color='red'>3</font>
# -  <font color='red'>6</font>
# -  <font color='red'>9</font>
# -  <font color='red'>12</font>

# ### Task 2: Cleaning the Data
# 
# **Subtask 2.1: Drop unecessary columns**
# 
# For this assignment, you will mostly be analyzing the movies with respect to the ratings, gross collection, popularity of movies, etc. So many of the columns in this dataframe are not required. So it is advised to drop the following columns.
# -  color
# -  director_facebook_likes
# -  actor_1_facebook_likes
# -  actor_2_facebook_likes
# -  actor_3_facebook_likes
# -  actor_2_name
# -  cast_total_facebook_likes
# -  actor_3_name
# -  duration
# -  facenumber_in_poster
# -  content_rating
# -  country
# -  movie_imdb_link
# -  aspect_ratio
# -  plot_keywords

# In[ ]:


# Check the 'drop' function in the Pandas library - dataframe.drop(list_of_unnecessary_columns, axis = )
# Write your code for dropping the columns here. It is advised to keep inspecting the dataframe after each set of operations


# #### <font color='red'>Question 3: What is the count of columns in the new dataframe? </font>
# -  <font color='red'>10</font>
# -  <font color='red'>13</font>
# -  <font color='red'>15</font>
# -  <font color='red'>17</font>

# **Subtask 2.2: Inspect Null values**
# 
# As you have seen above, there are null values in multiple columns of the dataframe 'movies'. Find out the percentage of null values in each column of the dataframe 'movies'. 

# In[ ]:


# Write you code here


# #### <font color='red'>Question 4: Which column has the highest percentage of null values? </font>
# -  <font color='red'>language</font>
# -  <font color='red'>genres</font>
# -  <font color='red'>num_critic_for_reviews</font>
# -  <font color='red'>imdb_score</font>

# **Subtask 2.3: Fill NaN values**
# 
# You might notice that the `language` column has some NaN values. Here, on inspection, you will see that it is safe to replace all the missing values with `'English'`.

# In[ ]:


# Write your code for filling the NaN values in the 'language' column here


# #### <font color='red'>Question 5: What is the count of movies made in English language after replacing the NaN values with English? </font>
# -  <font color='red'>3670</font>
# -  <font color='red'>3674</font>
# -  <font color='red'>3668</font>
# -  <font color='red'>3672</font>

# ### Task 3: Data Analysis
# 
# **Subtask 3.1: Change the unit of columns**
# 
# Convert the unit of the `budget` and `gross` columns from `$` to `million $`.

# In[ ]:


# Write your code for unit conversion here


# **Subtask 3.2: Find the movies with highest profit**
# 
#    1. Create a new column called `profit` which contains the difference of the two columns: `gross` and `budget`.
#    2. Sort the dataframe using the `profit` column as reference. (Find which command can be used here to sort entries from the documentation)
#    3. Extract the top ten profiting movies in descending order and store them in a new dataframe - `top10`

# In[ ]:


# Write your code for creating the profit column here


# In[ ]:


# Write your code for sorting the dataframe here


# In[ ]:


top10 = # Write your code to get the top 10 profiting movies here


# **Checkpoint:** You might spot two movies directed by `James Cameron` in the list.

# #### <font color='red'>Question 6: Which movie is ranked 5th from the top in the list obtained? </font>
# -  <font color='red'>E.T. the Extra-Terrestrial</font>
# -  <font color='red'>The Avengers</font>
# -  <font color='red'>The Dark Knight</font>
# -  <font color='red'>Titanic</font>

# **Subtask 3.3: Find IMDb Top 250**
# 
# Create a new dataframe `IMDb_Top_250` and store the top 250 movies with the highest IMDb Rating (corresponding to the column: `imdb_score`). Also make sure that for all of these movies, the `num_voted_users` is greater than 25,000. 
# 
# Also add a `Rank` column containing the values 1 to 250 indicating the ranks of the corresponding films.

# In[ ]:


# Write your code for extracting the top 250 movies as per the IMDb score here. Make sure that you store it in a new dataframe 
# and name that dataframe as 'IMDb_Top_250'


# #### <font color='red'>Question 7: Suppose movies are divided into 5 buckets based on the IMDb ratings: </font>
# -  <font color='red'>7.5 to 8</font>
# -  <font color='red'>8 to 8.5</font>
# -  <font color='red'>8.5 to 9</font>
# -  <font color='red'>9 to 9.5</font>
# -  <font color='red'>9.5 to 10</font>
# 
# <font color = 'red'> Which bucket holds the maximum number of movies from *IMDb_Top_250*? </font>

# **Subtask 3.4: Find the critic-favorite and audience-favorite actors**
# 
#    1. Create three new dataframes namely, `Meryl_Streep`, `Leo_Caprio`, and `Brad_Pitt` which contain the movies in which the actors: 'Meryl Streep', 'Leonardo DiCaprio', and 'Brad Pitt' are the lead actors. Use only the `actor_1_name` column for extraction. Also, make sure that you use the names 'Meryl Streep', 'Leonardo DiCaprio', and 'Brad Pitt' for the said extraction.
#    2. Append the rows of all these dataframes and store them in a new dataframe named `Combined`.
#    3. Group the combined dataframe using the `actor_1_name` column.
#    4. Find the mean of the `num_critic_for_reviews` and `num_user_for_review` and identify the actors which have the highest mean.

# In[ ]:


# Write your code for creating three new dataframes here
Meryl_Streep = # Include all movies in which Meryl_Streep is the lead


# In[ ]:


Leo_Caprio = # Include all movies in which Leo_Caprio is the lead


# In[ ]:


Brad_Pitt = # Include all movies in which Brad_Pitt is the lead


# In[ ]:


# Write your code for combining the three dataframes here
Combined = 


# In[ ]:


# Write your code for grouping the combined dataframe here


# In[ ]:


# Write the code for finding the mean of critic reviews and audience reviews here


# #### <font color='red'>Question 8: Which actor is highest rated among the three actors according to the user reviews? </font>
# -  <font color='red'>Meryl Streep</font>
# -  <font color='red'>Leonardo DiCaprio</font>
# -  <font color='red'>Brad Pitt</font>

# #### <font color='red'>Question 9: Which actor is highest rated among the three actors according to the critics?</font>
# -  <font color='red'>Meryl Streep</font>
# -  <font color='red'>Leonardo DiCaprio</font>
# -  <font color='red'>Brad Pitt</font>

# In[ ]:




