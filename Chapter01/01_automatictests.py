import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

    def notatest(self):
        pass


class MySecondTestCase(unittest.TestCase):
    def test_two(self):
        pass

    def test_two_part2(self):
        pass


if __name__ == '__main__':
    unittest.main()
