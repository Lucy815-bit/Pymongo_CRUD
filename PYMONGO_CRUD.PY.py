#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install pymongo


# In[61]:


import pymongo


# In[62]:


from pymongo import MongoClient


# In[43]:


#Creating a Database

#To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.

#MongoDB will create the database if it does not exist, and make a connection to it.


# In[44]:


Client = MongoClient("mongodb://localhost:27017/")


# In[63]:


cluster = ("mongodb+srv://<YOURUSERNAME>:<YOURPASSWORD>.@cluster0.huiho.mongodb.net/<>?retryWrites=true&w=majority")
cluster = MongoClient(cluster)


# In[64]:


db = cluster["students"]


# In[65]:


collection = db["names"]


# In[26]:


#Insert Into Collection

#To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.

#The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert.


# In[66]:


names = {"Fname":"Lucy" , "Lname":"Wagoro","Mjini":"Kisumu","Nchi":"Kenya"}
collection.insert_one(names)
#print(collection.inserted_id) 


# In[ ]:


#Insert Multiple Documents

#To insert multiple documents into a collection in MongoDB, we use the insert_many() method.

#The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:


# In[68]:


#insert many documents

names = [
  { "_id":1,"Fname": "Robert","Lname":"Maranga", "Mjini":"USA","Nchi":"USA"},
  { "_id":2,"Fname": "Ciru","Lname":"Wachiru", "Mjini":"USA","Nchi":"USA"},
  { "_id":3,"Fname": "Migot","Lname":"Ndede", "Mjini":"USA","Nchi":"USA"},
  { "_id":4,"Fname": "Jacky","Lname":"Atieno", "Mjini":"USA","Nchi":"USA"},
  { "_id":5,"Fname": "Clare","Lname":"Akoth", "Mjini":"USA","Nchi":"USA"},
  { "_id":6,"Fname": "Clare","Lname":"Akoth", "Mjini":"USA","Nchi":"USA"},
]

collection.insert_many(names)


# In[28]:


#FIND ONE

#To select data from a collection in MongoDB, we can use the find_one() method.

#The find_one() method returns the first occurrence in the selection.
#Find the first document in the collection:


# In[69]:



x = collection.find_one()

print(x) 


# In[ ]:


#FIND ALL

#To select data from a table in MongoDB, we can also use the find() method.

#The find() method returns all occurrences in the selection.

#The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.
#No parameters in the find() method gives you the same result as SELECT * in MySQL.


# In[70]:


for x in collection.find():
 print(x) 


# In[ ]:


#FILTER THE RESULT

#When finding documents in a collection, you can filter the result by using a query object.

#The first argument of the find() method is a query object, and is used to limit the search.
#Example

#Find document(s) with the MJINI "USA":


# In[71]:


myquery = { "Mjini": "USA" }

mydoc = collection.find(myquery)

for x in mydoc:
  print(x) 


# In[ ]:


#Limit the Result

#To limit the result in MongoDB, we use the limit() method.

#The limit() method takes one parameter, a number defining how many documents to return.

#Consider you have a "collection" collection:


# In[72]:


x = collection.find().limit(2)
print(x)


# In[74]:


#UPDATE THE DATABASE
collection.update({"Fname": "Lucy"}, {"$set":{"Fname": "Monicah"}})


# In[76]:


#Delete a document
collection.delete_one({"Fname":"Lucy"})# ccheck database


# In[ ]:





# In[ ]:


#Delete Collection

#You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
#Example

#Delete the "collection" collection:


# In[77]:


collection.drop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




