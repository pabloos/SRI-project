#A failed test to show how travis.yml works

import server
import unittest
 
class TestAdd(unittest.TestCase):
    def test_add_integers(self):
        return True
 
    def test_add_floats(self):
        return True
 
    def test_add_strings(self):
        return True
 
if __name__ == '__main__':
    unittest.main()