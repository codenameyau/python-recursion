import unittest
import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial.factorial(0), 1)
        self.assertEqual(factorial.factorial(1), 1)
        self.assertEqual(factorial.factorial(2), 2)
        self.assertEqual(factorial.factorial(3), 6)
        self.assertEqual(factorial.factorial(4), 24)
        self.assertEqual(factorial.factorial(5), 120)

    def test_factorial_rec(self):
        self.assertEqual(factorial.factorial_rec(0), 1)
        self.assertEqual(factorial.factorial_rec(1), 1)
        self.assertEqual(factorial.factorial_rec(2), 2)
        self.assertEqual(factorial.factorial_rec(3), 6)
        self.assertEqual(factorial.factorial_rec(4), 24)
        self.assertEqual(factorial.factorial_rec(5), 120)

    def test_factorial_tail_rec(self):
        self.assertEqual(factorial.factorial_tail_rec(0), 1)
        self.assertEqual(factorial.factorial_tail_rec(1), 1)
        self.assertEqual(factorial.factorial_tail_rec(2), 2)
        self.assertEqual(factorial.factorial_tail_rec(3), 6)
        self.assertEqual(factorial.factorial_tail_rec(4), 24)
        self.assertEqual(factorial.factorial_tail_rec(5), 120)

    def test_factorial_reduce(self):
        self.assertEqual(factorial.factorial_reduce(0), 1)
        self.assertEqual(factorial.factorial_reduce(1), 1)
        self.assertEqual(factorial.factorial_reduce(2), 2)
        self.assertEqual(factorial.factorial_reduce(3), 6)
        self.assertEqual(factorial.factorial_reduce(4), 24)
        self.assertEqual(factorial.factorial_reduce(5), 120)


if __name__ == '__main__':
    unittest.main()
