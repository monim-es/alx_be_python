number1 = 10 
number2 = 5

def addition(a,b): 
  return a+b 

def substraction(a,b): 
  return a-b

def Multiplication(a,b) : 
  return a*b

add = addition(number1,number2)
sub = substraction(number1, number2)
multi = Multiplication(number1, number2)
print(f"Addition of {number1} and {number2} is {add}")
print(f"Subtraction of {number1} and {number2} is {sub}")
print(f"Multiplication of {number1} and {number2} is {multi}")