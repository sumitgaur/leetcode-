def do_valid(days, bloomday,m,k):
    bq, f = 0, 0
    for b in bloomday:
        if b > days:
            f = 0
        else:
            f += 1
            if (f == k):
                bq += 1
                f = 0
    # print(bq,f)
    return bq >= m


def findmin(bloomday, m, k):
    if len(bloomday) < m * k:
        return -1

    l, r = min(bloomDay), max(bloomday)
    while l < r:
        m = (l + r) // 2
        if do_valid(m, bloomDay,):
            r = m
        else:
            l = m + 1
    return r


t1 = ([1, 10, 3, 10, 2], 3, 1)
t2 = ([1, 1, 1, 1, 1], 1, 1)
t3 = ([[1, 10, 3, 10, 2]], 3, 2)

print(findmin(t1[0], t1[1], t1[2]) == 3)
print(findmin(t2[0], t2[1], t2[2]) == 1)
print(findmin(t3[0], t3[1], t3[2]) == -1)