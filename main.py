from dfs import *

# create dummy graph & driver test
my_graph = Graph()
my_graph.add_directed_edge('r', 's')
my_graph.add_directed_edge('t', 'u')
my_graph.add_directed_edge('w', 'x')
my_graph.add_directed_edge('x', 'y')
my_graph.add_directed_edge('r', 'v')
my_graph.add_directed_edge('s', 'w')
my_graph.add_directed_edge('t', 'x')
my_graph.add_directed_edge('u', 'y')
my_graph.add_directed_edge('t', 'w')
my_graph.add_directed_edge('u', 'x')
my_graph.add_directed_edge('a', 'b')
my_graph.add_vertex('z')

print(dfs(my_graph))
