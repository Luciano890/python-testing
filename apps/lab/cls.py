class PlusOne:
    _number = []
    def __init__(self, n) -> None:
        """..."""
        self.n = n
        self._number.append(self.n)

    @property
    def num(self):
        """..."""
        return sum(self._number)

    @classmethod
    def sum_one(cls, n):
        """..."""
        return cls(n)
    
    @classmethod
    def sum_times_two(cls, n):
        """..."""
        return cls(2*n)

if __name__ == '__main__':
    a = PlusOne(10)
    print(a.n)
    a\
        .sum_one(10)\
        .sum_one(10)\
        .sum_times_two(40)
    print(a.num)
