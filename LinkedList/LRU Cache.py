# User function Template for python3

# design the class in the most optimal way


from collections import OrderedDict


class LRUCache:

    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

        # we return the value of the key

    # that is queried in O(1) and return -1 if we
    # don't find the key in out dict / cache.
    # And also move the key to the end
    # to show that it was recently used.
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
            # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry = int(input())  # number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list

        lru = LRUCache(cap)

        i = 0
        q = 1
        while q <= qry:
            qtyp = a[i]

            if qtyp == 'SET':
                lru.set(int(a[i + 1]), int(a[i + 2]))
                i += 3
            elif qtyp == 'GET':
                print(lru.get(int(a[i + 1])), end=' ')
                i += 2
            q += 1
        print()
# } Driver Code Ends