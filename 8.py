TRUE_MAPPING = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}
LETTERS = "abcdefg"

with open("8.txt") as f:
    part_1 = 0
    part_2 = 0

    for line in f.readlines():
        input, out = line.split("|")
        input = sorted((sorted(x) for x in input.strip().split(" ")), key=lambda x: len(x))
        out = (sorted(x) for x in out.strip().split(" "))

        def search(mapping, index=0):
            if index >= len(input):
                return True

            word = ""
            for c in input[index]:
                if c in mapping:
                    word += mapping[c]
                else:
                    for k in LETTERS:
                        if k not in mapping.values():
                            mapping[c] = k
                            if search(mapping, index):
                                return True
                            del mapping[c]
                    return False

            if "".join(sorted(word)) not in TRUE_MAPPING:
                return False

            return search(mapping, index + 1)

        mapping = {}
        if search(mapping):
            number = ""
            for word in out:
                digit = TRUE_MAPPING["".join(sorted([mapping[c] for c in word]))]
                if digit in [1, 4, 7, 8]:
                    part_1 += 1
                number += str(digit)
            part_2 += int(number)

    print(part_1)
    print(part_2)
