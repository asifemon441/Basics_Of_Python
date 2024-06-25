import unittest
from calculator import add

class TestAddition(unittest.TestCase):
    def test_add(self):
        result = add(10,5)
        self.assertEquals(result,15)
    def test_add1(self):
        result = add(-2,-4)
        self.assertEquals(result,-6)
    def test_add2(self):
        result = add(3,-2)
        self.assertEquals(result,1)

if __name__ =='__main__':
    unittest.main()

