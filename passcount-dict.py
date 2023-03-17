n = int(input("Enter the number of students: "))
dict = {}
student_pass_count = 0
student_fail_count = 0
for i in range(n):
    name = input("Enter student name: ")
    marks = eval(input("Enter student marks: "))
    hallticket =eval(input('enter a hallticket num'))
    # dict [name] = marks,hallticket
# for i in dict: 
if marks>= 35:
      student_pass_count +=1
      print('your passed:')
else:
        student_fail_count +=1
        print('your faild:')
print("exam pass count:", student_pass_count)
print("exam fail count:", student_fail_count)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


