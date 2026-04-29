x = 10
y = 5
x += 3
y *= 2
print(f"After += and *= operations: x={x}, y={y}")
print(f"result of x / y = {x / y}")

a = 15
b = 8
c = 12
cond1 = (a > b)
cond2 = b % 2 == 0
cond3 = c <= a
final_condition = cond1 or (cond2 and c<= a)
print(f"Comparison results: a>b={cond1}, b is even={cond2}, c<=a={cond3}")
print( f"final_condition = {final_condition}")

score = int(input("\nEnter your score (0-100): "))
if score >= 90:
    grade = 'A' 
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:    grade = 'F'
print(f"Your grade is: {grade}")

num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /: ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:    result = "Invalid operation"
print(f"result: {num1} {operation} {num2} is = {result}")

