with open("11.txt") as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]

    def iter_dir(x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                x2 = x + dx
                y2 = y + dy
                if x2 >= 0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid):
                    yield x2, y2

    def iter_all():
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                yield x, y

    def prop_flash(x, y):
        grid[y][x] += 1
        if grid[y][x] == 10:
            return 1 + sum(prop_flash(x2, y2) for x2, y2 in iter_dir(x, y))
        return 0

    part_1 = 0
    for step in range(2 ** 128):
        flashes = sum(prop_flash(x, y) for x, y in iter_all())

        for x, y in iter_all():
            if grid[y][x] > 9:
                grid[y][x] = 0

        if flashes == len(grid) * len(grid[0]):
            part_2 = step + 1
            break

        if step < 100:
            part_1 += flashes

    print(part_1)
    print(part_2)
