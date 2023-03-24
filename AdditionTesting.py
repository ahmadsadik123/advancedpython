import unittest


def addition(x, y):
    return x + y


class AdditionTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(10, 5), 15)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(-1, -1), -2)


if __name__ == "__main__":
    unittest.main()
