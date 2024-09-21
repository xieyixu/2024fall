import math
def function(n):
    a=math.log(n,2)
    if a.is_integer():
        return True
    else:
        return False

n=int(input())
numbers=[int(input()) for _ in range(n)]

j=0
for number in numbers:
    s=0
    for j in range(1,number+1):
        if function(j):
            s-=j
        else:
            s+=j
    print(s)