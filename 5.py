import math


def main(x):
    n = len(x)
    s = 0
    x.insert(0, 0)
    for i in range(1, n + 1):
        s += 78 * (math.fabs(x[n+1-math.ceil(i/3)])**3)
    return 91 * s


if __name__ == '__main__':
    print(main([-0.36, 0.18]))
