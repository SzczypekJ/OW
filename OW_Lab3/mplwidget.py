# -*- coding: utf-8 -*-
"""Definition of widget class for embeding matplotlib in PySide6 GUI

Classes:
- MplWidget: Widget class for embeding matplotlib in GUI

@Author: Krzysztof Kordal
@Date: 2022
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qtagg import FigureCanvas

from matplotlib.figure import Figure


class MplWidget(QWidget):
    """Widget class for embeding matplotlib in GUI"""
    def __init__(self, parent = None):

        super().__init__(parent)

        # Default position
        # self.default_pos = (0.1, 0.1, 0.85, 0.85)   # axis

        # Prepare canvas with figure with 1 axis
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.figure.canvas = self.canvas
        # self.axis.set_position(self.default_pos)
        
        # Put Canvas in widget layout
        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.addWidget(self.canvas)

    def set_projection_2D(self):
        self.axis.remove()
        self.axis = self.figure.add_subplot(111)

    def set_projection_3D(self):
        self.axis.remove()
        self.axis = self.figure.add_subplot(111, projection='3d')