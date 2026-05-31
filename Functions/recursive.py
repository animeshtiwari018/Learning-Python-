def chai(n) :
    print(n)
    if n == 0:
        return("All cups poured")
    return(chai(n-1))

print(chai(3))