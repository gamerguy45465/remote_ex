import random as r

print("Hello, I am going to try to guess your age")
name = input("Name Please? ")

isTrue = False

while(not isTrue):
    age = r.randint(15, 30)
    response = input(f"is {age} correct?")
    if response == 'y':
        print(f"{name} is {age} years old.")
        isTrue = True 

    elif response == 'n':
        print("Rats.")
