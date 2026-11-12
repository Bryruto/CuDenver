import math
import random


class SkipNode:
    def __init__(self, value: int, height: int):
        # store the value and make a forward link for each level
        self.value = value
        # each entry points to the next node on that level
        self.forward: list[SkipNode | None] = [None] * height


class Brycen_SkipList:
    def __init__(self, max_elements: int, seed: int | None = None):
        # use the expected size to set the maximum height
        # use a seed to make random promotions repeatable
        if max_elements < 1:
            raise ValueError("max_elements must be at least 1")
        self.height = max(1, math.ceil(math.log2(max_elements)))
        # the head value is a placeholder and is never compared with stored keys
        self.head = SkipNode(0, self.height)
        self.element_count = 0
        self.random = random.Random(seed)

    def search(self, key: int) -> bool:
        # search for one key starting at the highest level
        # move forward while the next value is smaller than the key
        # move down a level while staying at the same node
        # return true if the key is found or false otherwise
        current = self.head
        for level in range(self.height - 1, -1, -1):
            next_node = current.forward[level]
            while next_node is not None and next_node.value < key:
                current = next_node
                next_node = current.forward[level]

        candidate = current.forward[0]
        return candidate is not None and candidate.value == key

    def insert(self, value: int) -> None:
        # insert one value by finding the node before it at each level
        previous = [self.head] * self.height
        current = self.head
        for level in range(self.height - 1, -1, -1):
            next_node = current.forward[level]
            while next_node is not None and next_node.value < value:
                current = next_node
                next_node = current.forward[level]
            previous[level] = current

        # every node occupies level zero with a half chance of each promotion
        node_height = 1
        while node_height < self.height and self.random.randint(0, 1) == 1:
            node_height += 1

        # keep duplicates as separate nodes and include them in the count
        node = SkipNode(value, node_height)
        for level in range(node_height):
            node.forward[level] = previous[level].forward[level]
            previous[level].forward[level] = node
        self.element_count += 1


def test_empty_and_single_value():
    # check an empty list then check one stored value and missing values
    skiplist = Brycen_SkipList(1, seed=0)
    assert skiplist.search(5) is False
    skiplist.insert(5)
    assert skiplist.search(5) is True
    assert skiplist.search(4) is False
    assert skiplist.search(6) is False


def test_search_and_structure():
    # check searches and duplicate counts with different random promotions
    values = [9, -3, 5, 0, 5, 12, -3, 1]
    for seed in range(10):
        skiplist = Brycen_SkipList(len(values), seed=seed)
        for value in values:
            skiplist.insert(value)
        for key in range(-5, 15):
            assert skiplist.search(key) == (key in values)
        assert skiplist.element_count == len(values)

        # check that every level is sorted and higher nodes exist below
        levels = []
        for level in range(skiplist.height):
            nodes = []
            current = skiplist.head.forward[level]
            while current is not None:
                nodes.append(current)
                current = current.forward[level]
            assert [node.value for node in nodes] == sorted(node.value for node in nodes)
            levels.append(nodes)
        assert [node.value for node in levels[0]] == sorted(values)
        for level in range(1, skiplist.height):
            assert set(levels[level]).issubset(levels[level - 1])


def test_randomized_insertions_and_searches():
    # compare searches with a set after inserting random values
    rng = random.Random(42)
    values = [rng.randrange(-100, 101) for _ in range(1000)]
    skiplist = Brycen_SkipList(len(values), seed=42)
    present = set()
    for value in values:
        skiplist.insert(value)
        present.add(value)
        assert skiplist.search(value) is True
    for key in range(-110, 111):
        assert skiplist.search(key) == (key in present)


if __name__ == "__main__":
    # run the tests when this file is run directly
    test_empty_and_single_value()
    test_search_and_structure()
    test_randomized_insertions_and_searches()
