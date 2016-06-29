import types
import random
import copy

from sortedcontainers import SortedListWithKey

"""
The method to get the key to compare sets.
For comparison the SortedListWithKey member named list is used, as the member can be sorted.
This method is instroduced due to the overriding of operators like lower than, greater than and equal.
"""
def gen_set_key(value):
    return value.list


"""
The Set class that enables multiple operations supporting setlx notations
"""
class Set():

    """
    Constructor, to either pass generators or a already existing list containing the data (mostly used internally).
    Attention: If a set is passed, the reference to the internal member list.
    """
    def __init__(self, *args, list=None, keep_generators=False):
        if set is not None:
            assert isinstance(list, SortedListWithKey)
            self.list = list
            self.has_key = True
        else:
            self.list = SortedListWithKey()
            self.has_key = False

        for arg in args:
            if isinstance(arg, types.GeneratorType) \
                    and not keep_generators:
                for x in arg:
                    self._put(x)
            else:
                self._put(arg)

    """
    Overrides the add operator. Creates a new set not referencing the added sets.
    """
    def __add__(self, other):
        assert isinstance(other, Set)
        if len(self.list) == 0 and len(other.list) == 0:
            return Set()
        elif len(self.list) == 0:
            return copy.copy(other)
        else:
            set = SortedListWithKey(key=self.list._key)
            set.update(copy.deepcopy(self.list))
            other_list_copy = copy.deepcopy(other.list)
            for x in other_list_copy:
                if x not in set:
                    set.add(x)
            return Set(set=set)

    """
    Overrides the += operator. Adds all elements of an other set to the current set.
    """
    def __iadd__(self, other):
        assert isinstance(other, Set)
        for x in other.list:
            self._put(x)
        return self

    """
    Overrides the substraction operator. Removes every element from the current set, that is in the other set.
    """
    def __sub__(self, other):
        assert isinstance(other, Set)
        if len(self.list) == 0:
            return Set()
        set = SortedListWithKey(key=self.list._key)
        for x in self.list:
            if x not in other.list:
                set.add(x)
        s = Set(set=set)
        return s

    """
    Overrides the multiplication operator. Creates a new set only containing elements existing in both sets.
    """
    def __mul__(self, other):
        assert isinstance(other, Set)
        if len(self.list) == 0:
            return Set()
        set = SortedListWithKey(key=self.list._key)
        for x in self.list:
            if x in other.list:
                set.add(x)
        s = Set(set=set)
        return s

    """
    Method to represent the current set as string.
    """
    def __str__(self):
        return '{ %s }' % ', '.join([str(x) for x in self.list])

    """
    Overrides the pow operator (set ** 2). Returns the powerset.
    """
    def __pow__(self, other):
        return self.__rpow__(other)

    """
    Overrides the pow operator (2 ** set). Returns the powerset.
    """
    def __rpow__(self, other):
        assert isinstance(other, int)
        if other != 2:
            raise Exception('Lefthandside is not 2. To generate the powerset use "2 ** myset"')

        from copy import deepcopy
        copied_set = deepcopy(self)

        return Set.power(copied_set)

    """
    Overrides the modulo operator.
    """
    def __mod__(self, other):
        assert isinstance(other, Set)
        return (self - other) + (other - self)

    """
    Returns the iterator of the internal list.
    """
    def __iter__(self):
        return self.list.__iter__()

    """
    Returns the number of elements contained in the set.
    """
    def __len__(self):
        return len(self.list)

    """
    Overrides the lower than equal operator, indicating if a set is contained in an other set or both sets are equal.
    """
    def __lt__(self, other):
        assert isinstance(other, Set)
        if len(self.list) >= len(other.list):
            return False
        return all(x in other.list for x in self.list)

    """
    Overrides the greater than equal operator, indicating if a set contains an other set or both sets are equal.
    """
    def __gt__(self, other):
        assert isinstance(other, Set)
        if len(self.list) <= len(other.list):
            return False
        return all(x in self.list for x in other.list)

    """
    Overrides the greater than operator indicating if a set contains an other set but is not the same.
    """
    def __ge__(self, other):
        assert isinstance(other, Set)
        for x in other.list:
            if x not in self.list:
                return False
        return True

    """
    Overrides the lower than operator indicating if this set is contained in an other set but is not the smae.
    """
    def __le__(self, other):
        assert isinstance(other, Set)
        for x in self.list:
            if x not in other.list:
                return False
        return True

    """
    Overrides the equals operator. Indicates if two sets contain the same elements.
    """
    def __eq__(self, other):
        assert isinstance(other, Set)
        if len(self.list) != len(other.list):
            return False
        for x in self.list:
            if x not in other.list:
                return False
        for x in other.list:
            if x not in self.list:
                return False
        return True

    """
    Overrides the not equals operator. Indicates if two sets are not equal.
    """
    def __ne__(self, other):
        assert isinstance(other, Set)
        return not self == other

    """
    Overrides the in operator, indicates if the set contains the element.
    """
    def __contains__(self, other):
        return other in self.list

    """
    Returns the __getitem__ method of the internal list, to support array slicing.
    """
    def __getitem__(self, key):
        return self.list.__getitem__(key)

    """
    Returns the cartesian product of the current set.
    """
    def cartesian_product(self, other):
        assert isinstance(other, Set)
        s = Set()
        for x in self.list:
            for y in other.list:
                s.set.add((x, y))
        return s

    """
    Creates a power set from a set.
    """
    @staticmethod
    def power(s):
        if len(s) == 0:
            return Set(Set())
        x = s.pop()
        y = Set.power(s)
        z = Set(m + Set(x) for m in y)
        return y + z

    """
    Returns a arbitary element from set.
    """
    def arb(self):
        return self.list[-1] if len(self.list) % 2 == 0 else self.list[0]

    """
    Returns a random element from set.
    """
    def rnd(self):
        return self.list[random.randrange(0, len(self.list))]

    """
    Adds an element to the current set.
    """
    def put(self, other):
        self._put(other)

    """
    Internal _put method to keep track of the added element. To define if the current set contains sets.
    """
    def _put(self, other):
        if self.has_key is False:
            self.has_key = True
            if isinstance(other, Set):
                self.list._key = gen_set_key
        if other not in self.list:
            self.list.add(other)

    """
    Returns the last element of the set.
    """
    def peek(self):
        return self.list[-1]

    """
    Returns the last element of the set and removes it.
    """
    def pop(self):
        x = self.list.pop()
        return x

    """
    Returns the sum of all elements inside the sets. Using the + / += operators.
    """
    def sum(self):
        import copy
        temp = None
        for x in self.list:
            if temp is None:
                temp = copy.deepcopy(x)
            else:
                temp += x
        return temp


"""
Basic class testing methods.
"""
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