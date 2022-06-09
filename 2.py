import math


def main(z):
    if z < 72:
        return z ** 6 - z ** 2 - math.log10(z) ** 3
    elif 72 <= z < 130:
        return 1 + z ** 6
    elif z >= 130:
        return math.atan(z) ** 4 + 1 + (1 + z ** 3 / 23) ** 2


if __name__ == '__main__':
    print(main(155))
