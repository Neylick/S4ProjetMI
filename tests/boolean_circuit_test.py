import sys
sys.path.append('./../') # allows us to fetch files from the project root
import unittest
from modules.boolean_circuit import *

class BooleanCircuitTest(unittest.TestCase):
  def test_init(self):
    nodeand = node(0, "&", [], [])
    nodeor1 = node(1, "|", [], [])
    nodeor2 = node(2, "|", [], [])
    nodenot = node(3, "~", [], [])
    nodecopy = node(4, "", [], [])
    g = open_digraph([0,2,4],[1],[nodeand, nodeor1, nodeor2, nodecopy, nodenot])
    g.add_edges([(0,1),(3,1),(2,3),(4,2),(4,0)])
    bool_circ(g)

  def to_od(self):
    nodeand = node(0, "&", [], [])
    nodeor1 = node(1, "|", [], [])
    nodeor2 = node(2, "|", [], [])
    nodenot = node(3, "~", [], [])
    nodecopy = node(4, "", [], [])
    g = open_digraph([1],[0,2,4],[nodeand, nodeor1, nodeor2, nodecopy, nodenot])
    g.add_edges([(0,1),(3,1),(2,3),(4,2),(4,0)])
    bc = bool_circ(g)
    self.assertIsInstance(bc.to_od(), open_digraph)

  #is_well_formed is already tested in init

if __name__ == '__main__': 
  unittest.main() 