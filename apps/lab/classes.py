"""Classes"""

# class A:
#     """..."""
#     def __init__(self, f_zota) -> None:
#         self.f_zota = f_zota

#     def what(self, b):
#         """..."""
#         return b
    
#     def pren(self, p):
#         print(p)

# class B(A):
#     # def __init__(self) -> None:
#     #     pass
    
#     def what(self, b):
#         self.pren(super().what(b))
#         self.pren("esoo")

class B:
    __nums = []
    def __init__(self, num) -> None:
        self.num = num
        self.__nums.append(self.num)

    def _sum(self):
        return sum(self.__nums)

    @classmethod
    def add_num(cls, n):
        return cls(n)
    
    @classmethod
    def times_two(cls, n):
        return cls(2*n)

if __name__ == "__main__":
    b = B(10)
    (
        b
        .add_num(20)
        .add_num(20)
        .times_two(90)
        .add_num(20)
        .add_num(20)
        .times_two(90)
        .times_two(90)
        .times_two(90)
        .add_num(20)
        .add_num(20)
        .times_two(90)
        .add_num(20)
    )
    print(b._sum())