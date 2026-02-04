'''nums=[0,1,0,3,12]
j = 0  # index for non-zero placement
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
print(nums)'''
'''r=range(10)
r=iter(r)
while True:
    try:
        d=next(r)
        print(d)
    except StopIteration:
        break'''

def fib(n):
    a, b = 0, 1

    while n:
        print(a, end=" ")
        a, b = b, a + b
        n -= 1
fib(10)
