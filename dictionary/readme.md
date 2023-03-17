
Dictionary data structure
=========================
collection of {key:value} pairs is called dictionary it is denoted by curly braces{}

dictionary is a mutable collection of many values and ----- key values are immutable 

dictionary data types
=======================
1) keys----- will returns to the list of the keys in dictonary.

   name={'age':24,'name':'siva,'mobile.no':9885367512}
   for i in name.keys():
       print(i)
      
 age
name
mobile.no

2) values ---- it will be returns to the list of the values in dictionary.
   
name={'age':24,'name':'siva','mobile.no':9885367512}
for i in name.values():
    print(i)

24
siva
9885367512

3) items ---- it will be return to the each itam in the dictionary.
  
name={'age':24,'name':'siva','mobile.no':9885367512}
for i in name.items():
    print(i)
('age', 24)
('name', 'siva')
('mobile.no', 9885367512)

4) get ---- get all item of the values is same 

     name={
    "name":'siva',
    'age':34,
    'value':89876,
    'place':'rct'
}
value=name.get('place')
print(value)
rct

5) change -- we can change the value of a specific item  by referring to its key name

value={
    'age':23,
    'name':'siva',
    'year':1900
}
value['year'] = 2023
print(value)
{'age': 23, 'name': 'siva', 'year': 2023}

6)update------In the dictonary added to the one item 


value={
    'age':23,
    'name':'siva',
    'year':1900
}

value.update({'color':'red'})
print(value)

{'age': 23, 'name': 'siva', 'year': 1900, 'color':'red'}


7) pop --- In dict we can remove the specific key name.

    value={
    'age':23,
    'name':'siva',
    'year':1900
}

value.pop('name')
print(value)

{'age': 23, 'year': 1900}


8)popitem------ In dict removes the last inserted item



value={
    'age':23,
    'name':'siva',
    'year':1900
}

value.popitem()
print(value)
{'age': 23, 'name': 'siva'}


9) del---In dict we can del the all keywords.

  value={
    'age':23,
    'name':'siva',
    'year':1900
}

del value
print(value)

10) clear---In dict we can clear the all keywords.

   
value={
    'age':23,
    'name':'siva',
    'year':1900
}

value.clear()
print(value)
{}

nasted Dictionaries:

myname = {
    
}



