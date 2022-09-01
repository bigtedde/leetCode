# Ted Lawson

class Solution:
    def fib(self, n: float) -> float:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)


def main():
    n = 37
    s = Solution().fib(n)
    print(f'the Fib. Seq. at position {n} is {s}.')


if __name__ == '__main__':
    main()

