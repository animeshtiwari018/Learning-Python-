chai = input("choose your cup size (small/medium/large:)").lower()

if chai == "small":
    print("Price is 10 rupees")
elif chai == "medium":
    print("Price is 15 rupees")
elif chai == "large": 
    print("Price is 20 rupees")
else:
    print("Unknown cup size")