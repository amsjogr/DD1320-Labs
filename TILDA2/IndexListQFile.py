class IndexlistQ:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def basictest():
    q = IndexlistQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()

    # Förväntat resultat
    if (x == 1 and y == 2 and q.isEmpty()):
        print("test OK")
    else:
        print("FAILED expected x=1 and y=2 and an empty list but got x =", x, " y =", y, " and empty list is", q.isEmpty())


#if __name__ == "__main__":
#    basictest()