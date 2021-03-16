import sys
sys.path.append('./../')
from PIL import Image, ImageDraw
from modules.open_digraph import *
from random import randrange
import math

width = 500
height = 500

image = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image)


class vertex:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def coord(self):
    return (round(self.x), round(self.y))
  def copy(self):
    return vertex(self.x,self.y)
  def __add__(self, vertex):
    return vertex(self.x+vertex.x, self.y+vertex.y)
  def __sub__(self, vertex):
    return vertex(self.x-vertex.x, self.y-vertex.y)
  def __rmul__(self, scalar):
    return vertex(self.x*scalar, self.y*scalar)
  def rotate(self, angle, vertex=vertex(0,0)):
    return vertex+(math.cos(angle)*(self.x-vertex.x), math.sin(angle)*(self.y-vertex.y)) 

def drawarrow(self, v1, v2):
  '''doc : todo'''
  self.line([v1.coord(),v2.coord], 'black')
  s = slope_angle(v1,v2)
  m = (v1+v2)*1/2
  self.line(m.rotate(s + math.pi/4))
  self.line(m.rotate(-math.pi/4))

ImageDraw.ImageDraw.arrow = drawarrow

def drawnode(self, node, vertex, verbose=False):
  '''doc : todo'''
  self.ellipse((vertex.x, vertex.y,1,1), fill='black')
  self.text(vertex+vertex(1,1), node.get_label(), fill='black')
  if verbose : self.text(vertex-vertex(1,1), node.get_id(), fill='black')
ImageDraw.ImageDraw.node = drawnode

def drawgraph(self, graph, method='manual', node_pos=None, input_pos=None, output_pos=None):
  '''doc : todo'''
  if method == 'random' or method == 'rand' :
    layout = random_layout(graph)
    drawgraph(graph, 'manual', layout[0], layout[1], layout[2])
  if method == 'circle' :
    layout = circle_layout(graph)
    drawgraph(graph, 'manual', layout[0], layout[1], layout[2])
  else :
    for k in graph.get_id_node_map() :
      self.node(graph.get_node_by_id(k), node_pos[k])
    for i in range(len(input_pos)) :
      self.arrow(input_pos[i], node_pos[graph.get_input_ids()[i]])
    for i in range(len(input_pos)) :
      self.arrow(output_pos[i], node_pos[graph.get_output_ids()[i]])

ImageDraw.ImageDraw.graph = drawgraph

def random_layout(graph):
  '''doc : todo'''
  graph_node_dic = graph.get_id_node_map()
  graph_inputs = graph.get_input_ids()
  graph_outputs = graph.get_output_ids()
  node_pos = {k:(randrange(0,width), randrange(0,height)) for k in graph_node_dic}
  input_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_inputs]
  output_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_outputs]
  return (node_pos, input_pos, output_pos)

def circle_layout(graph):
  '''doc : todo'''
  v = vertex(3*width/4, 3*height/4)
  size = len(graph.get_nodes())
  graph_inputs = graph.get_input_ids()
  graph_outputs = graph.get_output_ids()
  node_pos = {k:v.rotate(2*math.pi/size, vertex(0,0)) for k in graph.get_id_node_map()}
  input_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_inputs]
  output_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_outputs]
  return (node_pos, input_pos, output_pos)

def slope_angle(v1, v2):
  '''doc : todo'''
  a = (v2.y-v1.y)/(v2.x-v1.x)
  b = v2.y%(a*v2.x)
  vertex(-b/a, 0)
  return math.atan(v1.y/(v1.x+b/a))

g = open_digraph.empty()
g.random(3, 100)
draw.graph(g)
image.save("test.jpg")


