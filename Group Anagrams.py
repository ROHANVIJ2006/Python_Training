'''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(word)

        return list(anagrams.values())


d={}
for data in str:
    temp=sorted(data)
    if temp in d:
        d[temp]=d[temp].append(data)
        else:
        d[temp]=[data]
return [d.values()]'''


'''
num = [1, 2, 3, 4, 5, 6]

def f1(num):
    for i in num:
        if i % 2 == 0:
            num.remove(i)
    print(num)

f1(num)'''
'''
def f2(**data):
    for i in data:
        print(i)
f2(x=10, y=20)'''

class Node:
    def __init__(self, data):
        self.data = data
    obj=Node()
