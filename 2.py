with open("2.txt") as f:
    ins = [x.split(" ") for x in f.read().split("\n")]
    x = sum(int(v) for c, v in ins if c == "forward")
    y = sum(int(v) for c, v in ins if c == "down") - sum(int(v) for c, v in ins if c == "up")
    print("part1: {}".format(x * y))

    aim = 0
    x, y = 0, 0
    for c, v in ins:
        if c == "forward":
            x += int(v)
            y += aim * int(v)
        else:
            aim += int(v) * (-1 if c == "up" else 1)
    print("part2: {}".format(x * y))
