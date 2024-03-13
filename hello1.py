

# initializing lists
test_list1 = [1,2,3]
test_list2 = ['a','b','c']

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using map() + __add__
# zipping lists of lists
res = list(map(list.__add__, test_list1, test_list2))

# printing result
print("The modified zipped list is : " + str(res))


stock_prices = [('abc',200),('def',300),('ghe',400)]   #packed tuple

for items in stock_prices:
    print(items)

for a,b in stock_prices:     #unpacking tuple
    print(a)

for a,b in stock_prices:
    print(b*10)

