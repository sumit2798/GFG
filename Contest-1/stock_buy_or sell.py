def stockBuySell(price, n):
    s = ""
    if (n == 1):
        return
    sol = []
    i = 0
    cnt = 0
    while (i < n - 1):
        # Find Local Minima. Note that the limit is (n-2) as we are
        # comparing present element to the next element.

        while ((i < n - 1) and (price[i + 1] <= price[i])):
            i = i + 1

        # If we reached the end, break as no further solution possible

        if (i == n - 1):
            break
        e = [0, 0]  # e[0] denotes buy , e[1] denotes sell
        e[0] = i
        i = i + 1

        # Find Local Maxima.  Note that the limit is (n-1) as we are
        # comparing to previous element

        while ((i < n) and price[i] >= price[i - 1]):
            i = i + 1
        e[1] = i - 1
        sol.append([e[0], e[1]])

        # Increment count of buy/sell pairs

        cnt = cnt + 1
    if (cnt == 0):
        s = "No Profit"
    else:
        s = ""
        for i in sol:
            s1 = "(" + str(i[0]) + " " + str(i[1]) + ")"
            s = s + s1
            s = s + " "
    print(s)
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(stockBuySell(arr,n))
    """
    5
7
100 180 260 310 40 535 695
10
23 13 25 29 33 19 34 45 65 67
5
4 2 2 2 4
5
5 5 5 5 5
9
57 69 12 59 5 9 29 29 99

Output:
(0 3) (4 6)
(1 4) (5 9)
(3 4)
No Profit
(0 1) (2 3) (4 8)

Explanation:
Testcase 1: We can buy stock on day 0, and sell it on 3rd day, which will give us maximum profit. 
Now, we buy stock on day 4 and sell it on day 6.
Testcase 2: We can buy stock on day 1, and sell it on 4th day, which will give us maximum profit.
 Now, we buy stock on day 5 and sell it on day 9.
Testcase 3: We can buy stock on day 3, and sell it on 4th day, which will give us maximum profit.
Testcase 4: We cannot sell any stock that will give us profit as the price remains same.
Testcase 5: Buy on day 0 and sell on day 1. Then buy on day 2 and sell on day 3. Next, buy on day 4 and sell on day 8.
    """
