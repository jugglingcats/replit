import unittest
from main import add

class TestMyStuff(unittest.TestCase):
  def test_test1(self):
    self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()