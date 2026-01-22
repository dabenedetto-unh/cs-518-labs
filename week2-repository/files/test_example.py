import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
    
    def test_string_concatenation(self):
        self.assertEqual("hello" + " world", "hello world")
    
    def test_list_length(self):
        self.assertEqual(len([1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()