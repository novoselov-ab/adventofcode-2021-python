from math import floor, ceil, tau
from functools import reduce
from copy import deepcopy

with open("18.txt", "r") as f:
    input = [eval(s) for s in f.readlines()]

    class Exploder:
        def __init__(self, t):
            self.exploded = False
            self.carry = None
            self.n = 0
            self._explode(t)
            if self.exploded:
                self.n = 0
                self._prop(t)

        def _explode(self, t, level=0):
            if self.exploded:
                return

            if isinstance(t[0], int) and isinstance(t[1], int) and level >= 4:
                self.carry = t
                self.exploded = True
                self.explode_n = self.n
                self.n += 2
                return True

            for i, v in enumerate(t):
                if isinstance(v, list):
                    if self._explode(v, level + 1):
                        t[i] = 0
                else:
                    self.n += 1

        def _prop(self, t):
            for i, v in enumerate(t):
                if isinstance(v, list):
                    self._prop(v)
                else:
                    if self.n == self.explode_n - 1 and self.carry[0] > 0:
                        t[i] += self.carry[0]
                    elif self.n == self.explode_n + 1 and self.carry[1] > 0:
                        t[i] += self.carry[1]
                    self.n += 1

    class Splitter:
        def __init__(self, t):
            self.splitted = False
            self._split(t)

        def _split(self, t):
            if self.splitted:
                return
            for i, v in enumerate(t):
                if isinstance(v, list):
                    self._split(v)
                else:
                    if v >= 10 and not self.splitted:
                        t[i] = [floor(v / 2), ceil(v / 2)]
                        self.splitted = True

    def reduce_snail(t):
        while True:
            if Exploder(t).exploded:
                continue
            if Splitter(t).splitted:
                continue
            break
        return t

    def add(x, y):
        return reduce_snail([deepcopy(x), deepcopy(y)])

    def mag(t):
        if isinstance(t, list):
            return 3 * mag(t[0]) + 2 * mag(t[1])
        else:
            return t

    print(mag(reduce(add, input)))

    ans = 0
    for i, v in enumerate(input):
        for j, w in enumerate(input):
            if i == j:
                continue
            ans = max(ans, mag(add(v, w)))
    print(ans)
