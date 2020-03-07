import unittest

class AdditionTestCase(unittest.TestCase):
    def test_main(self):
        result = addition(3, 2)
        assert result == 5


class MultiplyTestCase(unittest.TestCase):
    def test_main(self):
        result = multiply(3, 2)
        assert result == 6


def main():
    import sys
    num1, num2 = sys.argv[1:]
    num1, num2 = int(num1), int(num2)
    print(multiply(num1, num2))


def multiply(num1, num2):
    total = 0
    for _ in range(num2):
        total = addition(total, num1)
    return total


def addition(*args):
    total = 0
    for a in args:
        total += a
    return total



if __name__ == '__main__':
    main()
    #unittest.main()
