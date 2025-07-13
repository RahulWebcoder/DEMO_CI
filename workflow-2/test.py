import unittest
import main

class mathtest(unittest.TestCases):
    def test_is_even(self):
        self.assertTrue(main.is_even(4))
    def test_is_even(self):
        self.assertTrue(main.is_odd(5))    




if __name__ == '__main__':
    unittest.main()

