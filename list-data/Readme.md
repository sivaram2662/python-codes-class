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
 
