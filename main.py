import random

color = input("Enter a color: ")

if color.lower() == "red":
    flowers = ["Rose", "Carnation", "Poppy"]
    flower = random.choice(flowers)
    print(f"Here's a {flower} flower for you!")

elif color.lower() == "blue":
    flowers = ["Forget-Me-Not", "Iris", "Bluebell"]
    flower = random.choice(flowers)
    print(f"Here's a {flower} flower for you!")

elif color.lower() == "yellow":
    flowers = ["Daisy", "Sunflower", "Marigold"]
    flower = random.choice(flowers)
    print(f"Here's a {flower} flower for you!")

else:
    print("Sorry, I don't know a flower for that color.")