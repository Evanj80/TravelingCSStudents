import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

if (len(sys.argv) >= 4):
    vfile = sys.argv[1]
    efile = sys.argv[2]
    output = sys.argv[3]
else:
    print("USE: python net.py vfile efile output",
        "\nvfile = vertices file"
        "\nefile = edges file"
        "\noutput = name for picture"
        "\nExample: python net.py test1-vertices.txt test1-edges.txt test1-net.png"
    ) 
    exit()

vrtx = pd.read_csv(vfile, delimiter=' ',header=None)
edge = pd.read_csv(efile, delimiter=' ',header=None)

G = nx.Graph()
for i in range(1,vrtx[0].size):
    G.add_node(i,pos=(vrtx[1][i],vrtx[2][i]))
for i in range(1,edge[1].size):
    G.add_edge(edge[1][i],edge[2][i])

plt.figure(figsize=(16,12))
nx.draw(
    G,
    with_labels=True,
    font_size=24,
    font_weight='bold',
    font_color='white',
    node_size=2000,
    node_color='teal',
    edge_color='white'
)
plt.savefig(output, transparent=True)

