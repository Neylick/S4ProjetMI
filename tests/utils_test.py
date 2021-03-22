import sys
sys.path.append('./../') # allows us to fetch files from the project root
import unittest
from modules.utils import *

class int_list_utils_test(unittest.TestCase):
  
  def test_remove_all(self):
    l = [1,0,0,1,9]
    remove_all(l,1)
    self.assertIn(0,l)
    self.assertIn(9,l)
    self.assertNotIn(1,l)
    self.assertIs(len(l), 3)

  def test_count_occurences(self):
    l = [1,0,0,1,9]
    self.assertEqual( count_occurences(l,0), 2 )
    self.assertEqual( count_occurences(l,1), 2 )
    self.assertEqual( count_occurences(l,9), 1 )
    self.assertEqual( count_occurences(l,10), 0 )
  
  def test_random_list(self):
    self.assertEqual(len(random_int_list(5,5)),5)
    self.assertEqual(random_int_list(0,5), [])

class matrix_test(unittest.TestCase):
  
  def test_random_int_matrix(self):
    self.assertEqual(len(random_int_matrix(5,5)),5)
    for i in range(0,5) : self.assertEqual(len(random_int_matrix(5,5)[i]), 5)

  def test_random_symetric_matrix(self):
    self.assertEqual(len(random_symetric_int_matrix(5,5)), 5)
    for i in range(0,5) : self.assertEqual(len(random_symetric_int_matrix(5,5)[i]), 5)
    r = random_symetric_int_matrix(10,10)
    for j in range(10) :
      self.assertEqual(r[j][j], 0)
      for i in range(10) :
        self.assertEquals(r[i][j], r[j][i])

  def test_random_oriented_matrix(self):
    self.assertEqual(len(random_triangular_int_matrix(5,5)), 5)
    for i in range(0,5) : self.assertEqual(len(random_triangular_int_matrix(5,5)[i]), 5)
    r = random_triangular_int_matrix(10,10)
    for j in range(10) :
      for i in range(10) :
        if r[j][i] != 0 : self.assertEqual(r[i][j],0)

  def test_random_triangular_matrix(self):
    self.assertEqual(len(random_triangular_int_matrix(5,5)), 5)
    for i in range(0,5) : self.assertEqual(len(random_triangular_int_matrix(5,5)[i]), 5)
    r = random_triangular_int_matrix(10,10)
    for j in range(10) :
      self.assertEqual(r[j][j], 0)
      for i in range(10) :
        if i < j : self.assertEqual(r[j][i], 0)

    

if __name__ == '__main__': # the following code is called only when
  unittest.main() # precisely this file is run 