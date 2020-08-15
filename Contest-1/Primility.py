def isPrime(N):
    if (N==1): #1 is not prime so return false
        return True
    for i in range(2,1+int(math.sqrt(N))): #We check from 2 from sqrt(N) as divisors, if any, would exist till sqrt(N)
        if N%i==0: #If any i divides the number this means the nubmer is not prime
            return False
    return True #return true in ither cases
n=int(input())
print(isPrime(n))
