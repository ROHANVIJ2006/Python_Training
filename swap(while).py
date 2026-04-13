l1=[10,20,30,40]
s=0
e=len(l1)-1
while s<=e:
    t=l1[s]
    l1[s]=l1[e]
    l1[e]=t
    s+=1
    e-=1
print(l1)
