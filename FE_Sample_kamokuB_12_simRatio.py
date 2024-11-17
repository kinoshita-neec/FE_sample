# FEサンプル問題12
s1 = ["a","p","p","l","e"]
# s2 = ["a","p","p","l","e"]

def simRatio(s1,s2):
    i,cnt = 0,0
    if len(s1) != len(s2):
        return -1
    
    for i in range(0,len(s1)):
        if s1[i] == s2[i]:
            cnt = cnt + 1
    
    return cnt / len(s1)

s2 = list(map(str,input("s2をスペース区切りで入力→",).split()))
print(simRatio(s1,s2))
