answer = input("Please say hi ")
while answer != "hi":
    answer = input ("rude. say hi...")
print("thank you, Hi to you too!")

num = 10
while num > 0:
    print(f"Number is : {num}")
    num -= 1 
print("after loop 1")
num2 = 1
while num2 <= 10:
    print(f"Number is : {num2}")
    num2 += 1 
print("after loop 2")

count = 1
while count > 8:
    print("*" * count)
    count+=1

count = 7
while count > 0:
    print("*" * count)
    count-=1

word = "Tacos"
for character in word:
    print(character)

for letter in "pop tart":
    print(letter)
print("*****")

for num in range(5,10):
    print(num)

for num in range(0,100,10):
    print(num)

for num_bottles in range(99,0,-1):
    print(f"{num_bottles} bottles of beer on the wall.")
    print(f"{num_bottles} bottles of beer.")

    if num_bottles == 1:
        print(f"take one down, pass it around, no more bottles of beer on the wall.")
    else:    
        print(f"take one down, pass ot around,{num_bottles - 1} bottles of beer on the wall.")
    print("*" * 20)

num_bottles2 = 99
while num_bottles2 > 0 :
    print(f"{num_bottles} bottles of beer on the wall.")
    print(f"{num_bottles} bottles of beer.")

    if num_bottles == 1:
        print(f"take one down, pass it around, no more bottles of beer on the wall.")
    else:    
        print(f"take one down, pass ot around,{num_bottles - 1} bottles of beer on the wall.")
    print("*" * 20)
    num_bottles2 -=1
