with open('coffey tabel book.txt', 'r') as w:
    data = w.read()
arry = data.split('\n')
print(arry)
with open('data.txt', 'w') as w:
    for ok in arry:
        if ok == '':
            ok = ok + '\n'
        if ok[-1]=='=':
            ok = '\n'+ok + '\n'

        w.write(ok)
