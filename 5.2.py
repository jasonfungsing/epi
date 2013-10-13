__author__ = 'jasonfungsing'


def swap(x, i, j):
    print("bin for " + str(x) + " is: " + bin(x))
    iposition = (x >> i) & 1
    print("position i is: " + str(iposition))
    jposition = (x >> j) & 1
    print("position j is: " + str(jposition))
    if iposition != jposition:
        x = x ^ (1 << i)
        x = x ^ (1 << j)
    return x

print(swap(5,1,2))