#FEサンプル問題'22公開　問5
"""
問題文の例
単語群
 importance
 inflation
 information
 innovation
 c1="n" c2="f" の時 「2÷5=0.4」である。一般化すると・・・
  「 "c1" の次に "c2" が来る回数 / ("c1" の個数 - 末尾の"c1"の個数) 」

分母をクラスwordのメソッドを使って表すと
  (freq(c1) - freqE(c1)) 
  ⇒c1,c2はprob関数内ではs1、s2なので選択肢はウとなる

念のため分子も確認する
 "c1" の次に "c2" が来る回数 = "c1c2"がある個数
  ⇒words.freq(s1+s2)で正しい
"""
# 変数の整理
# クラス名　Words
# メンバ変数 配列word_list
# 

class Words:
    def __init__(self):
        self.word_list = []

    def freq(self,chara) -> int:
        count = 0
        for word in self.word_list:
            count += word.count(chara)
        return count

    def freqE(self,chara) -> int:
        count = 0
        for word in self.word_list:
            if chara == word[-1]:
                count += 1
        return count

    # 単語追加メソッド
    def add_word(self,word):
        self.word_list.append(word)

def prob(c1,c2):
    s1 = c1
    s2 = c2
    if words.freq( s1 + s2 ) > 0:
        return words.freq(s1 + s2) / (words.freq(s1) - words.freqE(s1))
    else:
        return 0

words = Words()
words.add_word("importance")
words.add_word("inflation")
words.add_word("information")
words.add_word("innovation")

#c1 = "n"
#c2 = "f"

print(words.word_list)
c1 = str(input("c1を指定：",))
c2 = str(input("c2を指定：",))
print(c1,"-",c2,"並びの出現割合：",prob(c1,c2))
