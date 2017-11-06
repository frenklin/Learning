#!/usr/bin/env python
"""Search triangles in graph"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import time
import random
import matplotlib.pyplot as plt


NSIZE = 500

# Test/debug data
#          A  B  C  D
graph1 = [[0, 1, 1, 1], #A
          [1, 0, 1, 0], #B
          [1, 1, 0, 1], #C
          [1, 0, 1, 0]] #D
#          A  B  C  D        
graph2 = [[0, 1, 1, 0], #A
          [1, 0, 1, 0], #B
          [1, 1, 0, 0], #C
          [0, 0, 0, 0]] #D
#          A  B  C  D       
graph3 = [[0, 1, 1, 0], #A
          [1, 0, 1, 0], #B
          [1, 1, 0, 1], #C
          [0, 0, 1, 0]] #D
#          A  B  C  D  E     
graph4 = [[0, 0, 1, 1, 1], #A
          [0, 0, 0, 1, 0], #B
          [1, 0, 0, 0, 1], #C
          [1, 1, 0, 0, 1], #D
          [1, 0, 1, 1, 0]] #E

def get_graph(nsize):
    """generate random graph"""
    result = []
    for i in range(0, nsize):
        row = []
        for j in range(0, nsize):
            rnd_v = 0 if random.random() > 0.4 else 1
            row.append(rnd_v)
        result.append(row)
    for i in range(0, nsize):
        result[i][i] = 0
        for j in range(i+1, nsize):
            result[i][j] = result[j][i]
    return result

def find_triangles1(graph, n):
    """ bruteforce search triangles"""
    triangles = []
    for i in range(0, n-1):
        for j in range(i+1, n-1):
            if graph[i][j] > 0:
                for k in range(j+1, n):
                    if graph[i][k] > 0 and graph[k][j] > 0:
                        triangles.append([i, j, k])
    return triangles

def find_triangles2(graph , n):
    """ bruteforce search triangles cycle by indexes"""
    triangles = []
    for i in range(0, n-1):
        for j in range(i+1, n-1):
            if graph[i][j] > 0:
                pervious_index = j
                if graph[i][j] > 1:
                    k = graph[i][j]
                else:
                    k = j + 1
                while True:
                    if graph[i][k] > 0:
                        if graph[i][pervious_index] == 1:
                            graph[i][pervious_index] = k
                            pervious_index = k
                        if graph[k][j] > 0:
                            triangles.append([i, j, k])
                    if graph[i][k] > 1:
                        k = graph[i][k]
                    else:
                        k = k + 1
                    if k > n - 1:
                        break
    return triangles

#def find_triangles3(graph, n):
#    """"""
#    triangles = []
##    edges = {}
#    for i in range(0, n):
#        edge = []
#        for j in range(i, n):
#            if(graph[i,j]>0):
#                edge.append(j)
#        edges[i] = edge                             #     0 ->  2,3,4
#    for edge in list(edges.keys()):                 #     2 ->  0,3
#        for i in len(edges[edge]):                  #     3 ->  0,2
#            if                                      #     4 ->  0
    



def get_calc_time(func, full_size_graph, steps):
    """Mesure computation time"""
    result = []
    for i in range(1, steps):
        start_calc = time.process_time()
        func(full_size_graph, i)
        result.append(time.process_time()-start_calc)
    return result


#def test():
#    """test"""
#    gr = get_graph(30)
#    print(len(find_triangles1(gr)))
#    find_triangles2(gr)
#    print(gr)
#    print find_triangles(graph2)
#    print find_triangles(graph3)
#    print find_triangles(graph4)


def run_and_plot():
    """Run & plot"""
    res1 = get_calc_time(find_triangles1, RND_GRAPH, NSIZE)
    res2 = get_calc_time(find_triangles2, RND_GRAPH, NSIZE)
    plt.plot(res1, label="Bruteforce")
    plt.plot(res2, label="Optimized")
    plt.tight_layout()
    plt.legend()

if __name__ == '__main__':
    RND_GRAPH = get_graph(NSIZE)
    #test()
    run_and_plot()
    #run_and_plot_multiproc()
    plt.show()
