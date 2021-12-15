from collections import defaultdict

with open("15.txt") as f:
    grid = [[int(x) for x in line.strip()] for line in f.readlines()]

    h = len(grid)
    w = len(grid[0])
    B = 2 ** 32

    def calc(wraps=1):
        dp = {}

        dp[(-1, 0)] = 0

        def step():
            for y in range(h * wraps):
                for x in range(w * wraps):
                    v = grid[y % h][x % w] +  y // h + x // w
                    v = 9 if v % 9 == 0 else v % 9
                    dp[(y, x)] = v + min(
                        dp.get((y - 1, x), B), dp.get((y, x - 1), B), dp.get((y + 1, x), B), dp.get((y, x + 1), B)
                    )

            return dp[(h * wraps - 1, w * wraps - 1)] - grid[0][0]

        prev = None
        for _ in range(1000):
            res = step()
            if res == prev:
                break
            prev = res

        return res

    print(calc(1))
    print(calc(5))
