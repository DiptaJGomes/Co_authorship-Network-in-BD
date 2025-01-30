import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the node and edge data
node_df = pd.read_csv("nodes_authors.csv")
edge_df = pd.read_csv("author_edge_pairs.csv")

# Create a graph instance
G = nx.Graph()

# Add nodes
for _, row in node_df.iterrows():
    G.add_node(row["UID"], label=row["Label"])

# Add edges
for _, row in edge_df.iterrows():
    G.add_edge(row["UID1"], row["UID2"])

# Draw the network (Force Directed) Fruchterman-Reingold (force-directed) layout
pos = nx.fruchterman_reingold_layout(G)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12)
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'))
plt.title("Co-authorship Network - Fruchterman-Reingold Layout")
plt.show()

# Draw nodes, edges, and labels
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12)
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'))
plt.title("Co-authorship Network")
plt.show()
