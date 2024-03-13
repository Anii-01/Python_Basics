#Question_7

Student_Dict = {}

def add_Student_Record():
    global Student_Dict
    Student_Name = 'Aniket'
    Student_roll_no = 1
    Student_class = 'BE'
    Student_marks = 90

    Student_Dict.update({Student_roll_no:{Student_Name,Student_class,Student_marks}})
    print("Student added Sucessfully!")

add_Student_Record()
print(Student_Dict)


def remove_Student_Record(Student_roll_no):
    global Student_Dict

    Student_Dict.pop(Student_roll_no)
    print("Student remove Sucessfully!")

def update_Student_Record(Student_roll_no,Student_Name,Student_class,Student_marks):
    global Student_Dict

    Student_Dict.setdefault()
    print("Student updates Sucessfully!")

def display_Student_Info(Student_roll_no):
    print(Student_Dict[Student_roll_no])
    print()







