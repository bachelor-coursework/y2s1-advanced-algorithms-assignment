class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex)
        self.adjacency_list[from_vertex].add(to_vertex)

    def remove_edge(self, from_vertex, to_vertex):
        self.adjacency_list[from_vertex].remove(to_vertex)

    def list_outgoing_adjacent_vertex(self, vertex):
        return list(self.adjacency_list.get(vertex, []))

    def list_incoming_adjacent_vertex(self, vertex):
        followers = []
        for v, edges in self.adjacency_list.items():
            if vertex in edges:
                followers.append(v)
        return followers

    def get_all_vertices(self):
        return list(self.adjacency_list.keys())
