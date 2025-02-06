age = 19
if age > 18 and age < 21:
    print(" you can enter the venue but cannot drink")

if age > 18 :
    if age < 21:
     print(" you can enter the venue but cannot drink")

day = input("what day of the week is it ?")

if day == 'saturday' or day == 'sunday':
   print("it's weekend")
else:
   print("ugh it's a workday :(")

age = int(input("how old are you? "))
if age < 5 or age >= 65:
      print("you get in for free!")
else:
       print ("that will be 5$")

year = input("what year were you born in?")
if not year.isnumeric():
    year = input("that isn't a number. try again plz. what year were you born in?")

year = int(year)
print(f"youre born{2025-year} years ago")
