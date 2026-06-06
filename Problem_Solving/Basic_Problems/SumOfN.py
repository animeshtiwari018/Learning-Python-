userInput = int(input("Enter a number:"))

def SumOfNumbers():
    sum = 0
    for i in range(0, userInput + 1):
        print(i)
        sum += i
    return sum
        
print("Sum =", SumOfNumbers())



# userInput = int(input("Enter a number: "))

# def SumOfNumbers():
#     total = 0
#     for i in range(0, userInput + 1):
#         total += i
#     return total

# print(SumOfNumbers())