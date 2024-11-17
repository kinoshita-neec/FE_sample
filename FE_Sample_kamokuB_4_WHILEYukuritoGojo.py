num1=int(input("num1:",))
num2=int(input("num2:",))

def gcd(num1,num2):
    x=num1
    y=num2
    # print("1","x",x,"y",y)

    while x != y:
        if x > y:
            x = x - y
            # print("2","x",x,"y",y)
        else:
            y = y - x
            # print("3","x",x,"y",y)

    return x
     
print(num1,"と",num2,"の最大公約数は",gcd(num1,num2))

"""
ユークリッド互除法
2つの数のうち大きい方から小さいほうを引くことを両者が等しくなるまで繰り返す
FE_H20S_15にも類題

"""
