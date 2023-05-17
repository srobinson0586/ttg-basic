#include "weighted_graph.h"

/*
*	Use main to create a testing suite to test your implementation
*/
int main(){
	return 0;
}

/*
*  	Creates a graph with an adjacency matrix with num_vertices vertices
* 	params: 
*			int num_vertices - the number of vertices to include in the graph
*	returns:
*			int** - the created adjacency matrix graph
*/
int** create_graph(int num_vertices){
	return NULL;
}

/*
*  	Adds edges to connect random edges in the graph
* 	params: 
*			int** graph - the graph to insert edges into
*			int n 		- number of edges to add into the graph
*	returns:
*			void
*/
void add_edges(int** graph, int n){
	return;
}

/*
*  	Finds a vertex within the graph
* 	params: 
*			int** graph - the graph to search
*			int val 	- the number of the vertex to return
*	returns:
*			int* - vertex you are looking. This is essentially an array that represents the vertex and its associated edges
*/
int* find_vertex(int** graph, int val){
	return NULL;
}

/*
*  	Finds an edge within the graph
* 	params: 
*			int** graph - the graph to search
*			int src 	- the src vertex
*			int dst 	- the dst vertex
*	returns:
*			int - weight of the edge you are looking for, if INT_MAX -> no edge exists
*/
int find_edge(int** graph, int src, int dst){
	return -1;
}

/*
*  	Removes edge in graph by setting the value to INT_MAX (no connection)
* 	params: 
*			int** graph - the graph to use
*			int src 	- the src vertex
*			int dst 	- the dst vertex
*	returns:
*			void
*/
void remove_edge(int** graph, int src, int dst){
	return;
}

/*
*  	Removes a vertex from the graph and shifts the graph (adjacency matrix and adjusts num_nodes)
* 	params: 
*			int** graph - the graph to remove from
*			int n 		- number of the vertex to remove
*	returns:
*			void
*/
void remove_vertex(int** graph, int n){
	return;
}

/*
*  	goes through the unvisited vertexes and finds the one with the shortest distance from set of vertices not in shortest path tree yet
* 	params: 
*			int** graph  - the graph to use
*			int dist[] 	 - array that keeps track of distances from src to that vertex (index corresponds to vertex number)
*			int sptSet[] - array that keeps track of the shortest path tree, determines if that vertex is in tree yet or not
*	returns:
*			int - returns the the number of the vertex with minimum distance
*/
int min_distance(int** graph, int dist[], int sptSet[]){
	return -1;
}

/*
*  	Determines the shortest path from src and dst
* 	params: 
*			int** graph - the graph to use
*			int src 	- the src vertex
*			int dst 	- the dst vertex
*	returns:
*			int - the distance between the two vertices
*/
int dijkstras(int** graph, int src, int dst){
	return -1;
}

/*
*	Destroys the graph
* 	params: 
*			int** graph - the graph to destroy	
*	returns:
*			void
*/
void destroy_graph(int** graph){
	return;
}

/*
*  	Prints the entire graph (edge weight between each node)
* 	params: 
*			int** graph
*	returns:
*			void
*/
void print_graph(int** graph){
	return;
}