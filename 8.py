def main(row):
    ans = {}
    row = row.replace('\n', ' ')
    row = row.replace('section', '')
    row = row.replace('>', '')
    row = row.replace('<', '')
    row = row.replace('/', '')
    row = row.replace('((', '')
    row = row.replace('def ', '')
    row = row.replace(')', '')
    row = row.replace('|', '')
    row = row.replace(' ', '')
    row = row.split('.')
    row.pop()
    for i in row:
        i = i.split('q(')
        ans |= {i[0]: i[1]}
    return ans


if __name__ == '__main__':
    print(main('''<section> (( def onge <| q(diraus_802). )) ((def tiququ <|
q(sousra).)) </section>'''))
