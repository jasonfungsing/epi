__author__ = 'jasonfungsing'


def parity(a):
    totalNumberOfOne = 0;
    while(a):
        last = a & 1 # get the right most bit
        if last==1:
            totalNumberOfOne = totalNumberOfOne +1
        a = a >> 1

    return totalNumberOfOne % 2



print(str(parity(5)))