def main(x):
    e = (0xF0000000 & x) >> 7
    d = (0x08000000 & x) >> 18
    c = (0x07F00000 & x) << 5
    b = (0x000FFE00 & x) << 1
    a = (0x000001FF & x)
    return c | b | a | d | e


if __name__ == '__main__':
    print(hex(main(0x07d86c0a)))
