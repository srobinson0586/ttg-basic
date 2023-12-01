#!/bin/python
# Python Competency 7B Dijkstras

class Infinity:
    """ A class to represent infinity. It has been implemented for you

    This allows us to perform arithmetic and comparisons with infinity
    during graph operations. You can represent edges that don't exist
    with an edge with infinite length. 
    """
    ### This lets us print it out as the unicode infinity sign.
    def __str__(self):
        return chr(0x221e)
    def __repr__(self):
        return self.__str__()

    ### These functions allow all comparisons.
    def __lt__(self, n):
        return False
    def __eq__(self, n):
        rtn = False
        if isinstance(n, Infinity):
            return True
        return rtn
    def __gt__(self, n):
        return not (self < n or self == n)
    def __le__(self, n):
        return self < n or self == n
    def __ge__(self, n):
        return self > n or self == n

    ### These functions allow addition to integers.
    def __add__(self, n):
        return self
    def __radd__(self, n):
        return self + n

class PriorityQueue:
    """
    A class to represent a Priority Queue. It has been implemented for you.

    Attributes
    __________
    d : dict
        a dictionary who's keys represent a graph node, i.e. an IP address (string)
        the values are the distance between that IP and our starting node

    Methods
    _______
    insert
        insert a new key / value pair into d
    update
        update a key's value if there's a new, lesser value
    pop_min
        pop the element in d with the minimum value
    """
    def __init__(self):
        """
        The constructor for the PriorityQueue class.
        """
        self.d = dict()

    def insert(self, key, value):
        """
        Insert a new element {`key` : `value`} into d
        """
        self.d[key] = value

    def update(self, key, value):
        """
        Update an element of d at `key`, if the passed in `value` is less than the current value

        Parameters:
        key : string
            The dictionary's key in question
        value : int
            The new value to potentially store at d[key]
        
        Returns:
            False if d was updated, True otherwise
        """
        rtn = False
        if value < self.d[key]:
            self.d[key] = value
            rtn = True
        return rtn

    def pop_min(self):
        """
        Pop the element in `d` with the minimum value

        Returns:
            A tuple containing the minimum value of `d`, and the index (key) at which it was stored
        """
        min_key = None
        min_value = inf
        for key, value in self.d.items():
            if value <= min_value:
                min_key = key
                min_value = value
        self.d.pop(min_key)
        return min_key, min_value

# used in Graph
inf = Infinity()

class Graph:
    """
    A class to represent a weighted, undirected graph. 
    
    Attributes
    __________
    nodes : set
        a set containing all the nodes (string IPs) in the graph
    edges : dict
        a dictionary who's keys are ordered pairs of nodes  (tuple)
        the values are the lengths of the edges connecting those two nodes (list)
        if an edge does not exist, the algorithm will treat it as an edge of infinite length

    Methods
    _______
    add_node
        add a new node to the graph's `nodes` set
    add_edge
        add a new edge to the graph's `edges` dict
    get_edge_length
        find the edge length between two passed in nodes
    dijkstras
        compute the shortest cumulative edge length between two passed in nodes
        using Dijkstra's shortest path algorithm.
    """

    def __init__(self):
        """ 
        Initialize the Graph class
        
        Initialize a *set* of nodes (strings) and a dictionary of edges.

        The keys of `edges` are ordered pairs (tuples) of nodes. The
        values are the lengths of the edges connecting those 2 nodes.
        If an edge does not exist, the algorithm will treat it as an edge
        of infinite length. 
        """
        # TODO: Implement the function
        pass

    def add_node(self, node):
        """
        Add `node` to the graph's set of nodes. 
        """
        # TODO: Implement the function
        pass

    def add_edge(self, a, b, length):
        """
        Add an edge between nodes `a` and `b` with length `length`. 
        """
        # TODO: Implement the function
        pass

    def get_edge_length(self, a, b):
        """
        Find the edge length between nodes `a` and `b`.

        If there is an edge that connects them directly, return
        the length of that edge. If there is no edge between them,
        return infinity. 
        """
        # TODO: Implement the function
        pass

    def dijkstras(self, src, dst):
        """ 
        Compute the shortest cumulative edge length between nodes
        `src` and `dst` using Dijkstra's shortest path algorithm.

        Return a tuple containing the cumulative length of the shortest
        path and a list of the nodes representing the path in order,
        starting with `src` and ending with `dst`.

        If there is no path at all from `src` to `dst`, return `inf` for
        the path length and an empty path. 
        """
        # TODO: Implement the function
        pass

if __name__ == "__main__":
    """ 
    Test out your work by creating a small graph and running Dijkstra's algorithm on it.
    Also test out the case where there is no path connecting the source and destination. 
    """
    # TODO: Implement the function
    pass
