from collections import defaultdict

with open("12.txt") as f:
    edges = defaultdict(list)
    for f, t in (l.strip().split("-") for l in f.readlines()):
        edges[f] += [t]
        edges[t] += [f]

    def calc(cur, maxvisits=2, visited=defaultdict(int)):
        if cur == "end":
            return 1
        p = 0
        for x in edges[cur]:
            if x.islower():
                if visited[x] >= maxvisits or x == "start":
                    continue
                visited[x] += 1
            p += calc(x, 1 if visited[x] == 2 else maxvisits, visited)
            if x.islower():
                visited[x] -= 1

        return p

    print(calc("start", 1))
    print(calc("start", 2))
