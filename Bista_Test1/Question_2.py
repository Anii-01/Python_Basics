#Question_2 
#primt numbers between 1 to 100


for element in range(2,101): 
    for j in range(2,101):
        if element%j == 0:
            break
    if element == j:
        print(element,end=",")
