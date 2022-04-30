#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
n=int(input('enter a number:'))
mylist = []

while len(mylist)<n  :
    rand=random.randint(0,n)
    if rand not in mylist:
        mylist.append(rand)
print(mylist)



# In[ ]:




