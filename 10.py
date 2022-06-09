def f(lul):
    n = []
    for i in lul:
        if i not in n and i[-1] is not None:
            n.append(i)
    return n


# можно оптимизировать
def trans(matrix):
    trans_matrix = [[0 for j in range(len(matrix))]
                    for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def main(matrix):
    matrix = f(matrix)
    trans_matrix = trans(matrix)
    trans_matrix = f(trans_matrix)
    matrix = trans(trans_matrix)
    for i in matrix:
        i[0] = i[0].replace('/', '.')
        i.append(i[0].split(':')[0])
        if i[0].split(':')[1] == '1':
            i[0] = 'да'
        elif i[0].split(':')[1] == '0':
            i[0] = 'нет'
        i[-1] = i[-1][:6] + i[-1][8:]
        i[1] = i[1].split('.')
        i[1][0] = i[1][0][:-2]
        i[1][1] = i[1][1][1:]
        i[1] = i[1][1] + ' ' + i[1][0]
    matrix.sort(key=lambda x: x[1])
    return matrix


if __name__ == '__main__':
    print(main(
        [[None, '11/06/2004:1', 'Руслан Е. Дудифян', None, 'Руслан Е. Дудифян'],
         [None, '03/07/1999:0', 'Илья Т. Чамук', None, 'Илья Т. Чамук'],
         [None, '15/07/2000:1', 'Демид И. Ритезко', None, 'Демид И. Ритезко'],
         [None, '03/01/2004:1', 'Одиссей Ч. Гилелий', None, 'Одиссей Ч. Гилелий']]
    ))
