#Question_3 - without list comprehension

class Maths_Operations:

    def __init__(self,input_list):

        self.input_list = input_list

    def Square_Of_Positive_Integers(self,input_list):

        square_list = []
        for number in input_list:
            if number >= 0 :
                square_list.append(number**2)
        return square_list

    def Cubes_Of_Negative_Integers(self,input_list):

        cube_list = []
        for number in input_list:
            if number < 0 :
                cube_list.append(number**3)
        return cube_list
    
    def Absolute_values_Of_Integers(self,input_list):

        absolute_list = []
        for number in input_list:
            absolute_list.append(abs(number))
        return absolute_list
    
    def Even_numbers(self,input_list):

        even_num_list =[]
        for number in input_list:
            if ((number % 2 == 0) and (number > 10)):
                even_num_list.append(number)
        return even_num_list
    
    def Display_Result(self,obj):

        print("Square of Positive Integers: ",obj.Square_Of_Positive_Integers(numbers))
        print("Cubes of Negative Integers: ",obj.Cubes_Of_Negative_Integers(numbers))
        print("Absolute Values of All Integers: ",obj.Absolute_values_Of_Integers(numbers))
        print("Even Numbers Greater than 10 : ",obj.Even_numbers(numbers))
        

#input_list
numbers = [5,-8,12,-3,17,0,-10,6]

obj = Maths_Operations(numbers)
obj.Display_Result(obj)


            








