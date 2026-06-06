def factorial() :
    fact = 1
    for i in range(1, user_input + 1):
        print(i)
        fact *= i
    return fact
    
    
    
user_input = int(input("Enter a number:"))
result = f"Factorial of {user_input} is {factorial()}"
print(result)