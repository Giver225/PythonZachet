import math


def main(x, z, y):
    return ((y + 1 + x ** 3) ** 6 / 29 - z ** 15) / \
           (66 * (y ** 2 + x + 38 * z ** 3) ** 5) - math.sqrt(
        math.fabs(y) ** 2 + (x - z ** 2 / 23) ** 4)


if __name__ == '__main__':
    print(main(0.74, 0.13, -0.56))
