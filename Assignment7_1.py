
# Problem Statement : Write a program which contains one class named as Demo.  Demo class contains two instance variables as no1 ,no2.  
# That class contains one class variable as Value.  There are two instance methods of class as Fun and Gun which displays values of instance 
# variables. Initialise instance variable in init method by accepting the values from user. 

# After creating the class create the two objects of Demo class as : 
# Obj1 = Demo(11,21) 
# Obj2 = Demo(51,101) 

# Now call the instance methods as 
# Obj1.Fun() 
# Obj2.Fun() 
# Obj1.Gun() 
# Obj2.Gun()

class Demo:
    Value = 10  # Class Variable

    def __init__(self, No1, No2):
        self.No1 = No1
        self.No2 = No2

    def Fun(self):
        print("Values of instance variables no1 and no2 for this object are:", self.No1, "and", self.No2)

    def Gun(self):
        print("Class variable Value for this object is:", self.Value)


# Creating objects of Demo class
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling instance methods
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

# Test Case : 
# Values of instance variables no1 and no2 for this object are: 11 and 21
# Values of instance variables no1 and no2 for this object are: 51 and 101
# Class variable Value for this object is: 10
# Class variable Value for this object is: 10