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

n = 10
a = 0
b = 1
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()

# Function for nth Fibonacci number
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(10))