class Words:
    def __init__(self):
        # 英単語を入れる配列
        self.words = []
        
    # words配列に英単語を追加する
    def add_word(self, word):
        self.words.append(word)
    
    # 英単語群中のalphabetの出現回数を返す
    def freq(self, alphabet: str) -> int:
        # アルファベットの出現回数
        count = 0
        # words配列をループする
        for word in self.words:
            print(word,self.words)
            # 英単語の文字数を取得する
            count += word.count(alphabet)
        return count
            
    
    # 英単語群の中で，文字列strで終わる英単語の数を数える
    def freqE(self, alphabet: str) -> int:
        count = 0
        for word in self.words:
            if (word.endswith(alphabet)):
                count += 1
        return count
        
    # c1の次にc2が出現する割合を返す
    def prob(self, c1: str, c2: str) -> int:
        s1 = c1
        s2 = c2
    
        # コード一部改変
        if (self.freq(s1 + s2) > 0): # words.freq(s1 + s2) > 0
          return self.freq(s1 + s2) / (self.freq(s1) - self.freqE(s1)) # words.freq(s1 + s2) / (words.freq(s1) - words.freqE(s1))
        else:
            return 0
        
word_list = Words()
# 配列に英単語を入れる
word_list.add_word("importance")
word_list.add_word("inflation")
word_list.add_word("information")
word_list.add_word("innovation")
print(word_list.words)

# c1とc2の値を指定
c1 = "n"
c2 = "f"

print(word_list.prob(c1, c2))