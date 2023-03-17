# n1=int(input("Enter First Number:")) 
# n2=int(input("Enter Second Number:")) 
# if n1>n2: 
#  print("Biggest Number is:",n1) 
# else : 
#     print("Biggest Number is:",n2) 


# num =int(input('enter the name:'))
# if num%2 == 0:
#     print('it is even number')
# if num%3 == 0:
#     print("it odd number")
# else:
#     print('number')
    
    
# age = int(input("Enter  your age"))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("you are not eligible to vote")

# rows =int(input("enter a no:"))
# for i in range(rows):
#     for j in range(i):
#         print(i, end=' ')
#     print('')

#
# num = input('Enter the number:')
# rev = ''.join(reversed(num))
# if (num == rev):
#   print(num,'is a Palindrome')
# else:
#   print(num,'is not a Palindrome')
  
   
#   print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
# month = input("Input the name of Month: ")

# if month == "february":
# 	print("No. of days: 28/29 days")
# elif month in ("april", "june", "september", "november"):
# 	print("No. of days: 30 days")
# elif month in ("january", "march", "may", "july", "august", "october", "december"):
# 	print("No. of days: 31 day")
 
 
 
 
# name = input("Enter a character: ")
# if name. isalpha():

#     print(name, "All characters are alphabets")
# elif name. isdigit():
#     print(name, "All characters are numbers")
# elif name. isalnum():
#     print(name, "All characters are alphanumeric")
# else:
#     print("All characters are special characteristics")

# i=1
# while i < 5:
#     print(i)
#     i+= 1
# print("it is a neasted value")
# num = int(input("enter number"))
# for sss in range(num,50):
#     print(num)
# if num%2 == 0:
#    if num%3 == 0:
#       print ("Divisible by 3 and 2")
#    else:
#       print ("divisible by 2 not divisible by 3")
# else:
#    if num%3 == 0:
#       print ("divisible by 3 not divisible by 2")
#    else:
#       print  ("not Divisible by 2 not divisible by 3")

# from flask import Flask

# app = Flask(__name__)

# @app.route("/home")
# def home():
#     return "Welcome! i am siva.<h1>i am siva<h1>"

# @app.route("/admin")
# def admin():
#     return "hello sai.<h1>i am sai<h1>"
# if __name__ == "__main__":
#     app.run()











# list = [10,9,11,14,5]
# big = list[0]

# for item in list:
#     if big<item:
#         big = item
# print('biggest is..', big)



# sample_list = [1, 2, 3, 4, 5]
# a=sample_list[:-2]
# b=a[::-1]
# print(b+sample_list[3:])


# list=[3,4,523,45,67,34,56,76,87,23,45,23,45,56,77]
# for i in list:
#     if i%2==0:
#         print(i,'even number')
#     else:
#         print(i,'odd number')



# print('hello word')
# print("what is your name")
# myname= input()
# print('it is very lucky, '+myname)
# print('how much of length in given name')
# print(len(myname))
# print('what  is your age')
# name=input()
# print('You will be ' + str(int(name) + 1) + ' in a year.')


# name=int(input('enter a number'))
# p=1
# for i in range(name):
#     for n in range(p):
#         print('*',end="")
#         p= p + 1
#     print()
    
    












# name=[22,44,3,6,8,3,9,22,66]
# num=[66,53,43,22,99,2,3,6]
# for key in num:
#     name.append(key)
# print(name)
# print(len(name))
# # value=set(name)
# # for value in name:
# #     if value%2 == 0:
# #         print(value,'it is even number')
# # else:
# #     print(value,'it is odd number')




# if __name__ == "__main__":
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
#     print(f"{avg_score:.2f}")















# # if __name__ == "__main__":
# n = int(input())
# arr = map(int, input().split())
# print(sorted(set(arr), reverse=True)[1])



































