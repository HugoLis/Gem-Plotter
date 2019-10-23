import networkx as nx
import matplotlib.pyplot as plt

#input code here:
letterCode = ["cabfdeighljknm", "imlckgfenbhdja", "kenmbjlcfiagdh"]

#input colors here:
colors = [1,2,3]

def firstOdds (n):
    count = 0
    output = []
    while (count < n):
        output.append(1+2*count)
        count += 1
    return output

def firstEvens (n):
    count = 1
    output = []
    while (count < n+1):
        output.append(2*count)
        count += 1
    return output

def stringToNumber (letterCode):
    output = []
    for char in letterCode:
        output.append((ord(char)-96) * 2)
    return output

def generateNumberCode (strings):
    output = []
    output.append(firstOdds(len(strings[0])))
    output.append(firstEvens(len(strings[0])))
    for i in range(0,3):
        output.append(stringToNumber(strings[i]))
    return output

def generateGraph (numberCode, colors):
    G = nx.Graph()
    for i in range(0,(len(numberCode[0]) )):
        G.add_edge(numberCode[0][i], numberCode[colors[0]+1][i], color='r', weight=2)
        G.add_edge(numberCode[0][i], numberCode[colors[1]+1][i], color='g', weight=2)
        G.add_edge(numberCode[0][i], numberCode[colors[2]+1][i], color='b', weight=2)
        #print(numberCode[0][i], numberCode[colors[0]+1][i], numberCode[colors[1]+1][i], numberCode[colors[2]+1][i])
    return G

numberCode = generateNumberCode(letterCode)
print(numberCode)

G = generateGraph(numberCode, colors)

labels = {0:0}
edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = [G[u][v]['weight'] for u,v in edges]


nx.draw_planar(G, with_labels=labels, edges=edges, edge_color=colors, width=weights)
plt.figure()
nx.draw_spring(G, with_labels=labels, edges=edges, edge_color=colors, width=weights)
plt.figure()
nx.draw_shell(G, with_labels=labels, edges=edges, edge_color=colors, width=weights)
plt.figure()
nx.draw_spectral(G, with_labels=labels, edges=edges, edge_color=colors, width=weights)
plt.figure()
nx.draw_kamada_kawai(G, with_labels=labels, edges=edges, edge_color=colors, width=weights)
plt.show()
