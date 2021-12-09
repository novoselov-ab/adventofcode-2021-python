from functools import reduce

with open("9.txt") as f:
    area = [[int(x) for x in line.strip()] for line in f.readlines()]

    def iter_dir(x, y):
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x2 = x + d[0]
            y2 = y + d[1]
            if x2 >= 0 and x2 < len(area[0]) and y2 >= 0 and y2 < len(area):
                yield x2, y2

    def height(area, x, y):
        height = -10
        for x2, y2 in iter_dir(x, y):
            height = max(height, area[y][x] - area[y2][x2])
        return height

    def calc_basin(area, x, y, basin):
        for x2, y2 in iter_dir(x, y):
            if area[y2][x2] != 9 and (y2, x2) not in basin:
                basin.add((y2, x2))
                calc_basin(area, x2, y2, basin)

    part_1 = 0
    part_2 = []
    for y, row in enumerate(area):
        for x, n in enumerate(row):
            if height(area, x, y) < 0:
                basin = set()
                calc_basin(area, x, y, basin)
                part_2.append(len(basin))
                part_1 += n + 1
    part_2 = reduce(lambda x, y: x * y, sorted(part_2, reverse=True)[:3])
    print(part_1)
    print(part_2)
