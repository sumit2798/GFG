n=int(input())
s=list(input())
t=list(input())
count=0
for i in s:
    if( i in t):
        t.remove(i)
    else:
        break
print(len(t))
