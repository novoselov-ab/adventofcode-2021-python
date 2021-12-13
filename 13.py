import sys

with open("13.txt") as f:
    grid = set()
    while True:
        line = f.readline()
        if not line.strip():
            break
        p = tuple(int(n) for n in line.split(","))
        grid.add(p)

    folds = []
    while True:
        line = f.readline()
        if not line.strip():
            break
        axis, v = line.split("=")
        folds.append((int(v), 0) if axis[-1] == "x" else (0, int(v)))

    def dofolds(folds):
        grids = [grid, None]
        for fold in folds:
            grids[1] = set()
            for p in grids[0]:
                if p[0] >= fold[0] and p[1] >= fold[1]:
                    grids[1].add((abs(fold[0] * 2 - p[0]), abs(fold[1] * 2 - p[1])))
                else:
                    grids[1].add(p)
            grids[0] = grids[1]
        return grids[1]

    def render(grid):
        for y in range(max(r[1] for r in grid) + 1):
            for x in range(max(r[0] for r in grid) + 1):
                sys.stdout.write("0" if (x, y) in grid else ".")
            sys.stdout.write("\n")

    print(len(dofolds(folds[0:1])))
    render(dofolds(folds))
