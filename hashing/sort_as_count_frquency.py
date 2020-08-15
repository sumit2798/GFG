def sortByFreq(a,n):
    #list containing frequency of all elements present in array a
    freq=[0 for i in range(max(a)+1)]

    #list of elements with frequency 'i' in array at index i.
    hash_for_freq=[ [] for i in range(n+1) ]

    for num in a:
        freq[num]+=1
    for i in range(max(a)+1):
        if(freq[i]):
            hash_for_freq[freq[i]].append(i)

    # here the complexity of this block of code can be proved to be O(n).
    l = []
    for i in range(n,0,-1):
        for num in hash_for_freq[i]:
            for j in range(i):
                l.append(num)
    return l
