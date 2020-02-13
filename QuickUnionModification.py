class QuickUnionUFModification:
    def __init__(self, num=0):
        self.num = num
        self.id = [i for i in range(num)]
        self.sz = [0] * num

    def __root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        i = self.__root(p)
        j = self.__root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
