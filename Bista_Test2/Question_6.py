#Question_6 : dictionary..

#function for frequency count
def frequency_count(file_paths):

    dict = {}
    for paths in file_paths:
        dict.update({paths:file_paths.count(paths)})

    print(dict)
    
#input_list
file_paths = ["/home/user/documents/report.txt","/home/user/documents/project1/specs.txt","/home/user/documents/project1/code/main.py","/home/user/documents/project2/notes.txt","/home/user/pictures/image.jpg"]
frequency_count(file_paths)


#nested dictionary hierarchy - pending

dict2 = {}
string_file_paths = str(file_paths)
#print(string_file_paths)
str1 = string_file_paths[0]
#print(str1)



