import sys
sys.path.append('./../') # allows us to fetch files from the project root
import unittest
from modules.open_digraph import *

#initialisation tests for both open_digraphs and nodes
class InitTest(unittest.TestCase):

  def test_init_node(self):
    n0 = node(0, 'i', [], [1])
    self.assertEqual(n0.id, 0)
    self.assertEqual(n0.label, 'i')
    self.assertEqual(n0.parents, [])
    self.assertEqual(n0.children, [1])
    self.assertIsInstance(n0, node)

  def test_init_digraph(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1,'r',[0],[])
    g = open_digraph([0],[1],[n0,n1])
    self.assertEqual(g.nodes, {0:n0,1:n1})
    self.assertEqual(g.inputs, [0])
    self.assertEqual(g.outputs, [1])
    self.assertIsInstance(g, open_digraph)

#node tests
class NodeTest(unittest.TestCase):
  def setUp(self):
    self.n0 = node(0, 'a', [], [1])
    self.n1 = node(1,'b',[0],[])
  
  def test_string(self):
    self.assertEqual(self.n0.__str__(), "(0, 'a', [], [1])")
    self.assertEqual(self.n1.__str__(), "(1, 'b', [0], [])")
  
  def test_copy(self):
    newnode = self.n0.copy()
    newnode.label = 'n'
    self.assertNotEqual(newnode.label, self.n0.label)
    self.assertIsNot(self.n0,newnode)
    self.assertEqual(self.n0.id, newnode.id)

  def test_gets(self):
    self.assertEqual(self.n0.get_children_ids(), self.n0.children)
    self.assertEqual(self.n0.get_parent_ids(), self.n0.parents)
    self.assertEqual(self.n0.get_id(), self.n0.id)
    self.assertEqual(self.n0.get_label(), self.n0.label)

  def test_sets(self):
    self.n0.set_children_ids([1,2])
    self.assertEqual(self.n0.children, [1,2])
    self.n0.set_children_ids([])
    self.assertEqual(self.n0.children, [])
    self.n0.set_parent_ids([1,2])
    self.assertEqual(self.n0.parents, [1,2])
    self.n0.set_parent_ids([])
    self.assertEqual(self.n0.parents, [])
    self.n0.set_id(-999)
    self.assertEqual(self.n0.id, -999)
    self.n0.set_label('test')
    self.assertEqual(self.n0.label, 'test')

  def test_adds(self):
    self.n0.add_child_id(999)
    self.assertIn(999, self.n0.children)
    self.n0.add_parent_id(999)
    self.assertIn(999, self.n0.parents)

  def test_remove(self):
    n3 = node(3,'c',[4,4,4], [])
    n4 = node(4,'d',[], [3,3,3])
    self.n0.remove_child_id(1)
    self.assertNotIn(1, self.n0.get_children_ids())
    self.n1.remove_parent_id(0)
    self.assertNotIn(0, self.n1.get_parent_ids())
    n3.remove_parent_id_all(4)
    n4.remove_child_id_all(3)
    self.assertEqual(n3.get_parent_ids(), [])
    self.assertEqual(n4.get_children_ids(), [])
    

#open_digraph tests
class DigraphTest(unittest.TestCase):
  def setUp(self):
    self.n0 = node(0, 'i', [], [1])
    self.n1 = node(1,'r',[0],[])
    self.g = open_digraph([0],[1],[self.n0,self.n1])

  def test_string(self):
    self.assertEqual(self.g.__str__(), "([0], [1], {0: node(0, 'i', [], [1]), 1: node(1, 'r', [0], [])})")

  def test_copy(self):
    gbis = self.g.copy()
    self.assertIsNot(self.g, gbis)
    self.assertIsNot(self.g.nodes, gbis.nodes)
    self.assertIs(self.g.inputs, gbis.inputs) 
    self.assertIs(self.g.outputs, gbis.outputs) 

  def test_gets(self):
    self.assertEqual(self.g.get_input_ids(), self.g.inputs)
    self.assertEqual(self.g.get_output_ids(), self.g.outputs)
    self.assertEqual(self.g.get_id_node_map(), self.g.nodes)
    self.assertEqual(self.g.get_nodes(), [self.g.nodes[k] for k in self.g.nodes])
    self.assertEqual(self.g.get_nodes_ids(), [k for k in self.g.nodes])
    self.assertEqual(self.g.get_nodes_by_ids(self.g.nodes), [self.g.nodes[k] for k in self.g.nodes])
    self.assertEqual(self.g.get_node_by_id(0), self.g.nodes[0])

  def test_sets(self):
    self.g.set_input_ids([1,2])
    self.assertEqual(self.g.inputs, [1,2])
    self.g.set_input_ids([])
    self.assertEqual(self.g.inputs, [])
    self.g.set_output_ids([])
    self.assertEqual(self.g.outputs, [])
    self.g.set_output_ids([1,2])
    self.assertEqual(self.g.outputs, [1,2])

  def test_adds(self):
    self.g.add_input_id(-999)
    self.assertIn(-999, self.g.inputs)
    self.g.add_output_id(-999)
    self.assertIn(-999, self.g.outputs)

  def test_new_id(self):
    n = self.g.new_id()
    self.assertNotIn(n, self.g.nodes)

  def test_new_edge(self):
    self.g.add_edge(1, 0)
    self.assertIn(1, self.n0.get_parent_ids())
    self.assertIn(0, self.n1.get_children_ids())

  def test_add_node(self):
    longueur = len(self.g.nodes)
    c = self.g.add_node('c',[],[])
    d = self.g.add_node('d',[],[])
    self.assertIn(c, self.g.get_nodes_ids())
    self.assertIn(d, self.g.get_nodes_ids())
    self.assertEqual(len(self.g.nodes), longueur+2)

  def test_add_edges(self):
    c = self.g.add_node('c',[],[])
    d = self.g.add_node('d',[],[])
    self.g.add_edges([(c,d),(c,d),(c,d)])
    self.assertIn(d, self.g.nodes[c].get_children_ids())
    self.assertIn(c, self.g.nodes[d].get_parent_ids())
    self.assertEqual(count_occurences(self.g.nodes[c].get_children_ids(), d), 3)
    self.assertEqual(count_occurences(self.g.nodes[d].get_parent_ids(), c), 3)

  def test_remove_edge(self):
    n0_1 = self.n0.copy()
    n1_1 = self.n1.copy()
    g_1 = self.g.copy()
    self.g.add_edge(1, 0)
    self.g.remove_edge(1, 0)
    self.assertEqual(n0_1, self.n0)
    self.assertEqual(n1_1, self.n1)
    self.assertEqual(self.g, g_1)

  def test_remove_node_by_id(self):
    g_1 = self.g.copy()
    n = self.g.add_node('test',[],[])
    self.g.remove_node_by_id(n)
    self.assertEqual(g_1, self.g)

  def test_well_formed(self):
    gtest = open_digraph([],[],[])
    self.assertTrue(gtest.is_well_formed())
    a = gtest.add_node()
    b = gtest.add_node()
    gtest.add_edge(a,b)
    gtest.add_edge(b,a)
    self.assertTrue(gtest.is_well_formed())

  def test_random(self):
    grand = open_digraph.empty()
    grand.random(10,10)
    self.assertTrue(grand.is_well_formed())

  #Assuming that both change_id and change_ids work fine if this one works 
  def test_normalize_ids(self):
    g = open_digraph.empty()
    g.random(5,5)
    g.normalise_ids()
    for k in g.get_nodes_ids():
      self.assertTrue(k < 5 and k >= 0)

  def test_adjacency(self):
    g = open_digraph.empty()
    g.random(10,10)
    a_m = g.adjacency_matrix()
    for j in range(len(a_m)):
      for i in range(len(a_m)):
        if a_m[j][i] != 0 : self.assertIn(g.get_node_by_id(j).get_children_ids() ,i)

  #Assuming that (max/min) (out/in) degree works if their associates work in the node tests.

  def test_graph_from_adjacency(self):
    g1 = open_digraph.empty()
    g1.random(10,10)
    m = g1.adjacency_matrix()
    g2 = open_digraph.empty()
    g2.graph_from_adjacency_matrix(m)
    self.assertEqual(g1,g2)


  def test_iscyclic(self):
    n0 = node(0,"a",[], [])
    n1 = node(1,"b",[], [])
    g = open_digraph([],[], [n0,n1])
    g.add_edge(0,1)
    self.assertFalse(g.is_cyclic())
    g.add_edge(1,0)
    self.assertTrue(g.is_cyclic())

# the following code is called only when
# precisely this file is run 
if __name__ == '__main__': 
  unittest.main() 