# FEサンプル問題10

# 単方向リストの要素(valだけ受け取って、後でリンクさせる)
class ListElement:
    def __init__(self,i_val):
        # メンバ変数vlaとnextの宣言
        self.val=i_val
        self.next=None

# エレメントを作る
Le1 = ListElement("あ")
Le2 = ListElement("い")
Le3 = ListElement("う")
Le4 = ListElement("え")
Le5 = ListElement("お")
Le6 = ListElement("か")

# 連結する
Le1.next = Le2
Le2.next = Le3
Le3.next = Le4
Le4.next = Le5
Le5.next = Le6

# ListHeadの設定
ListHead = Le1

# 削除するメソッド
def delNode(pos:int):
    prev:ListElement
    if pos == 1:
        global ListHead # 大域変数の更新
        ListHead = ListHead.next
    else:
        prev = ListHead
        #posが2と等しいときは繰り返しを実行しない
        for i in range( 2, pos ): #rage(始点,終点-1)なのでpos-1まで
            prev = prev.next
        prev.next = prev.next.next



#print(f'削除前 LH={"val=", ListHead.val,"next.val=", ListHead.next.val}、\n Le1={"val=", Le1.val,"next.val=", Le1.next.val}、\n Le2={"val=", Le2.val,"next.val=", Le2.next.val}、\n Le3={"val=", Le3.val,"next.val=", Le3.next.val}、\n Le4={"val=", Le4.val,"next.val=", Le4.next.val}')
print(f'削除前 {ListHead.val,ListHead.next.val,ListHead.next.next.val,ListHead.next.next.next.val,ListHead.next.next.next.next.val,}' )
EraseIndex = int(input("削除する番号"),)
delNode(EraseIndex)
#print(f'削除前 LH={"val=", ListHead.val,"next.val=", ListHead.next.val}、\n Le1={"val=", Le1.val,"next.val=", Le1.next.val}、\n Le2={"val=", Le2.val,"next.val=", Le2.next.val}、\n Le3={"val=", Le3.val,"next.val=", Le3.next.val}、\n Le4={"val=", Le4.val,"next.val=", Le4.next.val}')
print(f'削除前 {ListHead.val,ListHead.next.val,ListHead.next.next.val,ListHead.next.next.next.val,ListHead.next.next.next.next.val,}' )



"""
リスト構造をクラスを使って実装する場合、
通常はリスト要素を作るクラス（今回のListElementクラス）の他に
リスト要素を追加したり削除したりするクラス（LinkedListクラスなど）を
用意し、追加・削除などの手続きをクラスメソッドとして設定する。


class LinkedList:
    def __init__(self):  # 連結リストの初期化
        self.head = ListHead  # 最初のノードへの参照
    # リストの最後に要素を追加するメソッド
    def addNode(self,nex):  # リストの最後に要素を追加するメソッド
        new_node = ListElement(valu,nex)  # 新しいノードを作成
        if self.head.valu == None:  # リストが空の場合
            self.head = new_node  # リストの先頭に新しいノードを追加
            return  # メソッドを終了
        current = self.head  # リストの先頭を current とする
        while current.next:  # current が最後のノードでない限り
            current = current.next  # current を次のノードに更新
        current.next = new_node  # 最後のノードの次に新しいノードを追加

    # リストの要素を表示するメソッド
    def display(self):  # リストの要素を表示するメソッド
        current = self.head  # リストの先頭を current とする
        while current:  # current が None になるまで
            print(current.data, end=" -> ")  # current のデータを表示
            current = current.next  # current を次のノードに更新
        print("None")  # None を表示


# 連結リストを作成
tex = str(input("リストエレメントに入れる文字",))
nex = str(input("リストエレメントに入れる文字",))
my_linked_list = ListElement(tex)
my_linked_list.addNode()

# 削除前の連結リストを表示
print("削除前:")
my_linked_list.display()
    # リストの要素を削除するメソッド
    def remove(self, node_to_remove):  # リストの要素を削除するメソッド
        if not node_to_remove:  # 削除するノードがない場合
            return  # メソッドを終了

        if node_to_remove.next:
            # 次のノードがある場合、次のノードのデータを現在のノードにコピーし、次のノードを削除
            node_to_remove.data = node_to_remove.next.data  # 次のノードのデータを現在のノードにコピー
            node_to_remove.next = node_to_remove.next.next  # 次のノードを削除
        else:
            # 次のノードがない場合、現在のノードを単純に削除
            current = self.head  # リストの先頭を current とする
            prev = None  # current の前のノードを None とする

def delNode(pos):
    ListElement=prev

    if pos == 1:
        ListHead=ListHead.next
    else:
        prev = ListHead

        for i in range(2,pos-1):
            prev=prev.next

        prev.next=prev.next.next

"""
