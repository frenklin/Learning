#!/usr/bin/env python
"""Search triangles in graph"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import time
import random
import matplotlib.pyplot as plt

# Test/debug data
#        A  B  C  D
graph1 = [[0, 1, 1, 1], #A
         [1, 0, 1, 0],  #B
         [1, 1, 0, 1],  #C
         [1, 0, 1, 0]]  #D
#         A  B  C  D        
graph2 = [[0, 1, 1, 0], #A
         [1, 0, 1, 0],  #B
         [1, 1, 0, 0],  #C
         [0, 0, 0, 0]]  #D
#         A  B  C  D       
graph3 = [[0, 1, 1, 0], #A
         [1, 0, 1, 0],  #B
         [1, 1, 0, 1],  #C
         [0, 0, 1, 0]]  #D
#        A  B  C  D  E     
graph4 = [[0, 0, 1, 1, 1], #A
         [0, 0, 0, 1, 0],  #B
         [1, 0, 0, 0, 1],  #C
         [1, 1, 0, 0, 1],  #D
         [1, 0, 1, 1, 0]]  #E


def get_graph(nsize):
    """generate random graph"""
    result = []
    for i in range(0, nsize):
        row = []
        for j in range(0, nsize):
            rnd_v = 0 if random.random() > 0.5 else 1
            row.append(rnd_v)
        result.append(row)
    for i in range(0, nsize):
        result[i][i] = 0
        for j in range(i+1, nsize):
            result[i][j] = result[j][i]
    return result


def find_triangles1(graph):
    """ bruteforce search triangles"""
    triangles = []
    for i in range(0, len(graph)-1):
        for j in range(i+1, len(graph)):
            if graph[i][j] == 1:
                for k in range(j+1, len(graph)):
                    if graph[i][k] == 1:
                        if graph[k][j] == 1:
                            triangles.append([i, j])
                            triangles.append([i, k])
                            triangles.append([j, k])
    return triangles

def get_calc_time(func, steps):
    """Mesure computation time"""
    result = []
    for i in range(1, steps):
        graph = get_graph(i)
        start_calc = time.process_time()
        func(graph)
        result.append(time.process_time()-start_calc)
    return result


#def test():
#    """test"""
#    print find_triangles(graph1)
#    print find_triangles(graph2)
#    print find_triangles(graph3)
#    print find_triangles(graph4)


def run_and_plot(steps):
    """Run & plot"""
    plot1 = get_calc_time(find_triangles1, steps)

    plt.plot(plot1, label="Bruteforce")

    plt.tight_layout()
    plt.legend()
    plt.show()

run_and_plot(200)
