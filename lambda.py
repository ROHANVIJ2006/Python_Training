'''add = lambda a, b: a + b
print(add(40, 60))

print((lambda a, b: a + b)(10, 20))

fact = lambda n: n * fact(n - 1) if n > 0 else 1
print(fact(6))
'''

l=[1,2,3,4,5]
'''ans=map(lambda x: x ** 2, l)
for x in ans:
    print(x)
print(ans)
'''

# from functools import reduce
# print(reduce(lambda x, y: x * y, l))

an=list(filter(lambda x: not(x % 2), l))
print(an)