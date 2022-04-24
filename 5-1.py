#AOC-2020-


import timeit, sys, time


testData = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

data = []


def numFind(n):
    for row in range(0, len(n)):
        print(n[row])
        for col in range(0, len(n[row])):
            print(n[row][col])


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print("\n>>>>>", time.asctime(), "<<<<<")
    n = testData
    print("Result:", numFind(n))
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))
    print(">>>>>", time.asctime(), "<<<<<")