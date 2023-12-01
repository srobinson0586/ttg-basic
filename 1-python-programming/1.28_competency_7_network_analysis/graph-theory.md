# Basic Graph Theory

[Back to Competency 7 Assignment](./README.md)

A graph is a collection of *nodes* and *edges*.
- Nodes (also called *vertices*) often represent locations.
- Edges represent connections between nodes.

## Weighted vs Unweighted

A graph can be *weighted* or *unweighted*.
- In an unweighted graph, the edges simply represent connections. If an edge exists between 2 nodes, they are connected; otherwise, they are not.
- A weighted graph has *weights* (often called *lengths*) associated with its edges. Thus, 2 nodes could be connected by an edge with a large weight, they could be connected by an edge with a small weight, or they could not be connected at all. Edge weights are often very convenient for representing the physical distance between 2 points.

An unweighted graph could be a good model for Facebook, where the nodes are the accounts and 2 accounts have an edge between them if they are friends. A weighted graph would be a good model for a map, where nodes are cities and the weights are the driving times between them.

## Directed vs Undirected

A graph can also be *directed* or *undirected*.
- In an undirected graph, each edge represents a connection between 2 nodes in both directions. If node A is connected to node B by an edge, the same edge also connects node B to node A.
- In a directed graph, each edge represents a connection in a specific direction. A could be connected to B, but not B to A.

An undirected graph is a perfect model for Facebook friendships, because they are necessarily 2-way. A directed graph would be a good model for representing boss-employee relationships, because they are not 2-way.

## Examples

As a side-note, the account-friend graph we described earlier could be a very interesting representation of society as a whole. But Facebook could do even better: it could make a weighted, directed graph (again using accounts as nodes), where the edge from account A to account B is weighted by the amount user A likes/comments on posts from user B. Facebook has access to a ton of information about society as a whole from that graph, and they are definitely using it. The takeaway is that you can use graphs to analyze many, many things.

For each of these graphs, describe whether it would make more sense for it to be weighted or unweighted, and directed or undirected.

- nodes: computers
- edges: whether a network connection exists between 2 computers

```text
weighted or unweighted:
directed or undirected:
```

- nodes: computers
- edges: how much network traffic flows from computer A to computer B

```text
weighted or unweighted:
directed or undirected:
```

## Dijkstra's Shortest Paths Algorithm

If we have a weighted graph (we'll assume undirected, for simplicity, but it could also be directed), we often care about finding a path between 2 nodes with the minimum total length. For example, if we have a map of the US with distances between cities, we might want to compute the shortest route from San Diego to D.C. Google maps performs some computation of this kind for navigation.

Edsger Dijkstra (pronounced "Dike-struh"; one of the most famous computer scientists in history; read his quotes) invented an algorithm to compute shortest paths on a graph efficiently. We can summarize the algorithm as follows:

- We will always have the nodes divided into 2 sets:
  - The nodes we have visited (called the *visited* set). We have already computed the shortest path from our source node to all of these nodes. For each of these, we record the length of the shortest path from the source to it.
  - The remaining nodes (called the *remaining* set). We do not yet know the shortest path to these nodes, but we do keep track of an upper bound on the maximum distance from the source to each of them.

- The set of visited nodes starts out empty.

- The remaining set initially contains all the nodes. For the upper bounds, we know the source has distance 0 from itself. For all other nodes, we set the upper bound to infinity, since the distance from the source to each node could theoretically be arbitrarily large.

- Now we repeatedly perform the following:
  - Find the node in the remaining set with minimum upper bound distance from the source. Remove this node from the remaining set and add it to the visited set, labeling its distance from the source with the current upper bound estimate.

  - For all other remaining nodes, check if there is a shorter path to them through the node we just visited than we have previously found (i.e., if the node we just visited has an edge to a remaining node, see if *the distance from the source to the node we just visited* + *the length of the edge from the node we just visited to the remaining node* < *the currenct upper bound distance for that remaining node*). If this is the case, decrease the upper bound estimate to reflect the length of the new shorter path we just found.

The Wikipedia page for the algorithm (linked below) has a good description.

## References

- [Wikipedia | Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra)
- [Wikipedia | Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[Back to Competency 7 Assignment](./README.md)