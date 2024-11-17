# FEサンプル問題16 Unicode
# Unicode符号→UTF-8符号に変換するプログラム
#　
#　問題文中の例がヒントとなる
#　”あ”　3042(16)       11 000001 000010
#  3つ目の要素のx部分　　　　　     000010
#  2つ目の要素のx部分       000001
#  1つ目の要素のx部分  xx11　
#  3つ目、2つ目の処理はcodePointから下6ビットを取り出す処理をすればいい
#  ⇒2^6 = 64 で割った余りを取っていけばよい



def encode(codePoint):
    utf8Bytes=[224,128,128]
    cp=codePoint
    for i in range(len(utf8Bytes)-1,0,-1):
        utf8Bytes[i] = utf8Bytes[i] + cp % 64
        cp = cp//64
    return utf8Bytes

u_code=input("Unicode符号（0x800～0xFFFF）:",)
codePoint=int(u_code,16)

print(encode(codePoint))

# ↓確認用
# print("Unicode符号(10進数):",codePoint,"文字：",chr(codePoint))
# print("utf-8符号(encode(codePoint)):",encode(codePoint),"16進数:",[format(i,'02x') for i in encode(codePoint)])

# 0x0800～0xFFFFはベンガル文字、タイ文字、チベット文字など
# 例:タイ文字子音ก[k]　Unicode 0x0E01 →　utf-8 E0 B8 80
# https://orange-factory.com/sample/utf8/code3/e0.html#Thai
# https://0g0.org/
