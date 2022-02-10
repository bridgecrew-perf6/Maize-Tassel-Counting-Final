import unittest
import pytest
from main2 import *

# .assertEqual(a, b)
# .assertTrue(x)
# .assertFalse(x)
# .assertIsNone(x)
# .assertIs(a, b)
# .assertIsNot(a, b)
# .assertIn(a, b)
# .assertNotIn(a, b)
# .assertIsInstance(a, b)
# .assertNotIsInstance(a,b)

class MyTestCase(unittest.TestCase):
    #function testing
    def test_1(self):
        self.assertEqual(True, 1)
    def test_2(self):
        self.assertEqual(True, True)
    def test_3(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
