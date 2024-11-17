num = int(input())

#n-1    0     1     2     3      4       5      6  7  8  9  10 11 12 13
tree=[[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14],[],[],[],[],[],[],[]]


def order(n:int):
    print("n-1=",n-1,end="  ->  ")
    
    if len(tree[n-1]) == 2:
        print("order(tree[",n-1,"][0]) = order(",tree[n-1][0],")")
        order(tree[n-1][0])
        print("要素数２でAns=",n)
        print("order(tree[",n-1,"][1]) = order(",tree[n-1][0],")")
        order(tree[n-1][1])

    elif len(tree[n-1]) == 1:
        print("order(tree[",n-1,"][0]) = order(",tree[n-1][0],")")
        order(tree[n-1][0])
        print("要素数１でAns=",n)

    else:
        print("要素数０でAns=",n)

order(num)    
"""
深さ優先探索中間順の探索順路をたどっている
配列n行目の要素の数が２なら、その行の一個目の要素に格納された数字を返す
の行に移動
"""

