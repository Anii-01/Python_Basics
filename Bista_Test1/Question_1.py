#Question_1
#Problem statement : Create a list of tuples containing all pairs of numbers from two list, where the sum of the pair is even from two lists

#input lists
list1 = [1,2,3]
list2 = [4,5,6]

result = []

for element1 in range(0,len(list1)):
    for element2 in range(0,len(list2)):
        
        if ((list1[element1] + list2[element2]) % 2 == 0) :
            result.append((list1[element1],list2[element2]))

print("The resulting list of tuples is : ",result)


        


    










