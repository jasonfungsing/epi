__author__ = 'jasonfungsing'


def dutchNationalFlag(inputArray, pivotIndex):
    size = len(inputArray)
    small = 0
    equal = 0
    large = size - 1

    pivot = inputArray[pivotIndex]
    print("the pivot is: " + str(pivot))
    while equal < large:
        current = inputArray[equal]
        print("the array is: " + str(inputArray))
        print("start process: " + str(current))
        if current < pivot:
            inputArray[small], inputArray[equal] = inputArray[equal], inputArray[small]
            small += 1
            equal += 1
        elif current == pivot:
            equal += 1
        else:
            inputArray[large], inputArray[equal] = inputArray[equal], inputArray[large]
            large -= 1
        print("after process " + str(current) + ",  now array is: " + str(inputArray))

    return inputArray


print(dutchNationalFlag([2, 4, 3, 1, 6, 5, 7], 1))


