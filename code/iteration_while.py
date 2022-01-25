import random

number_to_guess = random.randint(0, 100)
print(number_to_guess)

while True:
    guess = int(input("Please enter your guess... "))

    if guess < number_to_guess:
        print("too small")
    elif guess > number_to_guess:
        print("too big")
    else:
        print("just right!")
        break
