import math
t={}
c=0
for _ in range(int(input())):
    x,y,v=list(map(int,input().split()))
    r=math.sqrt(((x/v)**2 +((y/v)**2)))
    if(t.get(r)==None):
        t[r]=1
    else:
        t[r]+=1
for i in t:
    if(t[i]!=1):
        c+=(t[i]*(t[i]-1))/2
print(int(c))
"""
5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2
"""