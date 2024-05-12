# Problem statement : Write a program which contains one class named as Arithmetic.  Arithmetic class contains three instance variables as
# Value1 ,Value2. Inside init method initialise all instance variables to 0.  
# There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division(). 
# Accept method will accept value of Value1 and Value2 from user. Addition() method will perform addition of Value1 ,Value2 and return result. 
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result. 
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result. 
#Division() method will perform division of Value1 ,Value2 and return result. 
#After designing the above class call all instance methods by creating multiple objects. 

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    try:
        def Accept(self):
            self.Value1 = float(input("Enter first value: "))
            self.Value2 = float(input("Enter second value: "))

        def Addition(self):
            return self.Value1 + self.Value2

        def Subtraction(self):
            return self.Value1 - self.Value2

        def Multiplication(self):
            return self.Value1 * self.Value2

        def Division(self):
            if self.Value2 == 0:
                return "Cannot divide by zero!"
            else:
                return self.Value1 / self.Value2

    except ZeroDivisionError as zobj:
        print("Exception occured :",zobj)

    except ValueError as vobj:
        print("Exception occured :",vobj)

    except Exception as eobj:
        print("Exception occured :",eobj)


# Creating objects of Arithmetic class
arithmetic1 = Arithmetic()
arithmetic2 = Arithmetic()

# Calling instance methods for arithmetic1 object
arithmetic1.Accept()
print("Addition:", arithmetic1.Addition())
print("Subtraction:", arithmetic1.Subtraction())
print("Multiplication:", arithmetic1.Multiplication())
print("Division:", arithmetic1.Division())

print("\n")

# Calling instance methods for arithmetic2 object
arithmetic2.Accept()
print("Addition:", arithmetic2.Addition())
print("Subtraction:", arithmetic2.Subtraction())
print("Multiplication:", arithmetic2.Multiplication())
print("Division:", arithmetic2.Division())

# Test Case : 

# Input  : Enter first value: 30
#          Enter second value: 10
# Output : Addition: 40.0
#          Subtraction: 20.0
#          Multiplication: 300.0
#          Division: 3.0

# Input  : Enter first value: 21
#          Enter second value: 11
# Output : Addition: 42.0
#          Subtraction: 10.0
#          Multiplication: 231.0
#          Division: 1.9090909090909092