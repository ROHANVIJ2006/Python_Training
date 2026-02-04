def max_subarray(n):
    sum = 0
    mv = n[0]
    n = [5, 4, -1, 7, 8]
    for v in n:
        sum+=v
        mv=max(mv,sum)
        if sum<0:
            sum=0
    return mv