from graph import Graph


def dfs(graph):
    output = []
    mark = 1
    vertices = graph.get_vertices()
    vertices_marked = {}
    for vertex in vertices:
        vertices_marked[vertex] = False
    for vertex in vertices:
        if not vertices_marked[vertex]:
            pass
