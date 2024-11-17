#キューモジュールのインポート
import queue

class PrioQueue:
    #コンストラクタ
    def __init__(self):
        self.queue = queue.PriorityQueue()

    #エンキューメソッド（put）の定義
    def enqueue(self, s:str, prio:int):
        self.queue.put((prio,s))

    #デキューメソッド（get）
    def dequeue(self):
        if self != None:
            return self.queue.get()[1]

    def size(self):
        return self.queue.qsize()


def prioSched():
    #インスタンスの作成
    prioQueue=PrioQueue()

    #データのPOST,GET
    prioQueue.enqueue("A",1)
    prioQueue.enqueue("b",2)
    prioQueue.enqueue("C",2)
    prioQueue.enqueue("D",3)
    prioQueue.dequeue()
    prioQueue.dequeue()
    prioQueue.enqueue("D",3)
    prioQueue.enqueue("B",2)
    prioQueue.dequeue()
    prioQueue.dequeue()
    prioQueue.enqueue("C",2)
    prioQueue.enqueue("A",1)

    #キューが空になるまでデキューする
    while (prioQueue.size() != 0):
        print(prioQueue.dequeue())

prioSched()  
