#creating shape class 
class Shape():
    def __init__(self, num_sides, tesselates= False):
        #raises error if incorrect number of sides is entered 
        if num_sides <= 0:
            raise Exception("Number of sides should be positive")
        self.num_sides = num_sides 
        self.tesselates = tesselates 
    #creating function with adds number of sides for two shapes 
    def __add__(self, second_shape):
        total_sides = self.num_sides + second_shape.num_sides 
        #creating object for the new shape
        new_object = Shape(total_sides)

        return new_object


    def get_info(self):
        raise NotImplementedError

#creating Circle class to inherit from Shape

class Circle(Shape):
    def __init__(self, num_sides, tesselates = False):
        super().__init__(num_sides, tesselates)

    def get_info(self):
    #create a function to return shape info 
        statement_1 = f"The number of sides is: {self.num_sides}\n"
        if self.tesselates == True:
            return statement_1 + "This shape tesselates!"
        else: 
            return statement_1 + "This shape does not tessealte!"
       

    def __str__(self):
        return self.get_info()
        

class Square(Shape):
    def __init__(self, num_sides, tesselates = False):
        super().__init__(num_sides, tesselates)

    def get_info(self):
    #create a function to return shape info 
        statement_1 = f"The number of sides is: {self.num_sides}\n"
        if self.tesselates == True:
            return statement_1 + "This shape tesselates!"
        else: 
            return statement_1 + "This shape does not tessealte!"
       

    def __str__(self):
        return self.get_info()
        

if __name__ == "__main__": 
    circle = Circle(100, False)
    print(circle)
    
    square = Square(4, True)

    new_shape = circle + square 

    print(new_shape.num_sides)