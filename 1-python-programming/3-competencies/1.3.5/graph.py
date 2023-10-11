from infinity import Infinity

inf = Infinity()

class Graph:
    """ A class representing weighted, undirected graphs. """
    def _init_(self):
        """ Initialize a set of nodes (strings) and a dictionary of edges.
        The keys of edges are ordered pairs (tuples) of nodes. The
        values are the lengths of the edges connecting those 2 nodes.
        If an edge does not exist, the algorithm will treat it as an edge
        of infinite length. """
        self.nodes = set()
        self.edges = dict()
    def add_node(self, node):
        """ Add node to the graph's set of nodes. """
        self.nodes.add(node)
    def add_edge(self, a, b, length):
        """ Add an edge between nodes `a` and `b` with length `length`. """
    def get_edge_length(self, a, b):
        """ Find the edge length between nodes `a` and `b`.

        If there is an edge that connects them directly, return
        the length of that edge. If there is no edge between them,
        return infinity. """
    def dijkstras(self, src, dst):
        """ Compute the shortest cumulative edge length between nodes
        `src` and `dst` using Dijkstra's shortest path algorith.

        Return a tuple containing the cumulative length of the shortest
        path and a list of the nodes representing the path in order,
        starting with `src` and ending with `dst`.

        If there is no path at all from `src` to `dst`, return `inf` for
        the path length and an empty path. """
if __name__ == "__main__":
    """ Test out your work by creating a small graph and running
    Dijkstra's algorithm on it. Also test out the case where there is
    no path connecting the source and destination. """
