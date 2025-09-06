array = [67, 41, 93, 6, 20, 55, 3]
largest = array[0]
second = 0

for x in range(1, len(array)):
    if largest > array[x]:
        second = array[x]
    else:
        largest = array[x]
        second = array[x-1]

print("The second largest is: " + str(second))
