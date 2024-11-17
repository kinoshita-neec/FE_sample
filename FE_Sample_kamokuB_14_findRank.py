# FEサンプル問題14 関数内で関数を呼び出す

# 配列sortedDataから代表数値を取り出す
# 代表値=（配列p[0,0.25,0.5,0.75,1]の各数値
#          ＝最少値、1/4、半分、3/4、最大値に最も近い数値）

import math

def findRank(sortedData,p):
    i = math.ceil(p * (len(sortedData) - 1))
    return sortedData[i]

def summarize(sortedData):
    rankData = []
    p = [0,0.25,0.5,0.75,1]

    for i in range(0,len(p)): #配列番号修正
        rankData.append(findRank(sortedData,p[i]))
    return rankData


# print(summarize([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]))
sortedData = list(map(float,input("昇順の数値配列をカンマ区切りで入力→",).split(",")))
print(summarize(sortedData))