#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define NUM_VERTS 5

int** create_graph(int num_vertices);
void add_edges(int** graph, int n);
int* find_vertex(int** graph, int val);
int find_edge(int** graph, int src, int dst);
void remove_edge(int** graph, int src, int dst);
void remove_vertex(int** graph, int n);
int min_distance(int** graph, int dist[], int sptSet[]);
int dijkstras(int** graph, int src, int dst);
void print_graph(int** graph);
