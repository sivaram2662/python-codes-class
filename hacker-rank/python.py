# # if __name__ == "__main__":
# n = int(input())
# arr = map(int, input().split())
# # print(sorted(set(arr), reverse=True)[1])
# print(arr)
# def f1(): 
#  if __name__=='__main__': 
#   print("The code executed as a program") 
#  else: 
#   print("The code executed as a module from some other program") 
#  f1()


# num=int(input("enter a terms"))
# def fibonacci(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     return fibonacci(n-1) + fibonacci(n-2)

# # Generate the first 10 numbers in the Fibonacci series
# for i in range(num):
#   print(fibonacci(i))
  
  
  
  
# num=int(input('enter a number'))
# for i in range(num):
#       print('it is febonacci')
#       if i in fibonacci():
#           if i == 0:
#               print('it is fibonaccis')
#           elif i == 1:
#               print('it is not fibonaccis')
          
        
        
        
        
        
# size =int(input("Enter the size : "))
# length = 0
# count = 0
# term1 = 0
# term2 = 1  
# while length < size :
#     count = count + 1
#     nextTerm = term1 + term2
#     term1 = term2
#     term2 = nextTerm
#     length = len(str(term2))
# if size == length :
#     print("The first fibonacci number of given length is : ",term2)
#     print("Index of this number is : ",count)    
               
               
               
               
# num=int(input('enter a terms:'))
# def fibonacci(n):
#     # if n<=0:
#     #     print('it is terms')
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-1)
# print(fibonacci(num))


# def fibonacci(n):
#     if n <= 0:
#         print("Wrong Input!")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# num = int(input("Enter the nth term: "))
# print(fibonacci(num))



# per=[3,4,5,4,5,3,2,5,6,8,8,9]
# num=[3,5,6,78,24,45,24]
# for i in num:
#     per.append(i)
# print(per)
# def fibonacci(per):
#     if per ==0 :
#         return 0
#     elif per ==1:
#         return 1
#     else:
#         return fibonacci(per-1)+ fibonacci(per-2)
# print(fibonacci(per))




# name=int(input('enter a number:'))
# for i in range(name):
#     def febinacci(i):
#         if i == 0:
#             return 0
#         elif i == 1:
#             return 1
#         else:
#             return febinacci(i-1)+febinacci(i-2)
# print(febinacci(i))




# def febinacci(n):
#     if n <=0:
#         print('it is wrong')
#     elif n ==1:
#         return 1
#     elif n ==2:
#         return 2
#     else:
#         return febinacci(n-1)+febinacci(n-2)
# name=int(input("enter a number:"))
# print(febinacci(name))

     
# def febinacci(n):
#     a,b=0,1
#     for i in range(n):
#         a, b= b ,a+b
#         return a
    
# for i in range(10):
# #     print(febinacci(i))

# def fibonacci(n):
#   a, b = 0, 1
#   for i in range(n):
#     a, b = b, a+b
#   return a

# for i in range(10):
#   print(fibonacci(i))


# def fibonacci(n):
#   a, b = 0, 1
#   result = []
#   for i in range(n):
#     result.append(a)
#     a, b = b, a+b
#   return result


# print(fibonacci(10))


# def febinocci(n):
#     a,b =0,1
#     for i in range(n):
#         a,b =b,a+b
#         return a
#     for i in range (10):
#         print(febinocci(i))
        

def febinocci(name):
    a,b=0,1
    rename=[]
    for i in range(name):
        rename.append(a)
        a,b=b,a+b
        return rename
print(febinocci(10))
        
















    