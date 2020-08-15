def CountBits(n):
    n += 1
    count = 0

    x = 2
    while x // 2 < n:

        quotient = n // x
        count += quotient * x // 2

        remainder = n % x
        if remainder > x // 2:
            count += remainder - x // 2

        x = x * 2

    return count
