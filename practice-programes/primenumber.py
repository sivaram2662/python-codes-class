name=int(input("enter the value:"))
if name>1:
    for i in range(2,name):
        if i%name==0:
            print(name,'it is  not primenumber')
            break
        else:
            print(name,'it is prime number')
    else:
        print(name,"it is  prime number")
        
        
        


