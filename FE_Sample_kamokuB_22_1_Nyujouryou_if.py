# FEサンプル問題'22公開　1
def fee(age):
    if age <= 3:
        ret = 100
    elif age <= 9:
        ret = 300
    else:
        ret = 500
    
    return ret

age = int(input("年齢を入力：",))
print("入場料：",fee(age),"円")