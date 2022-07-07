# Databricks notebook source


# COMMAND ----------

#Part 1
#keywords: and, or
#operators: ==, !=

# COMMAND ----------

#Part 2: Conditionals and loops. Python støtter ikke tradisjonell for-løkke
for food in breakfast:
    print (breakfast)
    
# print 0,1,2,3,4
range(0,5)






# COMMAND ----------

#Methods, Functions and Packages. Blokken etter "," skriver ut som feilmelding
assert "even" == result, f"Expected even, found {result}"

#Dokumentasjon i koden, på første linje i funksjonen
""""
Dette er dokumentasjon som synes hvis jeg bruker help() function
""""

#type hint (gives hint in the IDE if incorrect type is used)
def event_odd_int(num: int, event: str) -> str:
    

#PEP 8 - Stylde guide for Python Code

#kan bruke type(variable) for å sjekke type;

#default parameters, hvis parametre ikke spesifiseres. 
def event_odd_int(num: int, eventlabel:str ="even", oddLabel:str = "odd")

#named arguments. Useful if 3+ arguments, to ensure the right parameters are passed in the right order
print(evenOddInt(eventLabel="Even", oddLabel = "odd", num=3780))
       
#Arbritrary arguments. "*" indikerer at det er et variabelt antall input parametre
def sum(*args)

#function: operates only on the parameters passed
#method: operates on an object, e.g. foo.upper()




# COMMAND ----------

#Lesson 5: 
#empty list -> list = []
#accessing an item in a list -> list[i]
#Length of list -> len(list)
#Last item -> list[-1]
#Append -> list.append("oatmeal")
#Delete item -> del list[index]
#Remove item -> list.remove("oatmeal")
#Check if item is in list: if "oatmeal" in list
#Check if item is not in list: if "oatmeal" not in list
# min(list) (alphabetical order if non-numerical)
# max(list)
# range (start, stop, step). Can also do negative step

#List comprehension
caps_list = [item.capitalize() for item in breakfast_list if len(item) >=2]

#Dictionary:
breakfast_dict = {
    "eggs": 100,
    "apple": 100,
    "pancakes": 400,
    "waffles": 300,
}
# get value in dictionary: breakfast_dict["eggs"] or. breakfast_dict.get("eggs")
# check if key exist in dictionary: 
if "bacon" in breakfast_dict

#adding new key-value pair to dictionary
breakfast_dict["orange_juice"] = 100
#altering the value
breakfast_dict["orange_juice"] = 300
#deleting value
del breakfast_dict["orange_juice"]

# COMMAND ----------

Iterate over dictionary, use for in

# COMMAND ----------

for food in breakfast_dict
breakfast_dict = {"eggs": 160, "apple": 100, "pancakes": 400, "waffles": 300,}
print("Food          Calories")

for food in breakfast_dict:
  print(f"{food:13} {breakfast_dict[food]}")

# COMMAND ----------

Alternatively, you can unpack the key-value pairs while iterating over a dictionary using the items() method:


# COMMAND ----------

breakfast_dict = {"eggs": 160, "apple": 100, "pancakes": 400, "waffles": 300,}
print("Food          Calories")
for key_value in breakfast_dict.items():
  key = key_value[0]
  value = key_value[1]
  print(f"{key:13} {value}")

# COMMAND ----------

.items() returns a new data type called dict_items, which is a sub-type of tuple

# COMMAND ----------

#Unpacking a tuple
my_tuple = ("Smith", 39)
last_name, age = my_tuple

# COMMAND ----------

dict_

# COMMAND ----------

Constructor: __init__()

class Person:
    indention
    ...


# COMMAND ----------

#Pandas


# COMMAND ----------

# MAGIC %md
# MAGIC Test

# COMMAND ----------

import pandas as pd
data=("row one", "row two", "row three")
pd.DataFrame(data=data)

# COMMAND ----------

# MAGIC %md
# MAGIC Pandas Series is a single column of a Pandas DataFrame

# COMMAND ----------


