from collections import Counter

with open("6.txt") as f:
    a = [int(x) for x in f.readline().split(",")]

    def calc(iters):
        d = Counter(a)
        for t in range(iters):
            if t in d:
                d[t + 8 + 1] += d[t]
                d[t + 6 + 1] += d[t]
                del d[t]
        return sum(d.values())

    print("part1: ", calc(80))
    print("part2: ", calc(256))

