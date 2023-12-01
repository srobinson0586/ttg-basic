# Python Competency 7 - Network Analysis

[Back to OVERVIEW](../README.md)

Code: [`parse.py`](./competency_7a_json_parser/parse.py), [`graph.py`](./competency_7b_dijkstras/graph.py), [`analysis.py`](./analysis.py)

## Objectives
This competency will solidify the Python skills gained up until this point and provide hands on experience with the previous module, [JSON](../1.27_json/README.md).

## Network Analysis Implementation Description

You are managing the command and control of a tool that has been deployed against a targeted enemy machine. The target machine controls enemy missiles in real time, and your tool is designed to modify that control in various ways. 

The real-time operations require extreme speed in communicating with the target, and you've been asked to find the path across the network from your command server to the target that will minimize network delay.

You've been provided with a JSON file ([`network.json`](./network.json)) that contains:
- The IP addresses of 300 computers
- The delay (in microseconds) of the 400 connections between those machines
- The IP address of your command server
- The IP address of the target malicious machine against which your tool has been deployed.

This competency is split up into two sub-modules. You must first implement Competency 7A where you implement the `parse` python module, then Competency 7B where you implement the `graph` python module.

After implementing them, use both of the modules you've created to find the shortest path to the target machine. There is no template; you'll need to write the whole program yourself in [`analysis.py`](./analysis.py). You will need to do some fancy package importing to use the `graph` and `parse` modules in [`analysis.py`](./analysis.py). Refer to the [Python Documentation on Packages](https://docs.python.org/3/tutorial/modules.html#packages) for guidance.


### Python Competency 7A JSON Parse

Write a module that can parse data from a JSON file. There is a built-in Python module, `json`, that does this automatically. However, unfortunately your work space is isolated from the internet and your Python installation is defective (you're also glad to have this opportunity to practice your Python).

When you are finished with this part you should be able to read the data in [`network.json`](./network.json) into a dictionary.

There is a template in [`parse.py`](./competency_7a_json_parser/parse.py). The 2 main functions you must implement are `parse_object()` and `parse_array()`, which will call each other if/when objects and arrays nest inside each other.


### Python Competency 7B Dijkstras

Implement Dijkstra's shortest path algorithm. There is a template in [`graph.py`](./competency_7b_dijkstras/graph.py). This module will be the core computational engine that will find the shortest path to the target. 

There is also an `Infinity` class that has been implemented for you in [`graph.py`](./competency_7b_dijkstras/graph.py) that allows you to represent infinity in the case that there is no path between two points.

The `Graph` class you are tasked with implementing is an example of a **weighted**, **undirected** graph in Graph Theory. If you would like guidance on Graph Theory and Dijkstras Algorithm, check out the following resources:

- [Graph Theory](./graph-theory.md)
- [YouTube | Intro to Graph Theory](https://www.youtube.com/watch?v=LFKZLXVO-Dg)
- [YouTube | Dijkstras's Algorithm](https://www.youtube.com/watch?v=EFg3u_E6eHU)
- [YouTube | Priority Queues](https://www.youtube.com/watch?v=7z_HXFZqXqc)

## Assignment
- [ ] 7A: Implement the `parse` module, as described above, in [`parse.py`](./competency_7a_json_parser/parse.py)
  - [ ] You can check the correctness of your `parse` module by running `pytest` in the [competency_7a_json_parser](./competency_7a_json_parser/) folder. 
- [ ] 7B: Implement the `graph` module, as described above, in [`graph.py`](./competency_7b_dijkstras/graph.py) 
- [ ] Implement [`analysis.py`](./analysis.py) as described above using the functions you implemented for modules 7A and 7B to find the shortest path from the command server to the target machine in [`network.json`](./network.json).

[Back to OVERVIEW](../README.md)