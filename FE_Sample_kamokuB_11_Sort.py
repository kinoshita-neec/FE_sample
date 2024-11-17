# FE　サンプル問題11
# 与えられた数列の値aをa番目に格納していく

# 実装に当たる変更
# 配列番号がずれるため、要素数nはn+1とし、for条件としては元に戻す（n-1）

def binSort(data:list):
    n=len(data)+1
    bins=[None]*n
    print("data",data,"n",n,"bins",bins)

    for i in range(0,n-1):
       print("i",i,"data[i]",data[i],"bins",bins)       
       bins[data[i]]=data[i] 
    return bins

data=list(map(int, input("スペース区切りで数字を入力→",).split()))
print(binSort(data))
