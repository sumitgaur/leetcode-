from collections import Counter


def mostActive(customers):
    # Write your code here
    counter = Counter(customers)
    n = len(customers)
    return sorted(map(lambda x: x[0], filter(lambda x: (x[1] / n) > 0.05, counter.most_common())))


print(list(mostActive(["Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Alpha",
                       "Omega",
                       "Beta"])))
