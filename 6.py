def main(x):
    ans = {'JSX': {2002: {'HTML': {'QMAKE': 0,
                                   'XTEND': 1,
                                   },
                          'OPAL': 2,
                          'GOSU': 3
                          },
                   2013: {'QMAKE': 4,
                          'XTEND': 5
                          },
                   1977: 6
                   },
           'LOGOS': {2002: {'HTML': {'QMAKE': 7,
                                     'XTEND': 8
                                     },
                            'OPAL': 9,
                            'GOSU': 10
                            },
                     2013: 11,
                     1977: 12
                     }
           }
    i = ans
    while type(i) != int:
        for j in range(len(x)):
            if x[j] in i.keys():
                i = i[x[j]]
                break
    return i


if __name__ == '__main__':
    print(main(['XTEND', 2002, 'HTML', 1991, 'LOGOS']))
