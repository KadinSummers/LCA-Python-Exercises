def greet():
   print("Hello, World!")
greet()

def personalized_greeting(name):
    return(f"Hello, {name}!")
print(personalized_greeting("Kadin"))
 
def square(number):
    return number * 2
result_square = square(5)
print(result_square)
result_square =(square(5))
print(f"The square of 5 is: {result_square}")

def rectangle_area(length, width):
    return length * width
area = rectangle_area(4, 5)
print(f"Rectangle area for 4 x 5 is: {area}")

def apply_operation(func, number):
    return func(number)
def double(number):
    return number * 2
double_result = apply_operation(double, 7)
print(f"Double of 7 is: {double_result}")
square_result = apply_operation(square, 3)
print(f"Square of 3 is: {square_result}")
