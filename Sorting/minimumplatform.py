def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''

    platform = 1  # number of required platforms

    order = [] # stores pair with value as time of event and key is 1 for departure and 0 for arrival.

    for i in range(n):
        order.append([arr[i],0]) # arrival time
        order.append([dep[i],1]) # departure time

    # sort the order list, first according to time
    # if time is same for two events , than arrival comes first,followed by departure
    order = sorted(order, key= lambda x: (x[0],x[1]))

    # traverse one by one, if arr inc temp count else decrease it
    temp_required = 0 # temp requirement of platforms
    for i in range(2*n):
        if order[i][1]==0: # arrival
            temp_required+=1
            platform=max(platform,temp_required)
        else:
            if(temp_required):
                temp_required-=1 # decrease temp count by one for departure

    return platform # return answer