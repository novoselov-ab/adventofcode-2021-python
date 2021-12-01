with open("1.txt") as f:
    nums = [int(x) for x in f.read().split("\n")]
    cnt = sum(y - x > 0 for x, y in zip(nums, nums[1:]))
    print(f"part1: {cnt}")

    nums = [x + y + z for x, y, z in zip(nums, nums[1:], nums[2:])]
    cnt = sum(y - x > 0 for x, y in zip(nums, nums[1:]))
    print(f"part2: {cnt}")