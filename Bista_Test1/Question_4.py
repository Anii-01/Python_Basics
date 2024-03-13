#Question_4
#python program to zip two list together and create a list of tuples 

#input lists
test_list1 = [[1],[2],[3]]
#test_list2 = [[4],[5],[6]]
test_list2 = [['a'],['b'],['c']]

#print("The original list 1 is : " + str(test_list1))
#print("The original list 2 is : " + str(test_list2))

res = list(map(list.__add__, test_list1, test_list2))
print("The modified zipped list is : " + str(res))
