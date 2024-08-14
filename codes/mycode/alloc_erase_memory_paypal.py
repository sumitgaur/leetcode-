def alloc_erase(memory, queries):
    res = []
    for q in queries:
        if q[0] == 0:  # alloc
            flag = False
            for i in range(0, len(memory), 8):
                if memory[i:i + q[1]] == [0] * q[1]:
                    res.append(i)
                    memory[i:i + q[1]] = [1] * q[1]
                    flag = True
                    break
            if not flag:
                res.append(-1)
        else:  # erase
            c = 0
            for x in range(8 * q[1], 8 * q[1] + 8):
                if memory[x] == 1:
                    memory[x] = 0
                    c += 1
            res.append(c)
    print(res)

    return res


memory = [0] * 16
queries = [[0, 3], [0, 1], [1, 1], [0, 1]]
alloc_erase(memory, queries)
