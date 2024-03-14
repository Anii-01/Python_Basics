#Question_1
#Sum of N Numbers

def sum_Numbers(input_number):
    current_sum = 0
    for number in range(0,input_number+1):
        current_sum = current_sum + number
    return current_sum

input_number = int(input("Enter the number : "))
result = sum_Numbers(input_number)
print("The sum of numbers is :",result)





