def rsrt(a, b):
    for i in range(len(b)):
        r = a.count(b[i])
        for j in range(r):
            print(b[i], end=' ')
            a.remove(b[i])
    a.sort()
    for i in range(len(a)):
        print(a[i], end=' ')

    print()


for i in range(int(input())):
    n, m = map(int, input().rstrip().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    rsrt(a, b)