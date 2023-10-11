import networkx as nx

G = nx.DiGraph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=5)
G.add_edge("B", "D", weight=10)
G.add_edge("C", "D", weight=3)
G.add_edge("D", "A", weight=7)

shortest_path = nx.shortest_path(G, "A", "D", weight="weight")
shortest_path_length = nx.shortest_path_length(G, "A", "D", weight="weight")

print("Shortest Path:", shortest_path)
print("Shortest Path Length:", shortest_path_length)
