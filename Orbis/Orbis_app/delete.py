with open('newfile.txt', 'w', encoding='utf-8') as g:
    d = int(input())
    g.write("!")
    print('1 / {} = {}'.format(d, 1 / d), file=g)
    g.write("!!!")
