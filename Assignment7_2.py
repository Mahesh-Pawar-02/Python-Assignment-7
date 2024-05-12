# Problem Statement : Write a program which contains one class named as Circle. Circle class contains three instance variables as Radius ,
# Area, Circumference. That class contains one class variable as PI which is initialise to 3.14.  Inside init method initialise all instance
# variables to 0.0. There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display(). 
# Accept method will accept value of Radius from user. CalculateArea() method will calculate area of circle and store it into instance variable
# Area. CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference. 
# And Display() method will display value of all the instance variables as Radius , Area, Circumference. 
# After designing the above class call all instance methods by creating multiple objects. 

class Circle:
    PI = 3.14  # Class variable

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))

    def CalculateArea(self):
        self.Area = self.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print("Radius of the circle:", self.Radius)
        print("Area of the circle:", self.Area)
        print("Circumference of the circle:", self.Circumference)


# Creating objects of Circle class
circle1 = Circle()
circle2 = Circle()

# Calling instance methods for circle1 object
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

print("\n")

# Calling instance methods for circle2 object
circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()


# Test Case :
# Input  : Enter the radius of the circle: 10
# Output : Radius of the circle: 10.0
#          Area of the circle: 314.0
#          Circumference of the circle: 62.800000000000004