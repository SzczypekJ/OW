
class ComparisonCounter:
    def __init__(self):
        self.comparison_count_points = 0
        self.comparison_count_coords = 0

    # less or equal (<=)
    def le(self, x, y):
        self.comparison_count_coords += 1
        return x <= y