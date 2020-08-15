"""You are given a number N. You need to toggle the middle bit of N in binary form and print the result in decimal form.

If number of bits in binary form of N are odd then toggle the middle bit (Like 111 to 101).
If number of bits in binary form of N are even then toggle both the middle bits (Like 1111 to 1001)
Note: Toggling a bit means converting a 0 to 1 and vice versa.
"""
from math import log2
from math import floor
for i in range(int(input())):
    n=int(input())
    numberOfBits = 1 + floor(log2(n))
    if (numberOfBits % 2 != 0):
        n=n ^ (1 << (numberOfBits // 2))

    else:
        n=n ^ (1 << (numberOfBits // 2))
        n=n ^ (1 << ((numberOfBits //2)-1))
    print(n)
