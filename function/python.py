# def hello():
#     print('howdy')
#     print('hello world')
#     print('name')
# hello()
# hello()
# hello()

# #------------------------------------------

# def name():
#     print('ram')
#     print('super')
#     print('good')
# name()
# name()
# name()


# #---------------------------------------
# def hello(name):
#     print('Hello,' + name)
# hello('siva')
# hello('seshu')


# def value(variable):
#     print('value,' + variable)
# value('super')
# value('good')
# value('name')
# #------------------------------------

# import random

# def answer(name):
#     if name ==1:
#         return 'it is safe'
#     elif name==2:
#         return 'it is not crt value'
#     elif name==3:
#         return 'if it is value key'
#     elif name==4:
#         return 'if it has to display comtent'
# r=random.randint(1,4)
# name=answer
# print(name)
# print(answer(random.randint(1,4)))



# def a():
#     print('a()starts')
#     b()
#     d()
#     print('a()returns')
# def b():
#     print('b()starts')
#     c()
#     print('b()returns')
# def c():
#     print('c()starts')
#     print('c()returns')
# def d():
#     print('d()starts')
#     print('d()returns')
# a()
# b()
# c()
# d()


# import random

# def suffer(name):
#     if name==1:
#         return "it is call"
#     elif name==2:
#         return "it has to check"
#     elif name==3:
#         return "it has very special"
# name=random.randint(1,3)
# value=suffer()
# print(value)
# print(suffer(random.randint(1,3)))


# def a():
#     print('a() starts')
#     b()
#     c()
#     print('a() returns')
# def b():
    
    
    
# def spam():
#     name = 234
#     name


# def spam():
#     eggs = 'spam local'
# print(eggs) # prints 'spam local'

# def bacon():
#  eggs = 'bacon local'
#  print(eggs) # prints 'bacon local'
#  spam()
#  print(eggs) # prints 'bacon local'
# eggs = 'global'
# bacon()
# print(eggs) 

# def hello():
#     print('name')
#     print('value')
#     print('name')
# hello()
# hello()
# hello()



# def keyvalue(value):
#     print('this is,'+value)
# keyvalue('siva')
# keyvalue('ram')
# keyvalue('pavan')



# import random 
# def name(key):
#     if key == 1:
#         return'it is ceartain'
#     elif key==2:
#         return 'it name is ram'
#     elif key==3:
#         return 'it is display value'
#     elif key==4:
#         return'it is ram value'

# temp=random.randint(1,4)
# value=name(temp)
# print(value)
# print(name(random.randint(1,4)))




# def a():
#     print('a() starts')
#     b()
#     d()
#     print('a()returns')
# def b():
#     print('b() starts')
#     c()
#     print('b() returns')
# def c():
#     print('c()starts')
#     print('c() returns')
# def d():
#     print('d() starts')
#     print('d() returns')
    
# a()
# b()
# c()
# d()


# def spam ():
#     global eggs
#     eggs='spam'
# def bacon():
#     eggs='bancon'
# def ham():
#     print(eggs)

# eggs=42
# spam()
# print(eggs)


# def scam(divideBy):
#     return 42 / divideBy
# print(scam(2))
# print(scam(4))




import time 
indent = 0
indentincressing=True

while True:
    print('' *indent,end='')
    time.sleep(0.1)
    if indentincressing:
        indent=indent+1
        if indent==20:
            indentincressing =False
    else:
        indent=indent-1
        indentincressing =True
        

    













