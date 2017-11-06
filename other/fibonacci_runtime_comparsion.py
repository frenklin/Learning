#!/usr/bin/env python
"""Fibonacci algorthms runtime"""
__author__ = "Roman S"
__copyright__ = "Copyleft"

import time
import numpy as np
import matplotlib.pyplot as plt

STEPS = 900

def calc_fib1(arg):
    """Exponential simples/slowest/stright fib calc algo"""
    if arg == 1:
        return 1
    if arg == 0:
        return 0
    return calc_fib1(arg-1)+calc_fib1(arg-2)

def calc_fib2(arg):
    """Polynominal fib calc algo"""
    fn0 = 1
    fn1 = 0
    for i in range(1, arg):
        tmp = fn0
        fn0 = fn0+fn1
        fn1 = tmp
    return fn0

def calc_fib3(arg):
    """Fastest matrix fib computation algo"""
    m_n_matrix = np.array([[0, 1], [1, 1]], dtype=np.dtype('float'))
    f_zero_f_one_matrix = np.array([0, 1])
    pow_matr = np.linalg.matrix_power(m_n_matrix, arg)
    fb_n_fb_n1 = np.dot(pow_matr, f_zero_f_one_matrix)
    return fb_n_fb_n1[0]

def get_calc_time(func, steps):
    """Mesure computation time"""
    start_calc = time.process_time()
    result = []
    for i in range(1, steps):
        func(i)
        result.append(time.process_time()-start_calc)
    return result

def run_and_plot(steps):
    """Run & plot"""
    plot1 = get_calc_time(calc_fib1, 25)
    plot2 = get_calc_time(calc_fib2, steps)
    plot3 = get_calc_time(calc_fib3, steps)

    plt.plot(plot1, label="Exponential")
    plt.plot(plot2, label="Polynominal")
    plt.plot(plot3, label="Matrix")

    plt.tight_layout()
    plt.legend()
    plt.show()

run_and_plot(STEPS)
