import time

seed = 1


def lcg():
    a = 1103515245
    c = 12345
    m = 2147483648

    global seed
    seed = (seed * a + c) % m
    return seed


if __name__ == "__main__":
    seed = int(time.time())
    while True:
        print(lcg() % 37)
        input()
