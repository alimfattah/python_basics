fav_color = "green"
fav_movie = "amadeus"
fav_food = "pasta"

if fav_color == "green":
    print("I love green too!")
    if fav_movie =="amadeus":
        print("I love amadeus too!")
        if fav_food == "pasta":
            print ("I love pasta too!")

fav_color = "green"
fav_movie = "amadeus"
fav_food = "pasta"

if fav_color == "green":
    print("I love green too!")
if fav_movie =="amadeus":
    print("I love amadeus too!")
if fav_food == "pasta":
    print ("I love pasta too!")

fav_color = "purple"
fav_movie = "amadeus"
fav_food = "pasta"

if fav_color == "green":
    print("I love green too!")
    if fav_movie =="amadeus":
        print("I love amadeus too!")
        if fav_food == "pasta":
            print ("I love pasta too!")

unit = input ("what unit are you using? ")
temp = int(input ("what temperature is the water? "))
if unit == 'f':
    if temp == 212:
        print ("water is boiling")
    else:
        print("water is not boiling. must hit 212F")
elif unit == 'c':
    if temp == 100:
        print ("water is boiling")
    else:
        print("water is not boiling. must hit 100c")
elif unit == 'k':
    if temp == 373:
        print ("water is boiling")
    else:
        print("water is not boiling. must hit 373k")
else:
    print("I dont know those units, sorry!!! ")
