print("***WELCOME TO THE NAME APP***")
first_name = input("What is your first name??")
last_name = input("What is your last name??")

full_name = first_name + " " + last_name
print("Hi there, " + full_name)

age = input("How old are you (in years) ? ")
days = float(age) * 365

# Improved version with f-string:
print(f"{age} years is {days} days old")

age = input("How old are you (in years) ? ")
days = float(age) * 365
print(days)


print("WELCOME TO THE USELESS STORE")
print("*" * 30)

item = input("What item are you purchasing: ")
price = float(input(f"What is the price of {item}: "))
quantity = float(input(f"How many {item} are you buying: "))

print(f"added {quantity} {item}(s) to shopping cart!")
print(f"Subtotal: ${quantity * price}")
