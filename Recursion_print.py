'''def fun1(n):
    if n == 0:
        return 1
    if n==1:
        return 1
    else:
        return n*fun1(n-1)

print(fun1(5))'''

'''def print1(n):
    if n > 0:
        print(n, end='')
        return print1(n-1)

print1(5)'''

'''def print1(n):
    if n > 0:
        return print1(n-1)
        print(n, end='')
print1(5)'''

def fibonacci(n):
    if n == 1 or n == 2:
        return n-1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))

