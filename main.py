
n = int(input('write the number of rows : '))

while True:
    a = int(input('write 0 for increasing order and 1 for decreasing order : '))
    while a == 0:
        for i in range(n):
            for j in range(i+1):
                print('*', end=' ')
            print()

        break
    while a == 1:
        for i in range(n):
            for j in range(i,n):
                print('*',end=' ')
            for k in range(i+1):
                print(' ',end=' ')
            print()
        break

