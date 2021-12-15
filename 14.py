from collections import Counter

with open("14.txt") as f:
    poly = f.readline().strip()
    f.readline()

    rules = {p[0]: p[1] for p in (a.strip().split(" -> ") for a in f.readlines())}

    def run(steps):
        pairs = Counter()
        for i in range(len(poly) - 1):
            pair = poly[i : i + 2]
            pairs[pair] += 1

        first_last = [poly[1], poly[-1]]

        for _ in range(steps):
            new_pairs = Counter()
            for pair, c in pairs.items():
                new_pairs[pair[0] + rules[pair]] += c
                new_pairs[rules[pair] + pair[1]] += c
            pairs = new_pairs

        cnt = Counter()
        for p, c in pairs.items():
            cnt[p[0]] += c
            cnt[p[1]] += c

        cnt2 = Counter()
        for a, c in cnt.items():
            cnt2[a] = (c + 1 if a in first_last else 0) / 2

        cnt3 = Counter(cnt2).most_common()
        return int(cnt3[0][1] - cnt3[-1][1])

    print(run(10))
    print(run(40))
