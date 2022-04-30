#!/usr/bin/env python
# coding: utf-8

# In[7]:


mylist=[]
message=''
while True:
    num=input('enter anumber or write exit:')
    if num=='exit':
        break
    else:
        mylist.append(int(num))
    min=mylist[0]
print(mylist)

for i in range(1,len(mylist)):
    if min>mylist[i]:
        message='not organized!'
        print(message)
        break
    else:
        min=mylist[i]
if message=='':
    print('organized')


# In[ ]:


2

