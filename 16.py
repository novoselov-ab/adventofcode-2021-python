from operator import mul
from functools import reduce

with open("16.txt") as f:
    input = "".join((bin(int(c, 16))[2:].zfill(4) for c in f.readline()))

    part_1 = 0

    def parse_version(input):
        return int(input[0:3], 2), input[3:]

    def parse_type(input):
        return int(input[0:3], 2), input[3:]

    def parse_value(input):
        r = ""
        while True:
            group = input[0:5]
            input = input[5:]
            r += group[1:]
            if group[0] == "0":
                break

        return int(r, 2), input

    def parse_operator(input, type, versions):
        values = []
        if input[0] == "0":
            length = int(input[1:16], 2)
            input = input[16:]
            size = len(input)
            while len(input) + length > size:
                value, input = parse(input, versions)
                values.append(value)
        else:
            cnt = int(input[1:12], 2)
            input = input[12:]
            for _ in range(cnt):
                value, input = parse(input, versions)
                values.append(value)

        ops = {
            0: lambda v: sum(v),
            1: lambda v: reduce(mul, v, 1),
            2: lambda v: min(v),
            3: lambda v: max(v),
            5: lambda v: int(v[0] > v[1]),
            6: lambda v: int(v[0] < v[1]),
            7: lambda v: int(v[0] == v[1]),
        }
        return ops[type](values), input

    def parse(input, versions):
        version, input = parse_version(input)
        versions.append(version)
        type, input = parse_type(input)
        if type == 4:
            return parse_value(input)
        else:
            return parse_operator(input, type, versions)

    versions = []
    value, _ = parse(input, versions)
    print(sum(versions))
    print(value)
