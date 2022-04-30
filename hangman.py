#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
joon=10
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

computer_word=random.choice(words)
user_word=len(computer_word)*'-'

while joon>0 and computer_word!=user_word:
    print(user_word)
    letter=input('please enter a letter')
    letter=letter.lower()
    if letter in computer_word:
        for i in range(len(computer_word)):
            if letter==computer_word[i]:
                #user_word[i]=letter
                temp= list(user_word)
                
                temp[i]=letter
                user_word= "".join(temp)
    if letter not in computer_word:
        joon-=1
      
if computer_word==user_word:
    print(user_word)
    print('you win')
if joon==0:
    print('you fail')


# In[ ]:




