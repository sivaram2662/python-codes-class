
String Data structure:
======================














24-01-23
=========
List data structure 
====================
list is collection of element /items  encloesd by [] square brackets.
                        (or)
group of individual objects as a single entity

list is insertion order of element is fixed.
==============================================
list = [10,20,30,40,50,60,70,80]
print(list)
[10, 20, 30, 40, 50, 60, 70, 80]

list allows duplicate elements also
===================================
seshu,narayana,pavan--------number of time is objects is allowed.

list elements can be homogeneous and heterogeneous element. are mutabule it will be change 
===========================================================
 Homogeneous element:   if list has same type of element then that is called homogeneous element 
=====================
                  list = [10,20,30,40,50,60]
                  print(list)
                [10, 20, 30, 40, 50, 60]
heterogeneous element:  if list hame different types of element then that is called heterogrneous element
======================
                  list = [20,40,2.4,False,6.8,76]
                  print(list)
                   [20, 40, 2.4, False, 6.8, 76]

list indexing:
==============       
                         Fordword indexing
                        0  1  2  3  4  5  6   7 8             [True =1]   false=0                                                                  
                  st = [10,20,30,40,50,60,70,80,90]            
                        -9 -8 -7 -6 -5 -4 -3 -2 -1
                         Backwerd indexing

Indexing means Fetching a specific elements by using its index number 
lst = [10,20,30,40,50,60,70,80,90]
lst[0]
10
lst[True]
20
lst[False]
10
lst[-True]
90
lst[-False]
10
lst[6]
70
lst[-3]
70
lst[6]
70
lst[-5]
50

list slicing:
=============
slicing means set of the element by using start-num and end-num
lst = [10,20,30,40,50,60,70,80,90]
lst[2:-3]
[30, 40, 50, 60]
lst[-20:8]
[10, 20, 30, 40, 50, 60, 70, 80]
lst[4:-4]
[50]
lst[3::4]
[40, 80]
lst[-5::2]
[50, 70, 90]
lst[-5::-2]
[50, 30, 10]


creation of objects :
====================
1)list 
     num="i am siva"
     ram=list(num)
      print(ram)
     ['i', ' ', 'a', 'm', ' ', 's', 'i', 'v', 'a']

2) range
    num=list(range(1,100))
    print(num)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

3)split 
      num="amazon web service training sysllbus"
      name=num.split()
      print(name)
      ['amazon', 'web', 'service', 'training', 'sysllbus']


IMP function :
==============
    1) len : number of elements present in the list 
        value=[2,4,56,'siva']
        print(len(value))
        4
    2) count : number of occurance of a specific character 
            siva=[2,4,56,76,45,56,4,5,6,78,99,76,4,2]
            print(siva.count(2))
             2 
            print(siva.count(56))
            2
            print(siva.count(99))
            1
    3) index : returns the index of first occurrence of the specified item.
        siva=[2,4,56,76,45,56,4,5,6,78,99,76,4,2]
          print(siva.index(2))
          0
         print(siva.index(56))
          2
        print(siva.index(45))
        4 

   4) min: in list it will be given the min value 
       ram=[3,4,5,7,6]
       min(ram)
       3

   5) max: in the list it will be given the max value 
        ram=[3,4,5,7,6]
        max(ram)
        7

   6) sum : in the list value is sum of them.
          ram=[3,4,5,7,6]
          sum(ram)
           25

   7)del : inside the list of the value is del
          ram=[3,4,5,7,6]
          del(ram)

   8)clear: We can use clear() function to remove all elements of List.
             b=[3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7]
             b.clear()        
           print(b)           
                []

manipulating elements:
======================
1) append : We can use append() function to add item at the end of the list.
      list=[2,45,67,34]
     list.append('siva')
     list.append('ram')
     list.append('gangi')
     print(list)
     [2, 45, 67, 34, 'siva', 'ram', 'gangi']

2) insert: insert item at specific index position 
      list=[2,45,67,34]
     list.insert(2,"sriram")
     list.insert(3,"sri")
     list.insert(5,346638)
      print(list)
[2, 45, 'sriram', 'sri', 67, 346638, 34, 'siva', 'ram', 'gangi']

3) extend : add all items of one list to another list 
    name=[3,4,5,6,7]
   list.extend(name)
   print(list)
  [2, 45, 'sriram', 'sri', 67, 346638, 34, 'siva', 'ram', 'gangi', 3, 4, 5, 6, 7]

4)remove: we can remove the specific item from the list 
    
list= [2, 45, 'sriram', 'sri', 67, 346638, 34, 'siva', 'ram', 'gangi', 3, 4, 5, 6, 7]
    list.remove('sri')      
    list.remove('gangi')
    list.remove(67)
    print(list)
    [45, 'sriram', 346638, 34, 'siva', 'ram', 3, 6, 7]

5) pop:it remove and return the  last element of the list 
     list=[45, 'sriram', 346638, 34, 'siva', 'ram', 3, 6, 7]
   list.pop()            
   7
   list.pop()         
   6
   list.pop()           
   3
  print(list)            
  [45, 'sriram', 346638, 34, 'siva', 'ram']

ordering element:
=================
1)reverse : reversr order in the list 
      list= [45, 'sriram', 346638, 34, 'siva', 'ram']
      list.reverse()          
      print(list)
    ['ram', 'siva', 34, 346638, 'sriram', 45]

2) sort: for numbers----default natural sorting order is Ascending Order
        for string -----default natural sorting order is Alphabetical Order
        list=[2,56,78,34,5,67,2,45]      
        list.sort()
        print(list)    
        [2, 2, 5, 34, 45, 56, 67, 78]
     list=['siva','anu','cat','pavan','bucker','name']            
     list.sort()
     print(list)            
    ['anu', 'bucker', 'cat', 'name', 'pavan', 'siva']

3) sort-reverse-order: in the list reverse order the true and false 
 list=['siva','anu','cat','pavan','bucker','name']            
     list.sort()
     print(list)            
    ['anu', 'bucker', 'cat', 'name', 'pavan', 'siva']
    list.sort(reverse=True)           
   print(list)           
   ['siva', 'pavan', 'name', 'cat', 'bucker', 'anu']
   list.sort(reverse=False)        
   print(list)         
   ['anu', 'bucker', 'cat', 'name', 'pavan', 'siva'] 

mathamatical operator :
=======================
1)concentation : We can use + to concatenate 2 lists into a single list
   a=[2,3,4,6,7,8,3]           
   b=[3,4,56,67,54]          
   print(a+b)         
   [2, 3, 4, 6, 7, 8, 3, 3, 4, 56, 67, 54]

2)repetition operator(*):We can use repetition operator * to repeat elements of list specified number of time
    a=[3,4,5,6,7]       
    b=a*4
   print(b)           
 [3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7]

membership operation : we check the member of the list or not by using membership operator 
======================
1) in operator and not in operator 

a=[40,50,30,20,45]           
print(456 in a)            
False
print(50 not in a)           
False
print(20 in a)           
True
print(30 in a)            
True
 





============================================================================================




25-01-23
============
 
Tuple Data structure :
=========================

collection of element is called tuple is enclosed by parenthesis()
                  (or)
group of individual objects as a single entity 


list is insertion order of element is fixed.
============================================
name=10,20,30,40,50,60,90            
print(name)          
(10, 20, 30, 40, 50, 60, 90)
print(type(name))           
<class 'tuple'>

duplicates : in the tuple duplicates elements are allow 
===========
sri ram ,narayana,book --------

list elements can be homogeneous and heterogeneous element. are immutable  it will be change 
===========================================================
 Homogeneous element:   if tuple has same type of element then that is called homogeneous element 
=====================
                   t= 10,20,30,40,50,60
                  print(t)
                (10, 20, 30, 40, 50, 60)
heterogeneous element:  if tuple hame different types of element then that is called heterogrneous element
======================
                  t = 20,40,2.4,False,6.8,76
                  print(t)
                   (20, 40, 2.4, False, 6.8, 76)


list indexing:
==============       
                         Fordword indexing
                        0  1  2  3  4  5  6   7 8             [True =1]   false=0                                                                  
                  t = (10,20,30,40,50,60,70,80,90)            
                        -9 -8 -7 -6 -5 -4 -3 -2 -1
                         Backwerd indexing

Indexing means Fetching a specific elements by using its index number 
t = (10,20,30,40,50,60,70,80,90)
print(t[-1])
            
90
print(t[True])
            
20
print([-3])
            
[-3]
print(t[False])
            
10
print(t[4])
            
50

list slicing:
=============
slicing means set of the element by using start-num and end-num
t = (10,20,30,40,50,60,70,80,90)
print(t[3:-1])
            
(40, 50, 60, 70, 80)
print(t[-2::4])
            
(80,)

print(t[3:5])
            
(40, 50)
print(t[4:6])
            
(50, 60)

creation of objects:
======================
1) t=()----------creation of empty tuple
               
print(type(t))
            
<class 'tuple'>


2) t=(40,)-----------creation of single valued tuple ,parenthesis are optional,should ends with comma
    t=10,20,30,40      
   print(t)
            
  (10, 20, 30, 40)
  print(type(t))
            
<class 'tuple'>
3)t=29,45,67,78----------creation of multi values tuples & parenthesis are optional
t=10,30,40,59,67
print(n)
(10, 30, 40, 59, 67)

4)tuple----------------
   t=10,30,40,59,67           
n=tuple(t)         
print(n)          
(10, 30, 40, 59, 67)

IMP function:
==============
1) len---- To return number of elements present in the tuple
   t=10,20,30,40,50
    print(len(t))
    5
        
2) count : number of occurance of a specific character 
            siva=(2,4,56,76,45,56,4,5,6,78,99,76,4,2)
            print(siva.count(2))
             2 
            print(siva.count(56))
            2
            print(siva.count(99))
            1
3) index : returns the index of first occurrence of the specified item.
        siva=(2,4,56,76,45,56,4,5,6,78,99,76,4,2)
          print(siva.index(2))
          0
         print(siva.index(56))
          2
        print(siva.index(45))
        4 
 4) min: in tuple it will be given the min value 
       ram=(3,4,5,7,6)
       min(ram)
       3

 5) max: in the tuple it will be given the max value 
        ram=(3,4,5,7,6)
        max(ram)
        7
 6) sum : in the tuple value is sum of them.
          ram=(3,4,5,7,6)
          sum(ram)
           25

7)del : inside the tuple of the value is del
          ram=(3,4,5,7,6)
          del(ram)

ordering elements:
===================
1) sorted -------To sort elements based on default natural sorting order
 
  name=(304,1,34,90,34,23,56,78)
            
t=sorted(name)
            
print(t)
            
[1, 23, 34, 34, 56, 78, 90, 304]

2) sorted-reverse--------- in the tuple of value is reverse order ue the True or flase
n=(40,40,50,68,38,2,1)

 n=sorted(p,reverse=True)
            
print(n)
            
[68, 50, 40, 40, 38, 2, 1]
n=sorted(p,reverse=False)
            
print(n)
            
[1, 2, 38, 40, 40, 50, 68]

mathamatical operators:
=======================

concatentation----- We can use + to concatenate 2 tuple into a single tuple
n=(2,4,56,67,45)
            
b=(45,56,67,78)
            
c=n+b
            
print(c)
            
(2, 4, 56, 67, 45, 45, 56, 67, 78)


multipulation ----:We can use repetition operator * to repeat elements of tuple specified number of time
a=(20,30,45,56)
            
v=a*3
            
print(v)
            
(20, 30, 45, 56, 20, 30, 45, 56, 20, 30, 45, 56)


membership operation : we check the member of the tuple or not by using membership operator 
======================
1) in operator and not in operator 

a=(40,50,30,20,45)          
print(456 in a)            
False
print(50 not in a)           
False
print(20 in a)           
True
print(30 in a)            
True
 

===========================================================================================================


Set data structure
==================
collection element is called set represented with {}--curly brackets 

duplicates--in set duplicates elements are not allowed
===========



list elements can be homogeneous and heterogeneous element. are mutabule it will be change 
===========================================================
 Homogeneous element:   if set has same type of element then that is called homogeneous element 
=====================
                  n = {10,20,30,40,50,60}
                  print(list)
                {50, 20, 40, 10, 60, 30}
heterogeneous element:  if set has different types of element then that is called heterogrneous element
======================
                  n = {20,40,2.4,False,6.8,76}
                  print(list)
                 {False, 2.4, 20, 6.8, 40, 76}

creation of objects:
====================
1) n={20,40,50,69}
    print(n)
    {40, 50, 20, 69}
print(type(n))           
<class 'set'>

2) set()--we can create set objected

     name=[34,56,76,56,45,34]
            
n=set(name)
            
print(n)
            
{56, 34, 76, 45}


IMP function:
=============
1) len--To return number of elements present in the set
      n={34,45,67,34,256,46,234}
            
    print(len(n))
            
     6
2)copy---it will clone the set
 n={34,45,67,34,256,46,234}
b=n.copy()      
print(b)
{256, 34, 67, 234, 45, 46}

3)del : inside the set of the value is del
          ram={3,4,5,7,6}
          del(ram)

4)clear: We can use clear() function to remove all elements of set.
             b={3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7}
             b.clear()        
           print(b)           
                {}

minpulating elements:
=====================
             
1) add--- we can add function to add item to the set 
   a={23,45,67,34}
            
a.add('siva')
            
print(a)
            
{34, 67, 45, 23, 'siva'}

2)remove ---we can use this function to remove specific item from the set

   name={23,45,67,87}
            
name.remove(45)
            
print(name)
            
{67, 87, 23}

3) discard ----- it remove the specific element of the set
name={23,45,67,87}
 name.discard(87)
print(name)            
{67, 23}

4) update -----we can update function to add multiple items to the set 

a={23,45,67,45}          
b.update(a)           
print(b)           
{67, 45, 23}


ordering elements :
===================
1)union--We can use this function to return all elements present in both sets
       a={2,3.4,5,67}        
b={1,5,7}      
a.union(b)   
{1, 2, 67, 3.4, 5, 7}
2)Intersetion----Returns common elements present in both x and y
     a={2,3.4,5,67}        
b={1,5,7}
a.intersection(b)
{5}

3)difference---
a={23,56,78,345,67,89}
            
b={45,67,23,45,12,89,1,2,3,4}
            
a.difference(b)
            
{56, 345, 78}

membership operation : we check the member of the set or not by using membership operator 
======================
1) in operator and not in operator 

a={40,50,30,20,45}        
print(456 in a)            
False
print(50 not in a)           
False
print(20 in a)           
True
print(30 in a)            
True







=================================================================================



Dictionary data structure
=========================
collection of {key:value} pairs is called dictionary it is denoted by curly braces{}

dictionary is a mutable collection of many values and key values is immutable 







































