from enum import Enum
from typing import Any, Optional, Dict, List, Callable
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None

class LinkedList:
    head: Node

    def __init__(self) -> None:
        self.head = None

    def append(self, value: Any) -> None:
        new = Node(value)

        if self.head == None:
            self.head = new
        else:
            last = self.head
            while (last.next != None):
                last = last.next
            last.next = new

    def pop(self) -> Any:
        if self.head == None:
            return None
        else:
            first = self.head.value
            self.head = self.head.next
            return first

    def __str__(self) -> str:
        lista = str(self.head.value)
        check = self.head.next
        while check != None:
            lista += " -> "
            lista += str(check.value)
            check = check.next
        return lista

    def __len__(self) -> int:
        cnt = 0
        check = self.head
        while check != None:
            cnt += 1
            check = check.next
        return cnt

class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self) -> str:
        lista = str(self._storage.head.value)
        check = self._storage.head.next
        while check != None:
            lista += ", "
            lista += str(check.value)
            check = check.next
        return lista

    def __len__(self) -> int:
        cnt = 0
        check = self._storage.head
        while check != None:
            cnt += 1
            check = check.next
        return cnt

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    index: int
    data: Any

    def __init__(self, index: int, data: Any):
        self.index = index
        self.data = data

    def __str__(self) -> str:
        return str(self.data)

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        self.source = source
        self.destination = destination
        self.weight = weight

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(len(self.adjacencies), data)
        self.adjacencies[vertex] = []
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge = Edge(source, destination, weight)
        for key, value in self.adjacencies.items():
            if key == source:
                value.append(edge)
            elif key == destination:
                value.append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge1 = Edge(source, destination, weight)
        edge2 = Edge(destination, source, weight)
        for key, value in self.adjacencies.items():
            if key == source:
                value.append(edge1)
            elif key == destination:
                value.append(edge2)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        elif edge == 2:
            self.add_undirected_edge(source, destination, weight)
        else:
            return

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        visited = []
        queue = Queue()
        vertex = list(self.adjacencies.keys())[0]
        visited.append(vertex)
        queue.enqueue(vertex)

        while len(queue):
            vertex = queue.peek()
            queue.dequeue()
            visit(vertex, end=" ")

            for key, value in self.adjacencies.items():
                if key == vertex:
                    for i in value:
                        if i.destination not in visited:
                            queue.enqueue(i.destination)
                            visited.append(i.destination)

    def traverse_depth_first(self, vertex: Vertex, visited: List[Vertex], visit: Callable[[Any], None]) -> None:
        visit(vertex, end=" ")
        visited.append(vertex)

        for key, value in self.adjacencies.items():
            if key == vertex:
                for i in value:
                    if i.destination not in visited:
                        vertex = i.destination
                        self.traverse_depth_first(vertex, visited, visit)
                        visited.append(vertex)

    def show(self) -> None:
        graph = nx.DiGraph()
        for key, value in self.adjacencies.items():
            for i in value:
                if key == i.source and i.weight:
                    graph.add_edges_from([(i.source.data, i.destination.data)], weight=i.weight)
                elif key == i.source:
                    graph.add_edges_from([(i.source.data, i.destination.data)])

        pos = nx.spring_layout(graph, k=0.15, iterations=20)
        nx.draw_networkx(graph, pos, node_size=600)

        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

        plt.box(False)
        plt.show()

    def __str__(self) -> str:
        print = ""
        for key, value in self.adjacencies.items():
            print += str(key.index) + " : " + str(key.data) + " ----> "
            print += "["
            for i in value:
                if key == i.source:
                    print += str(i.destination.index) + " : " + str(i.destination.data)
                    print += ", "
                else:
                    print += str(i.source.index) + " : " + str(i.source.data)
                    print += ", "
            print += "]"
            print += "\n"
        return print

def mutual_friends(g: Graph, f0: Any, f1: Any) -> List[Any]:
    mutual_friends = []
    list0 = []
    list1 = []

    for key, value in g.adjacencies.items():
        if key.data == f0:
            for i in value:
                list0.append(i.destination.data)
        if key.data == f1:
            for i in value:
                list1.append(i.destination.data)

    for i in list0:
        if i in list1:
            mutual_friends.append(i)

    return mutual_friends


## GRAF 1 ##
g1 = Graph()

# dodanie wierzchołków
v0 = g1.create_vertex("v0")
v1 = g1.create_vertex("v1")
v2 = g1.create_vertex("v2")
v3 = g1.create_vertex("v3")
v4 = g1.create_vertex("v4")
v5 = g1.create_vertex("v5")

# dodanie krawędzi
g1.add_undirected_edge(v0, v1)
g1.add_undirected_edge(v0, v5)
g1.add_undirected_edge(v2, v3)
g1.add_undirected_edge(v2, v1)
g1.add_undirected_edge(v3, v4)
g1.add_undirected_edge(v4, v1)
g1.add_undirected_edge(v4, v5)
g1.add_undirected_edge(v5, v1)
g1.add_undirected_edge(v5, v2)

## GRAF 2 ##
g2 = Graph()

# dodanie wierzchołków
A = g2.create_vertex("A")
B = g2.create_vertex("B")
C = g2.create_vertex("C")
D = g2.create_vertex("D")

# dodanie krawędzi
g2.add_undirected_edge(A, B)
g2.add_undirected_edge(A, C)
g2.add_undirected_edge(B, D)
g2.add_undirected_edge(C, B)
g2.add_undirected_edge(C, D)

## GRAF 3 ##
g3 = Graph()

# dodanie wierzchołków
VI = g3.create_vertex("VI")
CH = g3.create_vertex("CH")
RU = g3.create_vertex("RU")
PA = g3.create_vertex("PA")
RA = g3.create_vertex("RA")
SU = g3.create_vertex("SU")
CO = g3.create_vertex("CO")
KE = g3.create_vertex("KE")

# dodanie krawędzi
g3.add_undirected_edge(VI, CH)
g3.add_undirected_edge(VI, RU)
g3.add_undirected_edge(VI, PA)
g3.add_undirected_edge(RU, RA)
g3.add_undirected_edge(RU, SU)
g3.add_undirected_edge(PA, CO)
g3.add_undirected_edge(PA, KE)
g3.add_undirected_edge(CO, RU)
g3.add_undirected_edge(CO, VI)


# funkcja mutual_friends()
print("v1 i v5:", mutual_friends(g1, "v1", "v5"))
print("v3 i v0:", mutual_friends(g1, "v3", "v0"))
print()
print("B i C:", mutual_friends(g2, "B", "C"))
print("A i D:", mutual_friends(g2, "A", "D"))
print()
print("VI i CO:", mutual_friends(g3, "VI", "CO"))
print("KE i CH:", mutual_friends(g3, "KE", "CH"))
