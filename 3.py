import math


def main(n, b):
    s1 = 0
    for c in range(1, b + 1):
        s2 = 0
        for k in range(1, n + 1):
            s2 += 1 + 64 * (k ** 3 / 35 - c ** 2 / 54)
        s1 += s2
    s3 = 0
    for j in range(1, n + 1):
        s3 += j ** 2 - j ** 3 - j ** 4 / 16
    return s1 + s3


if __name__ == '__main__':
    print(main(5, 4))
