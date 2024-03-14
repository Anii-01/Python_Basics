#Question_5 : Round values for each item present in the list using map function

def roundValues(number):
    return (round(number))

#input_values
input_list = [2.6743,3.63526,4.2325,5.9687967,6.3265,7.6988,8.232,9.6907]

result_rounded_list = map(roundValues , input_list)
print(list(result_rounded_list))