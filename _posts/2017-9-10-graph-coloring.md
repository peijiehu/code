---
layout: post
title: "Graph Coloring Algorithm"
excerpt: ''
categories: [code]
date:   2017-09-10 22:20:00
comments: true
---

## Graph Coloring Algorithm

Vertex coloring is the most common graph coloring problem. The problem is, given m colors, find a way of coloring the vertices of a graph such that no two adjacent vertices are colored using same color.

Following is the basic Greedy Algorithm to assign colors. It doesn’t guarantee to use minimum colors.

Time Complexity: O(V^2 + E) in worst case.

~~~ python
def graph_coloring(graph, colors):
    res = []
    for node in graph:
        if node in node.neighbors:
            raise Exception('self loop')
        illegal_colors = set()
        for neighbor in node.neighbors:
            if neighbor.color:
                illegal_colors.add(neighbor.color)
        for c in colors:
            if c not in illegal_colors:
                node.color = c
                res.append(node)
                break
    return res

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')

a.neighbors.add(b)
a.neighbors.add(d)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)
c.neighbors.add(d)
d.neighbors.add(a)
d.neighbors.add(c)

graph = [a, b, c, d]
colors = ['red', 'green', 'blue']

for node in graph_coloring(graph, colors):
    print node.label, node.color
~~~
