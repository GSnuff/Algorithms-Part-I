# Quick Find algorithm


class QuickFindUF:
    '''Python's (not the best) implementation of union-find algorithm.
    '''

    def __init__(self, num=0):
        self.num = num
        self.id = [i for i in range(num)]

    def setVal(self, num):
        self.num = num
        self.id = [i for i in range(num)]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.num):
            if self.id[i] == pid:
                self.id[i] = qid
