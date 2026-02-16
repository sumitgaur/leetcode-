def canChange(start: str, target: str) -> bool:
    start_queue = []
    target_queue = []
    for i in range(len(start)):
        if start[i] != '_':
            start_queue.append((start[i], i))
        if target[i] != '_':
            target_queue.append((target[i], i))
    if len(start_queue) != len(target_queue): return False
    while start_queue:
        sc, si = start_queue.pop(0)
        tc, ti = target_queue.pop(0)
        if not(sc == tc and ((sc == 'L' and si >= ti) or (sc == 'R' and si <= ti))):
            return False
    return True


start = "R_L_"
target = "__LR"
canChange(start, target)
