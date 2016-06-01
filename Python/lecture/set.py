import types
import random
import copy

from sortedcontainers import SortedListWithKey


def gen_set_key(value):
    return value.set

class Set():
    def __init__(self, *args, set=None, keep_generators=False):
        if set is not None:
            assert isinstance(set, SortedListWithKey)
            self.set = set
            self.has_key = True
        else:
            self.set = SortedListWithKey()
            self.has_key = False

        for arg in args:
            if isinstance(arg, types.GeneratorType) \
                    and not keep_generators:
                for x in arg:
                    self._put(x)
            else:
                self._put(arg)

    def __add__(self, other):
        assert isinstance(other, Set)
        if len(self.set) == 0 and len(other.set) == 0:
            return Set()
        elif len(self.set) == 0:
            return copy.copy(other)
        else:
            set = SortedListWithKey(key=self.set._key)
            set.update(self.set)
            for x in other.set:
                if x not in set:
                    set.add(x)
            return Set(set=set)


    def __iadd__(self, other):
        assert isinstance(other, Set)
        for x in other.set:
            self._put(x)
        return self

    def __sub__(self, other):
        assert isinstance(other, Set)
        if len(self.set) == 0:
            return Set()
        set = SortedListWithKey(key=self.set._key)
        for x in self.set:
            if x not in other.set:
                set.add(x)
        s = Set(set=set)
        return s

    def __mul__(self, other):
        assert isinstance(other, Set)
        if len(self.set) == 0:
            return Set()
        set = SortedListWithKey(key=self.set._key)
        for x in self.set:
            if x in other.set:
                set.add(x)
        s = Set(set=set)
        return s

    def __str__(self):
        return '{ %s }' % ', '.join([str(x) for x in self.set])

    def __pow__(self, other):
        return self.__rpow__(other)

    def __rpow__(self, other):
        assert isinstance(other, int)
        if other != 2:
            raise Exception('Lefthandside is not 2. To generate the powerset use "2 ** myset"')

        from copy import deepcopy
        copied_set = deepcopy(self)

        return Set.power(copied_set)

    def __mod__(self, other):
        assert isinstance(other, Set)
        return (self - other) + (other - self)

    def __iter__(self):
        return self.set.__iter__()

    def __len__(self):
        return len(self.set)

    def __lt__(self, other):
        assert isinstance(other, Set)
        if len(self.set) >= len(other.set):
            return False
        return all(x in other.set for x in self.set)

    def __gt__(self, other):
        assert isinstance(other, Set)
        if len(self.set) <= len(other.set):
            return False
        return all(x in self.set for x in other.set)

    def __ge__(self, other):
        assert isinstance(other, Set)
        for x in other.set:
            if x not in self.set:
                return False
        return True

    def __le__(self, other):
        assert isinstance(other, Set)
        for x in self.set:
            if x not in other.set:
                return False
        return True

    def __eq__(self, other):
        assert isinstance(other, Set)
        if len(self.set) != len(other.set):
            return False
        for x in self.set:
            if x not in other.set:
                return False
        for x in other.set:
            if x not in self.set:
                return False
        return True

    def __ne__(self, other):
        assert isinstance(other, Set)
        return not self == other

    def __contains__(self, other):
        return other in self.set

    def __getitem__(self, key):
        return self.set.__getitem__(key)

    # returns a new set representing the cartesian product of the current
    # set
    def cartesian_product(self, other):
        assert isinstance(other, Set)
        s = Set()
        for x in self.set:
            for y in other.set:
                s.set.add((x, y))
        return s

    @staticmethod
    def power(s):
        if len(s) == 0:
            return Set(Set())
        x = s.pop()
        y = Set.power(s)
        z = Set(m + Set(x) for m in y)
        return y + z

    def arb(self):
        return self.set[-1] if len(self.set) % 2 == 0 else self.set[0]

    def rnd(self):
        return self.set[random.randrange(0, len(self.set))]

    def put(self, other):
        self._put(other)

    def _put(self, other):
        if self.has_key is False:
            self.has_key = True
            if isinstance(other, Set):
                self.set._key = gen_set_key
        if other not in self.set:
            self.set.add(other)

    def peek(self):
        return self.set[-1]

    def pop(self):
        x = self.set.pop()
        return x

    def sum(self):
        import copy
        temp = None
        for x in self.set:
            if temp is None:
                temp = copy.deepcopy(x)
            else:
                temp += x
        return temp


if __name__ == '__main__':
    dl = [[x, x ** 2] for x in range(1, 10)]
    dl.append([1, 2, 3, 4])
    s = Set(1, 1, 2, 2, 2, 2, 3, 4)
    s1 = Set(2, 4, 6, 7, 8)

    s2 = s + s1
    s3 = s2 - s
    s4 = s * s1
    # s5 = s / s1
    s6 = s % s1
    print("s: %s" % s)
    print("s1: %s" % s1)
    print("s + s1: %s" % s2)
    print("2 ** s: %s" % 2 ** s)
    print("s + s1 - s: %s" % s3)
    print("s * s1: %s" % s4)
    # print("s / s1: %s" % s5)
    print("s %% s1: %s" % s6)

    print("-----------")
    for x in s:
        print(x)
    print("-----------")

    assert 1 in s

    print("[1, 1] in s: True")

    s7 = Set(1, 1, 2, 3)

    assert s7 <= s

    print("s <= s7: True")

    print("pop: %s" % s.pop())
    print("s: %s" % s)