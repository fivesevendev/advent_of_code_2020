import timeit, sys, time


def parser(n, o):
    with open(n) as unParsed:
        parsed = unParsed.read()
    parsed = str(parsed.split(sep=" "))
    parsed = parsed.replace("\\n", """'], ['""")
    parsed = '''data = [{}]'''.format(parsed)
    with open(o, mode='w') as output:
        output.write(parsed)
    return parsed


if __name__ == '__main__':
    startTime = timeit.default_timer()
    print(time.asctime())
    print()
    n = "input.txt"
    o = "output.txt"
    print(parser(n, o))
    print()
    print("Run Time Was {:.4F} Seconds".format(timeit.default_timer() - startTime))