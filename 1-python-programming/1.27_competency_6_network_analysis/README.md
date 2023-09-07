# Python Competency 6 - Network Analysis

You are managing the command and control of a tool that has been deployed against a targeted enemy machine. The target machine controls enemy missiles in real time, and your tool is designed to modify that control in various ways. 

The real-time operations require extreme speed in communicating with the target, and you've been asked to find the path across the network from your command server to the target that will minimize network delay.

You've been provided with a JSON file ([`network.json`](./network.json)) that contains:
- The IP addresses of 300 computers
- The delay (in microseconds) of the 400 connections between those machines
- The IP address of your command server
- The IP address of the target malicious machine against which your tool has been deployed.

This competency is split up into two sub-modules. You must first implement Competency 6A where you implement the `parse` python module, then Competency 6B where you implement the `graph` python module.

After implementing them, use both of the modules you've created to find the shortest path to the target machine. There is no template; you'll need to write the whole program yourself in `analysis.py`. You will need to do some fancy package importing to use the `graph` and `parse` modules in `analysis.py`. Refer to the [Python Documentation on Packages](https://docs.python.org/3/tutorial/modules.html#packages) for guidance.


## Python Competency 6A Json Parse

Write a module that can parse data from a JSON file. There is a built-in Python module, `json`, that does this automatically. However, unfortunately your work space is isolated from the internet and your Python installation is defective (you're also glad to have this opportunity to practice your Python).

When you are finished with this part you should be able to read the data in `network.json` into a dictionary.

There is a template in [`parse.py`](./competency_6a_json_parser/parse.py). The 2 main functions you must implement are `parse_object()` and `parse_array()`, which will call each other if/when objects and arrays nest inside each other.


## Python Competency 6B Dijkstras

Implement Dijkstra's shortest paths algorithm. There is a template in [`graph.py`](./competency_6b_dijkstras/graph.py). This module will be the core computational engine that will find the shortest path to the target. 

There is also an `Infinity` class that has been implemented for you in [`infinity.py`](./competency_6b_dijkstras/infinity.py) that allows you to represent infinity in the case that there is no path between two points.

The `Graph` class you are tasked with implementing is an example of a **weighted**, **undirected** graph in Graph Theory. If you would like guidance on Graph Theory and Dijkstras Algorithm, check out the following resources:

- [graph-theory.md](./graph-theory.md)
- [Intro to Graph Theory](https://www.youtube.com/watch?v=LFKZLXVO-Dg)
- [Dijkstras's Algorithm](https://www.youtube.com/watch?v=EFg3u_E6eHU)
- [Priority Queues](https://www.youtube.com/watch?v=7z_HXFZqXqc)
