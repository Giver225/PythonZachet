import struct

offset = 4


def find(adress, size, unpack, data):
    global offset
    s = data[adress - offset:adress - offset + size]
    s = struct.unpack(unpack, s)
    return s


def main(data):
    ans = {}
    data1 = data[offset:]
    a = 71
    b = 42
    c = 12
    d = 27
    a_str = find(offset, a, '<q8cQQdIIHfffBQ', data1)
    ans |= {'A1': a_str[0],
            'A2': (a_str[1] +
                   a_str[2] +
                   a_str[3] +
                   a_str[4] +
                   a_str[5] +
                   a_str[6] +
                   a_str[7] +
                   a_str[8]).decode('utf-8'),
            'A3': a_str[9],
            'A4': a_str[10],
            'A5': a_str[11]
            }
    b_str = find(a_str[12], b, '<fIIfIIQQH', data1)
    ans['A6'] = {'B1': [{'C1': b_str[0],
                         'C2': list(find(b_str[2],
                                         b_str[1] * 2,
                                         f'<{b_str[1]}H',
                                         data1))},
                        {'C1': b_str[3],
                         'C2': list(find(b_str[5],
                                         b_str[4] * 2,
                                         f'<{b_str[4]}H',
                                         data1))}],
                 'B2': b_str[6],
                 'B3': b_str[7],
                 'B4': b_str[8]
                 }
    ans['A7'] = {'D1': list(find(a_str[14],
                                 a_str[13] * 8,
                                 f'<{a_str[13]}q',
                                 data1)),
                 'D2': a_str[15],
                 'D3': a_str[16],
                 'D4': a_str[17],
                 'D5': a_str[18],
                 'D6': a_str[19]}
    return ans


if __name__ == '__main__':
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(main(b'TFQS\xca\xc39\xba\xbe\x95\xf9\xd6mzmcladf\xc3`\xc0d\xe6\x04\xec\xc6'
                   b'\xe3\xc7-\x15\x93\x1f8\xf6Z\xe0 \xd3E\x88\xe4?W\x00\x00\x00\x05\x00\x00\x00'
                   b'\x81\x00\xf118\xbf\x97\x0ey?MA\x01>y-qa\x1eg\xcbE\xad\x16P\xdam\xd5'
                   b"o\xd6\xf5T\x07U&\x1a,'\xbf\x03\x00\x00\x00K\x00\x00\x00aJ2\xbf\x03"
                   b'\x00\x00\x00Q\x00\x00\x00bMZ$\x90p\xf9\x16\x08\r9\x0f:\xebO\xec\xa7y{\xf1;'
                   b'\xc2\xa3\xbd\xf5X\x99\x93Q\xa9{\xab\xf9\x80X\x85\xce\xd8\xa0Ug\x18\x19\x0eN'
                   b'l\xb4m\xa3\xaa\xad\x8a\xa1M\xd7\xcbg9'))
