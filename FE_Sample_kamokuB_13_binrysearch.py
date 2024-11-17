# FEサンプル問題13 二分探索
# ⓵中央値[middle]と目的値targetを比較する
# [middle]<target なら後半部分を対象に⓵
# [middle]>target なら前半部分を対象に⓵
# 本来、low、heighの更新時にmiddleを外す（＝middle+1,middle-1）
# ウ　要素数2でtarget==data[2]
#　　⇒low 1 height 2 middle 1 data[middle]< target
#　　⇒lowに1が入り続ける


def search(data,target):
    low = 0
    heigh = len(data)-1

    while low <= heigh:
        middle = (low + heigh) // 2
        print("data",data,"low",low,"heigh",heigh,"middle",middle,"target",target)
        if data[middle] < target:
            low = middle #本来はmddle+1
        elif data[middle] > target:
            heigh = middle #本来はmddle-1
        else:
            return middle+1 #配列番号を1からに合わせる
        
    return -1

data = list(map(int,input("dataをスペース区切りで入力→",).split()))
target = int(input("targetを入力→"))
print(search(data,target))
