import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
import random

import traceback
import logging

def updateGraph(G, pos, color):
    nx.set_node_attributes(G, color, name="color")
    nx.draw(
        G, 
        with_labels=True, 
        pos=pos,
        node_color=retorno_lista_cores(G),
        )
    plt.show()

def retorno_lista_cores(graph):
    colors: dict = {}

    for n in graph.nodes():
        colors[n] = graph.nodes[n]["color"]

    array_colors: list = []
    for i in colors:
        array_colors.append(colors[i])

    return array_colors

def retorno_posicoes(graph):
    
    pos: dict = {}

    for n in graph.nodes():
        pos[n] = graph.nodes[n]["pos"]

    return pos


def create_graph(graph, pos):

    # Inicialização dos nós e chaves
    nodes: list = [] # chaves
    edges: list = [] # relação chave X arestas

    # Formação nís
    nodes: list = list(graph.keys())

    # Formação arestas
    for node in graph:
        for adjacency_node in graph.get(node):
            s = (node, adjacency_node)
            edges.append(s)

    # Criação do grafo
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Atributos de coordenadas
    nx.set_node_attributes(G, pos, name="pos")
    

    return G


# aqui que vem a brincadeira
def DFS(G, s):

    #TODO ver se dá pra botar os dois atributos em crete_graph()
    color: dict = {} 
    pos: list = retorno_posicoes(G)

    λ = {} #vetor de distancia, distância da aresta inicial ao vértice contabilizado
    π = {} #vetor de predecessores, antes de um vértice n qualquer

    for v in G.nodes() :
        color[v] = 'white'
        λ[v] = np.inf
        π[v] = 'null'
        G.nodes[v]["color"] = color[v]


    color[s] = 'gray'
    λ[s] = 0
    Queue = [s]
    
    ## Isso daqui vai repetir muito kkkkkk
    updateGraph(G, pos, color)


    while Queue:
        u = Queue.pop(0)
        for v in G.neighbors(u):
            if color[v] == 'white':
                color[v] = 'gray'
                λ[v] = λ[u] + 1
                π[v] = u
                Queue.append(v)
        color[u] = "black"
        ## Isso daqui vai repetir muito kkkkkk
        updateGraph(G, pos, color)
        
    

    
    

    DFS_tree = nx.create_empty_copy(G)

    for v1, v2, data in G.edges(data=True) :
        if (π[v2] is v1) or (π[v1] is v2 and not nx.is_directed(DFS_tree)):
            DFS_tree.add_edge(v1, v2)
            DFS_tree.nodes[v1]['depth'] = π[v1]
            DFS_tree.nodes[v1]['depth'] = π[v2]

    return DFS_tree


    #
    


def main():
    aresta_inicial = 2
    graph = {
        0 : [1, 3, 4],
        1 : [0, 2, 5],
        2 : [1],
        3 : [0, 5, 6, 7],
        4 : [0],
        5 : [1, 3],
        6 : [3, 7],
        7 : [0, 3, 6],
        8 : []
    }

    coordinates = [
        (223,157),
        (294,270),
        (356,156),
        (86,154),
        (297,43),
        (146,262),
        (40,36),
        (170,41),
        (212,351)
    ]


    coordinates.reverse()

    size_condition: bool = len(coordinates) == len(graph)
    pos: dict = {}
    try:
        if size_condition:
            for n in graph:
                pos[n] = coordinates[n]
        else:
            print("Houve um erro de tamanho entre Grafo")
    except Exception as e:
        logging.error(traceback.format_exc())


    try:
        G = create_graph(graph, pos)
        DFS(G, aresta_inicial)
    except Exception as e:
        print(e)


    # nx.draw(graph_tree)
    # plt.show()

main()