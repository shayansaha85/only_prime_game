def isPrime(n):
    if n == 1 or n == 0:
        return False
    else:
        count = 0
        for i in range(2, n + 1):
            if n % i == 0:
                count += 1
        if count == 1:
            return True
        else:
            return False
