# Even/Odd Function

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# User se input
number = int(input("Enter a number: "))

# Function call
result = check_even_odd(number)

print("The number is:", result)