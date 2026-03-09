from math import factorial

def trangle(n=5):
    for i in range(n):
        print(' '*(n - i - 1),end='')

        if i == 0:
            print('*')
        elif i == n - 1:
            print('*' * (2 * n - 1))
        else:
            print('*' + ' ' * (2 * i -1) + '*')
    
trangle(5)

# input n
n = 5
for i in range(n):
    for j in range(n-i+1):

        # for left spacing
        print(end=" ")

    for j in range(i+1):

        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # for new line
    print()