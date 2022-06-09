import math


def main(n):
    if n == 0:
        return -0.24
    elif n >= 1:
        return main(n - 1) + 3 * main(n - 1) ** 2 + main(n - 1) ** 3


if __name__ == '__main__':
    print(main(2))
