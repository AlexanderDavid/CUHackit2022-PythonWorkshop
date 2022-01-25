import random

number_to_guess = random.randint(0, 100)
print(number_to_guess)

for i in range(5):
    guess = int(input(f"Please enter your guess ({i}/5)... "))

    if guess < number_to_guess:
        print("too small")
    elif guess > number_to_guess:
        print("too big")
    else:
        print("just right!")
        break
else:
    print("You'll get em next time")
