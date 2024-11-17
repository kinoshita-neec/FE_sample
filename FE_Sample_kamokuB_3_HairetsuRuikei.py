#設問の変数inは予約語なので代わりに変数intsとする
#userInput = input()
#ints = [map(int, userInput(),split())]

ints= [3,2,1,6,5,4]

def makeNewArray(ints):
    out = []
    i = 0
    tail = 0
    # print("1 ints",ints,"out",out,"i",i,"tail",tail)

    out.append(ints[0])
    # print("2 ints",ints,"out",out,"i",i,"tail",tail)

    for i in range(1,len(ints)-1):
        tail = out[len(out)-1]
        # print("3 ints",ints,"out",out,"i",i,"tail",tail)
        out.append(tail + ints[i])
        # print("4 ints",ints,"out",out,"i",i,"tail",tail)
    return out

print(makeNewArray(ints))
"""
return out なのでoutの値の変化に注目してトレースする
iとtailはそれぞれintsとoutの添え字を指定する変数

    i→
int[3,2,1,6,5,4]

    tail→
out[]

ints[A,B,C,D・・・]に対して、
[A, A+B, A+B+C, A+B+C+D・・・]という各要素番号までの累計をしている
"""
