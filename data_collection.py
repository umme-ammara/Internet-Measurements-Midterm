#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd 
import socket
#Read the IP addresses
df = pd.read_csv('top-alexa.csv')
domain = df['Domain Names']


# In[13]:


#print(domain)
notconvert = []
domainlist = []
iplist = []
#Covert to IP addresses
for i in range(len(domain)):
    d = domain[i]
    try: 
        ip = socket.gethostbyname(d)
        domain[i] = ip 
        domainlist.append(d)
        iplist.append(ip)
        #print(i,d,ip)
    except:
        #print(i,d)
        notconvert.append(i)
        
print(len(notconvert)) #29 domains that could not be converted -> discard these from the dataset

#for i in notconvert:
#    domain.drop(index=i,inplace=True)
    
#domain.reset_index(drop=True,inplace=True)
#print(domain)
    


# In[14]:


#Covert domain and ip lists to file output 
textfile = open("domains.txt", "w")
for d in domainlist:
    textfile.write(d + "\n")
textfile.close()

textfile2 = open("ip.txt","w")
for ip in iplist:
    textfile2.write(ip + "\n")
textfile2.close()


# In[21]:


#test = "yahoo.co.jp is Hosted on YAHOO IP Address: 183.79.250.123 (Tokyo, Japan) route-admin@mail.yahoo.co.jp +000000000"


# In[ ]:




