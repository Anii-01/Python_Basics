#Question_3 using the - "List Comprehension"

inputlist = [5,-8,12,-3,17,0,-10,6]

result_list = [(element**2) for element in inputlist if element >= 0 ]
print("Square of Positive Integers: ",result_list)
result_list = [(element**3) for element in inputlist if element < 0 ]
print("Cubes of Negative Integers: ",result_list)
result_list = [abs(element) for element in inputlist]
print("Absolute values of all integers:  ",result_list)
result_list = [element for element in inputlist if (((element % 2) == 0) and (element > 10))]
print("Even numbers greater than 10: ",result_list)
  


