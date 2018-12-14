#!/usr/bin/env python
# coding: utf-8

# In[32]:


n = 9
backward = 0
IsOdd=True

if n%2==0:
    IsOdd = False
    
if IsOdd==True:
    backward = round((n-1)/2)
    
forward = round(backward + 1)

for i in range(0, forward):
    if IsOdd == False:
        break
    for j in range(0, i+1): 
        # printing stars 
        print("* ",end="") 
    print("\r")
    
for i in range(backward,0,-1):
    if IsOdd == False:
        break
    for j in range(0, i): 
        # printing stars 
        print("* ",end="") 
    print("\r")

