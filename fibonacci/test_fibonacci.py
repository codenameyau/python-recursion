import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fibonacci.fib(1), 1)
        self.assertEqual(fibonacci.fib(2), 1)
        self.assertEqual(fibonacci.fib(3), 2)
        self.assertEqual(fibonacci.fib(4), 3)
        self.assertEqual(fibonacci.fib(5), 5)
        self.assertEqual(fibonacci.fib(6), 8)
        self.assertEqual(fibonacci.fib(7), 13)
        self.assertEqual(fibonacci.fib(8), 21)

    def test_fib_rec(self):
        self.assertEqual(fibonacci.fib_rec(1), 1)
        self.assertEqual(fibonacci.fib_rec(2), 1)
        self.assertEqual(fibonacci.fib_rec(3), 2)
        self.assertEqual(fibonacci.fib_rec(4), 3)
        self.assertEqual(fibonacci.fib_rec(5), 5)
        self.assertEqual(fibonacci.fib_rec(6), 8)
        self.assertEqual(fibonacci.fib_rec(7), 13)
        self.assertEqual(fibonacci.fib_rec(8), 21)

    def test_fib_binet(self):
        self.assertEqual(fibonacci.fib_binet(1), 1)
        self.assertEqual(fibonacci.fib_binet(2), 1)
        self.assertEqual(fibonacci.fib_binet(3), 2)
        self.assertEqual(fibonacci.fib_binet(4), 3)
        self.assertEqual(fibonacci.fib_binet(5), 5)
        self.assertEqual(fibonacci.fib_binet(6), 8)
        self.assertEqual(fibonacci.fib_binet(7), 13)
        self.assertEqual(fibonacci.fib_binet(8), 21)

if __name__ == '__main__':
    unittest.main()
