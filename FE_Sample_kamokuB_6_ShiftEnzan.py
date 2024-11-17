# FEサンプル問題6　シフト演算、ビットの並びを逆にする
# 問題文の例
# rev(01001011)
#   r(11010010)

byte=0b01001011

def rev(byte):
    rbyte = byte
    r = 0b00000000
    # print("i","処理前r ","処理前rbyte","(rbyte&00000001)","処理後のr","処理後rbyte")

    for i in range(1,9):
        # print(i,format(r ,'08b'),format(rbyte,'08b'),"   ",format(rbyte&0b00000001,'08b'),end="        ")
        r = (r << 1) | (rbyte & 0b00000001)
        rbyte = rbyte >> 1
        # print(format(r,'08b'),format(rbyte,'08b'))  
    return format(r,'08b')

print(rev(byte))

"""
各変数のビットを以下のように考える
byte {a8,a7,a6,a5,a4,a3,a2,a1}
rbyte{a8,a7,a6,a5,a4,a3,a2,a1}
r    {r1,r2,r3,r4,r5,r6,r7,r8} ← {0,0,0,0,0,0,0,0}


ア r ← ( r << 1 ) or ( rbyte and 00000001)
   rbyte ← rbyte >> 1

    一行目
        左辺 r{r2,r3,r4,r5,r6,r7,r8,0}→末尾に0を作っている
        右辺 
           rbyte {a8,a7,a6,a5,a4,a3,a2,a1}
        and      { 0, 0, 0, 0, 0, 0, 0, 1}
                ={ 0, 0, 0, 0, 0, 0, 0,a1}→末尾のa1を取り出した

        左辺⋁右辺
          左辺{r2,r3,r4,r5,r6,r7,r8, 0}
        or右辺{ 0, 0, 0, 0, 0, 0, 0,a1}
             ={r2,r3,r4,r5,r6,r7,r8,a1}→a1を末尾に格納した

    二行目
        rbyteを右シフト演算
        rbyte { 0,a8,a7,a6,a5,a4,a3,a2}→今度はa2を取り出す


※選択肢はすべて、一行目rの更新、二行目rbyteの更新になっており、
※当て勘として、初期状態byte、中間状態rbyte、　最終状態rと推定できれば、
　iを1ずつ増やして処理する場合、rbyteに対して<<7(=7bit捨てる)のような演算は入りにくい
"""

    
