#!/usr/bin/env python
# coding: utf-8

# In[1]:


##list must be sorted
a=[1,1,1,1,1,13,13]
a.sort()
print(~a.index(13))


# In[2]:


###negative index of duplicates from front and back in sorted list
index=[]
for i in a:
    index.append(a.index(i))
#     index.append(a[::-1].index(i)) this will not work as .index method tells us the index from the front size
    index.append(~a[::-1].index(i))
    print(index)
    index.clear()


# In[3]:


#positive index
for i in a:
    index.append(a.index(i))
    index.append(~a[::-1].index(i)+len(a))
    print(index)
    index.clear()


# In[ ]:




