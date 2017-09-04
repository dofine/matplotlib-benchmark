# -*- coding: utf-8 -*-
# @Author: dofin
# @Date:   2017-09-04 21:24:57
# @Last Modified by:   dofin
# @Last Modified time: 2017-09-04 23:20:22
import sys
import os
import time
import matplotlib
BACKEND = "Qt5Agg"
matplotlib.use(BACKEND)

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import timeit

import matplotlib.pyplot as plt
import numpy as np


def draw1():

    fig = Figure()
    # A canvas must be manually attached to the figure (pyplot would automatically
    # do it).  This is done by instanciating the canvas with the figure as
    # argument.
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    # continuously draw three figures
    for i in range(1, 4):
        ax.plot([i, i + 1, i + 2], [1, 1, 1])
        ax.set_title('hi mom {i}'.format(i=i))
        ax.grid(True)
        ax.set_xlabel('time')
        ax.set_ylabel('volts')
        # fig.savefig('test_{i}.png'.format(i=i))
        canvas.print_png('test_{i}.png'.format(i=i))
        ax.cla()


def draw2():
    fig, ax = plt.subplots()
    for i in range(1, 4):
        ax.plot([i, i + 1, i + 2], [1, 1, 1])
        ax.set_title('hi mom {i}'.format(i=i))
        ax.grid(True)
        ax.set_xlabel('time')
        ax.set_ylabel('volts')
        fig.savefig('test_{i}.png'.format(i=i + 10))
        ax.cla()


def draw3():
    fig = Figure()
    # A canvas must be manually attached to the figure (pyplot would automatically
    # do it).  This is done by instanciating the canvas with the figure as
    # argument.
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.grid(True)
    ax.set_xlabel('time')
    ax.set_ylabel('volts')
    ax.set_title('hi mom {i}'.format(i=1))
    line1, = ax.plot([1, 2, 3], [1, 1, 1])

    canvas.print_png('test_{i}.png'.format(i=21))
    # continuously draw three figures
    for i in range(2, 4):
        # ax.plot([i, i + 1, i + 2])
        line1.set_data([i, i + 1, i + 2], [1, 1, 1])
        ax.relim()
        ax.autoscale_view(True, True, True)
        ax.set_title('hi mom {i}'.format(i=i))
        canvas.draw()
        canvas.print_png('test_{i}.png'.format(i=i + 20))
        # fig.savefig()
        # ax.cla()


def draw4():

    x = np.linspace(0, 6 * np.pi, 100)
    y = np.sin(x)

    # You probably won't need this if you're embedding things in a tkinter plot...
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(x, y,
                     'r-')  # Returns a tuple of line objects, thus the comma

    for phase in np.linspace(0, 10 * np.pi, 10):
        line1.set_ydata(np.sin(x + phase))
        fig.canvas.draw()
        fig.savefig('test_{phase}.png'.format(phase=phase))


print("Using backend: {}".format(BACKEND))

print(timeit.timeit("draw1()", globals=globals(), number=20))
print(timeit.timeit("draw2()", globals=globals(), number=20))
print(timeit.timeit("draw3()", globals=globals(), number=20))
