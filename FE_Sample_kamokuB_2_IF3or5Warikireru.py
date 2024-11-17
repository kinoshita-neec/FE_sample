num = int(input())
def fizzBuzz(num):
    # print(num%3,num%5)

    result:str = ""

    if (num%3==0)&(num%5==0):
        result="3と5で割り切れる"
    elif (num%3 == 0):
        result="3で割り切れる"
    elif num%5 == 0:
        result="5で割り切れる"
    else:
        result="3でも5でも割り切れない"
    
    return result

print(fizzBuzz(num))

