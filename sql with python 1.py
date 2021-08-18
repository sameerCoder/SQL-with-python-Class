#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# SQL query to create a Table.

CREATE TABLE IF NOT EXISTS USERTABLE (STUDENTID INTEGER, STUDENTNAME TEXT, STUDENTADDRESS TEXT)


# In[ ]:


# INSERT DATA INTO TABLE.
INSERT  INTO USERTABLE VALUES(10,'JAMES','CALIFORNIA')
INSERT INTO USERTABLE VALUES(11,'RONIT','PARIS')


# In[ ]:


# SECOND WAY OF INSERTING INTO TABLE.
INSERT INTO USERTABLE (STUDENTID,STUDENTNAME, STUDENTADDRESS) VALUES (12,'ROHIT','INDIA')


# In[ ]:


# THIRD WAY OF INSERTING INTO TABLE.
INSERT INTO USERTABLE (STUDENTID,STUDENTNAME,STUDENTADDRESS) VALUES(13,'ROY','PARIS'),(14,'TONY','CANADA'),(15,'PAY','MICHIGIN')


# In[6]:


##############################################################


# In[7]:


# REAL EXAMPLE ##########


# In[23]:


# SAMPLE1.DB  IS DATABASE.
# TABLENAME1 IS TABLE INSIDE SAMPLE1.DB DATABASE.
import sqlite3

with sqlite3.connect("sample1.db") as conn:
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS TABLENAME1 (STUDENTID INTEGER, STUDENTNAME TEXT)")
    cursor.execute("INSERT INTO TABLENAME1 VALUES(100,'JAMES')")
    conn.commit()
   


# In[20]:


pwd


# In[ ]:


#NOW CREATE ANOHTER EMPLOYEE TABLE INSIDE SAME SAMPLE1.DB DATABASE.


# In[24]:


#ONLY CREATING EMPLOYEETABLE WITH NO RECORD.

import sqlite3

with sqlite3.connect("sample1.db") as conn2:
    cursor=conn2.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEETABLE (EMPLOYEID INTEGER, EMPLOYENAME TEXT)")
    


# In[27]:



import sqlite3

with sqlite3.connect("sample1.db") as conn2:
    cursor=conn2.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEETABLE (EMPLOYEID INTEGER, EMPLOYENAME TEXT)")
    cursor.execute("INSERT INTO EMPLOYEETABLE VALUES(201,'EMPLOYEE1_JAMES')")
    cursor.execute("INSERT INTO EMPLOYEETABLE VALUES(202,'EMPLOYEE2_RONY')")
    conn.commit()


# In[28]:


###################
# NOrmal sql queries
CREATE TABLE IF NOT EXISTS EMPLOYEETABLE (EMPLOYEID INTEGER, EMPLOYENAME TEXT) # for creating table

# inserting record into tables
INSERT INTO EMPLOYEETABLE VALUES(201,'EMPLOYEE1_JAMES')


# In[ ]:





# In[ ]:




