for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dic = {}  # stores how many subarray with particular sum we have found till now
    curr_sum = 0
    count = 0
    for i in range(n):
        curr_sum += arr[i]

        if curr_sum == 0:  # we found subarray starting from the index 0 to current i
            count += 1
        if curr_sum - 0 in dic:
            count += dic[curr_sum - 0]  # adding all the subaarays with this sum found till now
        dic[curr_sum] = dic.get(curr_sum, 0) + 1

    print(count)

