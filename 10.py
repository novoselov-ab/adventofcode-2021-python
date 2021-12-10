PAREN = {"[": "]", "(": ")", "{": "}", "<": ">"}
INV_PAREN = {v: k for k, v in PAREN.items()}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
POINTS_2 = {")": 1, "]": 2, "}": 3, ">": 4}

with open("10.txt") as f:
    part_1 = 0
    scores = []
    for line in f.readlines():

        def parse(line):
            s = []
            for c in line.strip():
                if c in PAREN:
                    s.append(c)
                elif c in INV_PAREN:
                    if s.pop() != INV_PAREN[c]:
                        return POINTS[c], []
            return 0, s

        p, s = parse(line)
        part_1 += p
        if s:
            score = 0
            for n in s[::-1]:
                score = score * 5 + POINTS_2[PAREN[n]]
            scores.append(score)
    print(part_1)
    print(sorted(scores)[len(scores) // 2])
