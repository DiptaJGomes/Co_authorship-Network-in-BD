import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the edge list from CSV
df = pd.read_csv("author_edge_pairs.csv")

edges = list(df.itertuples(index=False, name=None))
G = nx.from_edgelist(edges)

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12)
plt.title("Co-authorship Network Graph")
plt.show()
