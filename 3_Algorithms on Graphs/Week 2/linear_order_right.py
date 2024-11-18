from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_all_vertices(self):
        vertices_with_outgoing = set(self.graph.keys())

        vertices_with_incoming = set()
        for neighbors in self.graph.values():
            vertices_with_incoming.update(neighbors)

        all_vertices = vertices_with_outgoing.union(vertices_with_incoming)

        return all_vertices
    
    def find_sink(self):
        all_vertices = self.get_all_vertices()

        for vertex in all_vertices:
            if not self.graph[vertex]:  # if vertex has no outgoing edges
                return vertex
        return None  # No sink is found
    
    def remove_sink_from_graph(self, sink):
        for source_vertex in self.graph:
            neighbors = self.graph[source_vertex]
            updated_neighbors = [neighbor for neighbor in neighbors if neighbor != sink]
            self.graph[source_vertex] = updated_neighbors
        
        if sink in self.graph:
            del self.graph[sink]
    
    def linear_order(self):
        order = []
        while self.graph:
            sink = self.find_sink()
            if sink is None:
                raise ValueError("There is a cycle in the graph")
            order.append(sink)
            self.remove_sink_from_graph(sink)
        return order[::-1]
    
if __name__ == "__main__":
    g = Graph()
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    try:
        result = g.linear_order()
        print("Topological Sort Order:", result)
    except ValueError as e:
        print(e)