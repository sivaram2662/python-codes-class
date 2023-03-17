name=int(input("enter anumber:"))
def febinaccio(name):
    if name==0:
        return 0
    elif name==1:
        return 1
    else:
        return febinaccio(name-1)+febinaccio(name-2)
print(febinaccio(name))



#---------------------------------------------

num=int(input("enter a terms"))
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Generate the first 10 numbers in the Fibonacci series
for i in range(num):
  print(fibonacci(i))

#--------------------------------------------------  
num=int(input('enter a terms:'))
def fibonacci(n):
    # if n<=0:
    #     print('it is terms')
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-1)
print(fibonacci(num))

#--------------------------------------------

name=int(input('enter a number:'))
for i in range(name):
    def febinacci(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return febinacci(i-1)+febinacci(i-2)
print(febinacci(i))


#----------------------------------------------
def febinacci(n):
    if n <=0:
        print('it is wrong')
    elif n ==1:
        return 1
    elif n ==2:
        return 2
    else:
        return febinacci(n-1)+febinacci(n-2)
name=int(input("enter a number:"))
print(febinacci(name))

#--------------------------
    
def febinacci(n):
    a,b=0,1
    for i in range(n):
        a, b= b ,a+b
        return a
    
for i in range(10):
#     print(febinacci(i))

#------------------------

 def fibonacci(n):
  a, b = 0, 1
  result = []
  for i in range(n):
    result.append(a)
    a, b = b, a+b
  return result


print(fibonacci(10))      
#-------------------------------
def febinocci(name):
    a,b=0,1
    rename=[]
    for i in range(name):
        rename.append(a)
        a,b=b,a+b
        return rename
print(febinocci(10))
        
















    