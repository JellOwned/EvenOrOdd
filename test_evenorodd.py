import unittest

from evenorodd.evenorodd import isEven, isOdd


class TestEvenOrOdd(unittest.TestCase):

    def test_even(self):
        self.assertTrue(isEven(0), True)
        self.assertTrue(isEven("2"), True)
        self.assertTrue(isEven(-2), True)

        self.assertTrue(not isEven(1), True)
        self.assertFalse(not isEven(0), False)

        self.assertFalse(isEven(1), False)
        self.assertFalse(isEven("3"), False)
        self.assertFalse(isEven(-1), False)

        self.assertIsInstance(isEven(4), bool)
        self.assertIsInstance(isEven("2"), bool)
        self.assertIsInstance(isEven(-4), bool)

        with self.assertRaises(ValueError):
            isEven(True)
            isEven(False)
            isEven("abc")
            isEven(5.12)


    def test_odd(self):
        self.assertFalse(isOdd(0), False)
        self.assertFalse(isOdd("2"), False)

        self.assertFalse(not isOdd(1), False)
        self.assertTrue(not isOdd(0), True)

        self.assertTrue(isOdd(1), True)
        self.assertTrue(isOdd("3"), True)
        self.assertTrue(isOdd(-1), True)

        self.assertIsInstance(isOdd(3), bool)
        self.assertIsInstance(isOdd("1"), bool)
        self.assertIsInstance(isOdd(-3), bool)

        with self.assertRaises(ValueError):
            isOdd(True)
            isOdd(False)
            isOdd("abc")
            isOdd(5.12)

if __name__ == "__main__":
    unittest.main()