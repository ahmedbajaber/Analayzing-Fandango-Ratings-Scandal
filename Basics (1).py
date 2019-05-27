#!/usr/bin/env python
# coding: utf-8

# #Analysing whether Fandango movie ratings are inflated 
# 
# In 2015, Walt Hickey presented evidence to show that the movie rating website 'Fandango' was inflating their users movie ratings.
# He claimed that Fandango's system did this by rounding up all users scores i.e. a movie rating of 3.1 would be listed as 4. 
# Fandango claimed that this was just a bug. So I will look at more recent Fandango data to see whether the ratings are still being inflated.
# 

# In[2]:


import pandas as pd
pd.options.display.max_columns = 90

after = pd.read_csv('movie_ratings_16_17.csv')
previous = pd.read_csv('fandango_score_comparison.csv')



# In[3]:


print(after.head())


# In[4]:


fan_previous = previous[['FILM','Fandango_Stars','Fandango_Ratingvalue','Fandango_votes','Fandango_Difference']]


# Isolating data we need from dataset previous to Hickey's analysis.

# In[5]:


fan_after = after[['movie','year','fandango']]


# Isolating data needed from data after analysis.

# Aim is to determine whether there has been any change in the Fandango rating system after Hickeys analysis. Do note that Fandango issued a statement claiming that it was a bug and that they were going to fix it.
# 

# In[6]:


fan_after.sample(10, random_state = 1)


# Taking a random sample of 10 movies to see if they were popular enough to warrant 30 reviews(since Hickey used 30 reviews as a benchmark for popular movies)
# Checked online and found that 90% of our sample met the criteria

# In[7]:


print(fan_previous[fan_previous['Fandango_votes']<30])


# Checking whether second database has any movies with less than 30 views.

# In[8]:


fan_previous['year'] = fan_previous['FILM'].str[-5:-1]
fan_previous.head()


# In[9]:


fan_2015 = fan_previous[fan_previous['year']=='2015']
fan_2015.head()


# In[10]:


fan_2016 = fan_after[fan_after['year'] == 2016]
fan_2016['year'].value_counts()


# Making sure values in both databases are exclusively from the year before Hickey's analysis and the year directly after Hickey's analysis.

# In[21]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
fig = plt.figure(  figsize = (6,6))
fan_2015['Fandango_Stars'].plot.kde(label = 2015, legend= True)
fan_2016['fandango'].plot.kde(label = 2016, legend =True, c ='red')
plt.legend()
plt.xlabel('Stars')
plt.xlim(0,5)
plt.title('Distributions for Fandango Ratings between 2015 & 2016')
plt.show()



# Distribution shows that movie ratings from fandango are usually High to Very High (4 or 5 stars).
# The left shift from 2015 to 2016 is interesting due to our  analysis. It shows a shift in ratings for popular movies before and after Hickey's analysis. It is a left shift which means that movie ratings went down between the 2 years.

# In[23]:


fan_2015['Fandango_Stars'].value_counts().sort_index()


# In[24]:


fan_2016['fandango'].value_counts().sort_index()


# After comparing frequency distributions, we can see that there is a significant difference between the number of popular movies in 2015 and 2016. So it doesn't make sense to compare using absolute frequencies. So it would be better to compare relative frequencies using percentages.

# In[27]:


fan_2015['Fandango_Stars'].value_counts(normalize = True).sort_index() * 100


# In[28]:


fan_2016['fandango'].value_counts(normalize = True).sort_index() * 100


# Comparing the 2 relative frequency tables, we can see that there is a significant drop in higher ratings of popular movies. In 2015, almost 7% of popular movies got a perfect score of 5 whilst in 2016, less than 1% could achieve that score. Furthermore, there is a huge difference between movies that got a 4.5 rating. On the other end of the scale, we can also see that some movies recieved a score of 2.5in 2016 where that score was non-existent in 2015 for popular movies. 
# 

# In[ ]:





# 
# In conclusion, my analysis has brought to light that there is a difference between Fandangos ratings for popular movies in 2015 and 2016. In fact, it showed that there is a decrease in popoular movie ratings between the 2 years since movie ratings were lower in 2016. 
# 
# Chances are that the ratings system was fixed after Hickey's analysis found it to be biased. But I can't be completely sure of that, because it could be that movies in 2016 were generally viewed as worse movies than those in 2015. 






