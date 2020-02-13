class QuickUnionUF:
    '''Python better implementation of union-find algortihm
    '''

    def __init__(self, num=0):
        self.num = num
        self.id = [i for i in range(num)]

    def setNum(self, num):
        self.num = num
        self.id = [i for i in range(num)]

    def __root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        i = self.__root(p)
        j = self.__root(q)
        self.id[i] = j

class QuickUnionUFModification:
    def __init__(self,num=0):
        self.num = num
        self.id = [i for i in range(num)]
        self.rootID = [1]*num


