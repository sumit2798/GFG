def groovingmonkeys(a,n):
    c=0
    for i in range(1,m):
      if(a[i]==i):
        c+=1
    return c
if __name__=="__main__":
    for i in range(int(input())):
        num=int(input())
        mon=list(map(int,input().split()))
        b=[i for i in range(1,num)]
        d={}
        print(groovingmonkeys(mon))