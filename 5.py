with open("5.txt") as f:
    lines = [x.strip().split(" -> ") for x in f.readlines()]
    lines = [[x.split(",") for x in p] for p in lines]

    def delta(t1, t0):
        if t1 == t0:
            return 0
        return (t1 - t0) / abs(t1 - t0)

    def calc(diag):
        d = {}
        for f, t in lines:
            x0, y0, x1, y1 = *map(int, f), *map(int, t)
            if not diag and x0 != x1 and y0 != y1:
                continue
            while x0 != x1 or y0 != y1:
                d[(x0, y0)] = d.get((x0, y0), 0) + 1
                x0 += delta(x1, x0)
                y0 += delta(y1, y0)
            d[(x0, y0)] = d.get((x0, y0), 0) + 1
        return sum((1 for d in d.values() if d > 1))
    print("part1: ", calc(False))
    print("part2: ", calc(True))
