with open("7.txt") as f:
    crabs = sorted([int(x) for x in f.readline().split(",")])

    def fuel_1(d):
        return abs(d)

    def fuel_2(d):
        d = abs(d)
        return int((1 + d) / 2 * d)

    def crabify(fuel):
        pos = 0
        prev_dist = None
        for ans in range(crabs[0], crabs[-1] + 1):
            while pos < len(crabs) and crabs[pos] <= ans:
                pos += 1
            dist = sum(fuel(c - ans) for c in crabs)
            if prev_dist and dist > prev_dist:
                return prev_dist
            prev_dist = dist

    print(crabify(fuel_1))
    print(crabify(fuel_2))
