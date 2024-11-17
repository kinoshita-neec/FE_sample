x=int(input("x:",))
y=int(input("y:",))

# xのy乗を求める関数
def pow(x:int,y:int):
    return x**y

# √x**2 + y**2　を求める関数
def calc(x:int,y:int):
    return pow(pow(x,2) + pow(y,2) ,0.5)

print(calc(x,y))

"""
√〇　は　〇の0.5乗

参考
(x**2 + y**2)＝平方数の和はフェルマーの二平方和定理などで登場する
●m,nがいずれもx**2 + y**2の形で表せるならmnもx**2 + y**2の形で表せる
●奇素数pについてpを4で割ったあまりが1<->pは二つの平方数の和で表せる
 pが素数であるとき、pが2つの平方数の和で表されるための必要十分条件は
 p=2あるいはp mod 4 ≡ 1 (pを4で割ったあまりが1)
"""
