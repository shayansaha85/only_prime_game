import prime_checker as pc


def isPresent(n, li):
    length = len(li)
    count = 0
    for x in li:
        if x == n:
            count += 1
            break
    if count == 0:
        return False
    else:
        return True


def enterPrime():
    li = []
    n = input('Enter prime: ')
    li.append(n)
    count = 0
    if n.isdecimal():
        if pc.isPrime(int(n)):
            while pc.isPrime(int(n)):
                count += 1
                n = input('Enter prime: ')
                if n in li:
                    break
                li.append(n)
            return count
        else:
            return count
    else:
        return count
