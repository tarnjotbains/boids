import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot 
import pyqtgraph as pg
import sys 
import os 
from boids import BoidSim

#----------------------------------------------------------------------------------
#                                       Config
#----------------------------------------------------------------------------------

# Number of boids to simulate. 
NUMBOIDS = 50

# Limits of the axis 
XAXISMIN = -500
XAXISMAX = 500
YAXISMIN = -500
YAXISMAX = 500

# Speed is how often the graph gets updated with new boid positions in Milliseconds
SPEED = 10 
#----------------------------------------------------------------------------------

class MainWindow(qtw.QWidget): 
    def __init__ (self, num_boids, x_axis_min, x_axis_max, y_axis_min, y_axis_max, speed): 
        super().__init__() 
        self.setWindowTitle('Boids Simulation')
        self.setLayout(qtw.QVBoxLayout())

        self.plot_boids(num_boids,x_axis_min, x_axis_max, y_axis_min, y_axis_max)

        self.timer= QtCore.QTimer()
        self.timer.setInterval(speed) 
        self.timer.timeout.connect(self.update) 
        self.timer.start()

        self.show()  

    def plot_boids(self,num_boids,x_axis_min, x_axis_max, y_axis_min, y_axis_max): 
        container = pg.PlotWidget() 
        container.hideAxis('bottom')
        container.hideAxis('left')

        self.sim = BoidSim(num_boids)

        container.setRange(xRange=[x_axis_min, x_axis_max])
        container.setRange(yRange=[y_axis_min, y_axis_max])

        self.plot= container.plot(x= self.sim.boids[:,0], y= self.sim.boids[:,1], pen=None, symbol='t', 
                symbolPen=None, symbolSize=20, symbolBrush=(195,46,212))
        
        self.layout().addWidget(container) 

    def update(self):
        """
        Updates the plot with new boid positions. 

        Returns
        -------
        None.

        """
        self.sim.move_all_boids_to_new_positions()
        self.plot.setData(x= self.sim.boids[:,0], y= self.sim.boids[:,1]) 


if __name__ == "__main__":
    app = qtw.QApplication([]) #keeps track of things under the hood. 
    mw = MainWindow(NUMBOIDS, XAXISMIN, XAXISMAX, YAXISMIN, YAXISMAX, SPEED) 
    app.exec_() 
    
            