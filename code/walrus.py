# Simple Assignment
num = 15

print(num)
# >>> 15

print(num = 15)
# >>> TypeError

# Walrus
print(num := 15)
# >>> 15

# Get and test user input
inp = input("> ")
if inp.lower() in ["y", "yes"]:
    print("you said yes!")

if (inp := input("> ")).lower() in ["y", "yes"]:
    print("You said yes!")
