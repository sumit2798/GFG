from collections import OrderedDict


def winner(arr, n):
    mp = OrderedDict({})

    # adding names in the dictionary
    # to have count of each names
    for i in arr:
        mp[i] = mp.get(i, 0) + 1

    maxx = -1
    ans = ""
    mp = OrderedDict(sorted(mp.items()))

    # iterating over the dictoinary to get the names and their frequncy
    for key, value in mp.items():
        if value > maxx:
            maxx = value
            answer = key

    return (answer, maxx)