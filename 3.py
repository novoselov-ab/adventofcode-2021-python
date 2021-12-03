with open("3.txt") as f:
    nums = [x for x in f.read().split("\n")]
    totals = [0] * len(nums[0])
    for n in nums:
        for i, c in enumerate(n):
            totals[i] += 1 if c == "1" else -1
    gamma = int("".join(map(lambda x: "1" if x > 0 else "0", totals)), 2)
    epsilon = int("".join(map(lambda x: "1" if x <= 0 else "0", totals)), 2)
    print("part 1: {}".format(gamma * epsilon))

    nums = sorted(nums)

    def process(nums, flip):
        for i in range(len(nums[0])):
            index = next((j for j, n in enumerate(nums) if n[i] == "1"), len(nums))
            cmp = index > len(nums) / 2 if flip else index <= len(nums) / 2
            nums = nums[index:] if cmp else nums[:index]
            if len(nums) == 1:
                return int(nums[0], 2)

    print("part 2: {}".format(process(nums, True) * process(nums, False)))
