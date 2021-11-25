#The first half of the asterix pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()
#The second half of the asterix pattern
n = 4
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()
