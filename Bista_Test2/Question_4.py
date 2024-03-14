#Question_4 : Factorial of number using Generator function

def factorial_generator(limit_num):
    for number in range(limit_num):
        yield number

limit_num = int(input("Enter number : "))
gen = factorial_generator(limit_num)

fact = 1
for value in gen :
    
    if(value == 0):
        pass
    else:
        print(value,"! x ", end='')     
        fact = fact + (fact * value)
   
print(" = ",fact)


        



        



