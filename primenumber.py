num=int(input("enter a number:"))
if num >1:
    for i in range(2,num):
        if (num % i) ==0:
            print('it is prime number')
            break
        else:
            print('is not a prime number')
else:
    print('is not a prime number')


