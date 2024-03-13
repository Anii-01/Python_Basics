#Question_5

even_Number_list = []
odd_Number_list = []

#generator function to print the odd and even number list in range
def my_generator():

    for number in range(2,20):
        yield number
        if((number %2) == 0):
            even_Number_list.append(number)
        else:
            odd_Number_list.append(number)

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(even_Number_list)
print(odd_Number_list)


#prime number using normal method
'''

print ("The Prime Numbers in the range are: ")  
for number in range (2, 20+ 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
            

'''