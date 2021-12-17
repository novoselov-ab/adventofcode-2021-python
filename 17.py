target_x = [85, 145]
target_y = [-163, -108]


def run(vx, vy):
    x = 0
    y = 0
    max_y = 0
    for _ in range(100000):
        max_y = max(max_y, y)
        if y < target_y[0] or x > target_x[1]:
            return None

        in_target = x >= target_x[0] and x <= target_x[1] and y >= target_y[0] and y <= target_y[1]
        if in_target:
            return max_y
        x += vx
        y += vy
        if vx != 0:
            vx -= 1
        vy -= 1

    return None


def brute():
    res = []
    vel = set()
    for vx in range(0, target_x[1] + 1):
        for vy in range(target_y[0] - 2, -target_y[0] + 2):
            s = run(vx, vy)
            if s is not None:
                res.append(s)
                vel.add((vx, vy))
    print(max(res))
    print(len(vel))


brute()
