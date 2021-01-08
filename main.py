#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 09:25:49 2021

@author: tarnjotbains

This is a script that uses pyQtGraph and BoidSim to visualize 100 boids. 
"""

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
from boids import BoidSim

#-----------------------------------------------------------------------------
#                               Config
#-----------------------------------------------------------------------------
NUMBOIDS = 50
XAXISMIN= -500
XAXISMAX = 500
YAXISMIN = -500
YAXISMAX = 500
#-----------------------------------------------------------------------------


def update():
    """
    Updates the plot with new boid positions. 

    Returns
    -------
    None.

    """
    global p1, sim, curve
    sim.move_all_boids_to_new_positions()
    curve.setData(x= sim.boids[:,0], y= sim.boids[:,1]) 



#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
    #mw = QtGui.QMainWindow()
#   mw.resize(800,800)

win = pg.GraphicsLayoutWidget(show=True, title="Boids Simulation")
win.resize(1920,1080)
win.setWindowTitle('Boids Simulation')

    # Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

p1 = win.addPlot(title="A flock of Boids")
p1.setRange(xRange=[XAXISMIN,XAXISMAX])
p1.setRange(yRange=[YAXISMIN ,YAXISMAX])

sim = BoidSim(NUMBOIDS) 

curve = p1.plot(x= sim.boids[:,0], y= sim.boids[:,1], pen=None, symbol='t', 
                symbolPen=None, symbolSize=20, symbolBrush=(195,46,212))
    
timer = QtCore.QTimer()
timer.timeout.connect(update) 
timer.start(10)
    
            