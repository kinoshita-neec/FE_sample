#FEサンプル問題'22公開　2

array = [1,2,3,4,5]
#array = list(map(int,input("配列をスペース区切りで入力：",).split()))


for left in range(0,(len(array))//2):#疑似言語ではrange(1,(len(array)//2)
    right = len(array)-left-1 #疑似言語ではlen(array)-left+1
    tmp = array[right]
    array[right]=array[left]
    array[left] = tmp

print(array)

