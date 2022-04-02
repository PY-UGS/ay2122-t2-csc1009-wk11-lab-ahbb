class Calculator:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def adder(self,num1,num2):
        return num1+num2

    def subtractor(self,num1,num2):
        return num1-num2

    def multiplier(self,num1,num2):
        return num1*num2

    def divider(self,num1,num2):
        return num1/num2

    def clear(self):
        self.num1 = 0
        self.num2 = 0
        return self.num1,self.num2

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

num1 = float(num1)
num2 = float(num2)

c = Calculator(num1,num2)

print("Addition: ",c.adder(num1,num2))
print("Subtraction: ",c.subtractor(num1,num2))
print("Multiplication: ",c.multiplier(num1,num2))
print("Division: ",c.divider(num1,num2))
print("Clearing.")
print(c.clear())






