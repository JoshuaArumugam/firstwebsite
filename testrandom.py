import random

def TestRandom():
    results = [0] * 10

    for i in range(200):
        randomNumber = random.randint(1, 10)
        results[randomNumber - 1] = results[randomNumber - 1] + 1

    print("The expected frequency is 20.")
    print("Number \t Frequency \t Difference")

    for i in range(10):
        print(i + 1, "\t", results[i], "\t\t", results[i] - 20)

TestRandom()
