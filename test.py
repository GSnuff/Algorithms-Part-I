import QuickUnionUF
import QuickUnionModification as qum
import QuickUnionUF

test1 = qum.QuickUnionUFModification(10)
print(test1.id)

test1.union(5, 2)
print("First un")
print(test1.id)

test1.union(3, 4)
print("Second un")
print(test1.id)

test1.union(4, 6)
print("Third un")
print(test1.id)

test1.union(5, 6)
print("Fourth un")
print(test1.id)

test2 = qum.QuickUnionUFModification(10000)

print(test2.id)

for i in range(1000):
    test2.union(i, i + 1)

print(test2.id)

print(test2.connected(2, 5))
