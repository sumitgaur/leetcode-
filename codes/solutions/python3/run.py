def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, 1 + l):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1
def solution(n):
    d = [0] * 30
    l = 0
    while n > 0:
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, 1 + l//2): #here you put l//2
        ok = True
        print('p est ',p)
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return
solution(5)