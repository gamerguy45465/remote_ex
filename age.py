import random as r

print("Hello, I am going to try to guess your age")
name = input("Name Please? ")

isTrue = False

ages = []

while(not isTrue):
    age = r.randint(0, 100)
    if age in ages:
        continue
    response = input(f"is {age} correct?")
    if response == 'y':
        print(f"{name} is {age} years old.")
        isTrue = True 

    elif response == 'n':
        print("Rats.")
        ages.append(age)
        if len(ages) == 100:
            print("Impossible, you can't be that old")
            isTrue = True 
