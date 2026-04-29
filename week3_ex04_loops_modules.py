import random


fruits = ["apple", "banana", "orange", "grape", "mango"]
# Loop through the list of fruits and print each fruit
for fruit in fruits:
    print(fruit)  

    print("\nCountdown:")
    count = 5
    while count >= 1:
        print(count)
        count -= 1
        print("Blast off!")

print("\nFirst 10 square numbers:")
for i in range(1, 11):
    print(f"{i} squared = {i**2}") 

colours = ["red", "green", "blue", "yellow", "purple", "orange", "pink",]
print("\n3 random colours")
for i in range(3):
    random_colour = random.choice(colours)
    print(random_colour)

     