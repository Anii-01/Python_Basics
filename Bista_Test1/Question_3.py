#Question_3

List1 = [" Python is a powerful programming language"," Python is used for web development"," Python has a rich set of libraries "]

string = str(List1)
splitted = string.split()
dict = {}

for word in splitted:
    if(word.isalnum()):
            Count = splitted.count(word)

            dict.update({word:Count})

print(dict)
    

