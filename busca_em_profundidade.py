import networkx as nx
import matplotlib.pyplot as plt

import numpy as np
# import random

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


def DFS(Graph, node_start):

    #TODO ver se dá pra botar os atributos abaixo em crete_graph()
    color: dict = {} 
    pos: list = retorno_posicoes(Graph)

    # 1. definição atribuições de cores aos nós do grafo
    for vertex in Graph.nodes() :
        color[vertex] = 'white'
        Graph.nodes[vertex]["color"] = color[vertex]


    color[node_start] = 'gray'
    updateGraph(Graph, pos, color)

    # 2. DFS propriamente dito
    visited = set()
    stack = []

    visited.add(node_start)
    stack.append(node_start) 

    while stack:
        s = stack.pop()
        # impressão do output
        print(s, end = " ")
        for vertex in Graph.neighbors(s):
            if color[vertex] == 'white':
                color[vertex] = 'gray'

            if vertex not in visited:
                stack.append(vertex)
                visited.add(vertex)

            
        color[s] = "yellow" 
        updateGraph(Graph, pos, color)


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

    # 
    try:
        if size_condition:
            for n in graph:
                pos[n] = coordinates[n]
        else:
            print("Houve um erro de tamanho entre Grafo")
    except Exception as e:
        logging.error(traceback.format_exc())


    try:

        # desenho e output
        G = create_graph(graph, pos)
        DFS(G, aresta_inicial)

    except Exception as e:
        logging.error(traceback.format_exc())


    # nx.draw(graph_tree)
    # plt.show()

main()