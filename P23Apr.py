r=2*11
c=33
e=(c-7)/2
e=int(e)
l=(r/2)+1
l=int(l)
for i in range(1, l, 2):
    p=i*3
    count=(c-p)/2
    count=int(count)
    for j in range(0, count):
        print('-', end='')
    for k in range(0, i):
        if (i==l-1):
            for w in range(0, e):
                print('-', end='')
            print('WELCOME', end='')
            for w in range(0, e):
                print('-', end='')
            break
        print('.|.', end='')
    for j in range(0, count):
        print('-', end='')
    print('')

for i in range(l-3, 0, -2):
    p=i*3
    count=(c-p)/2
    count=int(count)
    for j in range(0, count):
        print('-', end='')
    for k in range(0, i):
        print('.|.', end='')
    for j in range(0, count):
        print('-', end='')
    print('')
