age = input("How old are you? ")
age = int(age)

if age >=21:
    print("come on in!")
else:
    print("go home kid")

color = "blue"

if color == "green":
    print("beginner")
elif color == "blue":
    print("intermediate")
elif color == "black":
    print("advanced")

num = 3
if num > 0:
    print("from the if")
elif num==3:
    print("from elif 1")
elif num<10:
    print("form elif 2")

num = 3
if num > 0:
    print("from the if 1")
if num==3:
    print("from the if 2")
if num<10:
    print("form the if 3")


first_name = input ("Enter your first name : ")
last_name = input ("enter your last name:")
name_length = len(first_name) +len(last_name)

if name_length ==12:
    print(f"{first_name} {last_name} is exactly the average of the american names") 

elif name_length < 12:
    print(f"{first_name} {last_name} is shorter than the average of the american names") 
else:
    print(f"{first_name} {last_name} is longer than the average of the american names") 
