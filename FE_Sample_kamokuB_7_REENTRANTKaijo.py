n = int(input())

def factorial(n:int):
    # print(n,"×",end="")
    if n == 0:
        return 1

    return n * factorial(n - 1)

print("\n",factorial(n))
