array = [6, 7, 4, 1, 3, 2, 8, 9, 10, 5]

def sumElements():
    total = 0
    for i in range(10):
        total = total + array[i]

    return total

def maxMin():
    maximum = array[0]
    minimum = array[0]

    for i in range(1, 10):
        if array[i] > maximum:
            maximum = array[i]
        if array[i] < minimum:
            minimum = array[i]

    return [maximum, minimum]
