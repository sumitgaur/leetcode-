def queue_by_stack():
    global x
    q = int(input().strip())
    s1, s2 = [], []
    for _ in range(q):
        in_ = input().strip()
        op, x = in_.split(" ") if " " in in_ else (in_, _)
        if op == "1":
            while s2:
                s1.append(s2.pop())
            s1.append(x)
            while s1:
                s2.append(s1.pop())
        elif op == "2":
            s2.pop()
        else:
            print(s2[-1])


