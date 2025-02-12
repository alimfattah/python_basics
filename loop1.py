
# Break will exit the loop immediately
for letter in "supercalifragilisticexpialidocious":
    if letter == 'c':
        break
    print(letter)

# message = input("say hi: ")
# while True:
#     if message == "hi":
#         break
#     message = input("please say hi: ")
# print("FINALLY! THANKS FOR SAYING HI")

# Continue stops the current loop iteration
# But the loop continues on to the next iteration
for letter in "supercalifragilisticexpialidocious":
    if letter in "aeiou":
        continue
    print(letter)

#nested loop

for outer in range (1,5):
    print(outer)
    for inner in range (1,10):
        print("\t", inner)
