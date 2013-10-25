__author__ = 'jasonfungsing'

def dutchNationalFlag(inputArray, pivotIndex):
    size = len(inputArray)
    small = 0
    equal = 0
    large = size - 1

    pivot = inputArray[pivotIndex]
    while equal < large:
        print("now the array is: " + str(inputArray))
        if inputArray[equal] < pivot:
            inputArray[small], inputArray[equal] = inputArray[equal], inputArray[small]
            small += 1
            equal += 1
        elif inputArray[equal] == pivot:
            equal += 1
        else:
            inputArray[large], inputArray[equal] = inputArray[equal], inputArray[large]
            large -= 1

    return inputArray



print(dutchNationalFlag([2,4,3,1,6,5,7], 1))


