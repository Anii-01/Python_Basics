#Question_6 - to_check even numbers


#input_list
my_nums = [1,2,3,4,5,6]

def is_even(num):
     return num%2 == 0

print(list(filter(is_even,my_nums)))

for n in filter(is_even,my_nums):
     print("Even numbers are : ", n)
