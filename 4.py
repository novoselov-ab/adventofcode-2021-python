with open("4.txt") as f:
    moves = [int(x) for x in f.readline().split(",")]

    boards = []
    while f.readline():
        board = []
        for i in range(5):
            board.append([int(x) for x in f.readline().strip().replace("  ", " ").split(" ")])
        boards.append(board)

    def check_h(board, x, y):
        return all(board[k][x] is None for k in range(5))

    def check_v(board, x, y):
        return all(board[y][k] is None for k in range(5))

    def pin(board, m):
        for y, row in enumerate(board):
            for x, n in enumerate(row):
                if n == m:
                    row[x] = None
                    if check_h(board, x, y) or check_v(board, x, y):
                        return True
        return False

    def run():
        winners = []
        skip = set()
        for m in moves:
            for i, board in enumerate(boards):
                if i in skip:
                    continue
                if pin(board, m):
                    winners.append((m, board))
                    skip.add(i)
        return winners

    def score(winner):
        move, board = winner
        s = sum([sum(n for n in i if n) for i in board])
        return move * s

    winners = run()
    print("part1: {}".format(score(winners[0])))
    print("part2: {}".format(score(winners[-1])))
