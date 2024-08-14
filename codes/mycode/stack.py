# Enter your code here. Read input from STDIN. Print output to STDOUT

S = ""
st_ops = []

q = int(input().strip())
for _ in range(q):
    in_ = input().strip()
    op, x = in_.split(" ") if " " in in_ else [in_, _]
    if op == "1":
        S += x
        st_ops.append(["1", x])
    elif op == "2":
        k = int(x)
        st_ops.append(["2", S[-k:]])
        S = S[:-k]
    elif op == "3":
        print(S[int(x) - 1])
    elif op == "4":
        op, x = st_ops.pop()
        if op == "1":
            S = S[:-len(x)]
        else:
            S+=x
