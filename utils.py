import typing
import numpy as np

class ComparisonCounter:
    def __init__(self):
        self.comparison_count_points = 0
        self.comparison_count_coords = 0

    # less or equal (<=)
    def le(self, x, y):
        self.comparison_count_coords += 1
        return x <= y
    

class Point:
    def __init__(self, number_of_cryteria: int, point_coordinates: np.ndarray[float]) -> None:
        self.number_of_cryteria = number_of_cryteria
        self.vector = point_coordinates