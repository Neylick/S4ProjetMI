import sys
sys.path.append('./../') # allows us to fetch files from the project root
import unittest
from modules.utils import *

class list_utils_test(unittest.TestCase):
  def test_remove_all(self):
    l = [1,0,0,1,9]
    remove_all(l,1)
    self.assertIn(0,l)
    self.assertIn(9,l)
    self.assertNotIn(1,l)
    self.assertIs(len(l), 3)

if __name__ == '__main__': # the following code is called only when
  unittest.main() # precisely this file is run 