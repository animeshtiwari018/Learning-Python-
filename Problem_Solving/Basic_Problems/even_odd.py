def odd_even() :
    if(user_input % 2 == 0):
        print(f"Number {user_input} is Even!")
    else:
        print(f"Number {user_input} is Odd!")
    
user_input = int(input("Enter a number:"))
result = odd_even()
print(result)