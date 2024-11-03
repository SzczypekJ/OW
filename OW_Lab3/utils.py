from typing import Any, List
import numpy as np

class ComparisonCounter:
    def __init__(self):
        self.comparison_count_points = 0
        self.comparison_count_coords = 0

    def count_point_comparison(self):
        self.comparison_count_points += 1

    def count_coords_comparison(self):
        self.comparison_count_coords += 1


    def reset_counters(self) -> None:
        self.comparison_count_points = 0
        self.comparison_count_coords = 0

    # Less than (<)
    def lt(self, x, y) -> bool:
        self.count_coords_comparison()
        return x < y

    # Less than or equal (<=)
    def le(self, x, y) -> bool:
        self.count_coords_comparison()
        return x <= y

    # Equal (==)
    def eq(self, x, y) -> bool:
        self.count_coords_comparison()
        return x == y

    # Not equal (!=)
    def ne(self, x, y) -> bool:
        self.count_coords_comparison()
        return x != y

    # Greater than or equal (>=)
    def ge(self, x, y) -> bool:
        self.count_coords_comparison()
        return x >= y

    # Greater than (>)
    def gt(self, x, y) -> bool:
        self.count_coords_comparison()
        return x > y

class Point:
    def __init__(self, number_of_cryteria: int, point_coordinates: np.ndarray[float], compariser: "ComparisonCounter") -> "Point":
        self.number_of_cryteria = number_of_cryteria
        # self.vector = np.array(point_coordinates)
        self.vector = tuple(point_coordinates)

        self.compariser = compariser



    def __lt__(self, other: "Point") -> bool:
        # Less than: returns True if self is lexicographically smaller than other
        if not isinstance(other, Point) or self.number_of_cryteria != other.number_of_cryteria:
            return NotImplemented
        
        self.compariser.count_point_comparison()

        # Compare Points
        is_lt = True
        for i in range(len(self.vector)):
            if not self.compariser.lt(self.vector[i], other.vector[i]):
                is_lt = False
                break

        return is_lt

    def __le__(self, other: "Point") -> bool:
        # Less than or equal: returns True if self is lexicographically smaller or equal to other
        if not isinstance(other, Point) or self.number_of_cryteria != other.number_of_cryteria:
            return NotImplemented
        
        self.compariser.count_point_comparison()

        # Compare Points
        is_le = True
        for i in range(len(self.vector)):
            if not self.compariser.le(self.vector[i], other.vector[i]):
                is_le = False
                break

        return is_le

    def __eq__(self, other: Any) -> bool:
        # Equality: returns True if all coordinates are equal
        if not isinstance(other, Point) or self.number_of_cryteria != other.number_of_cryteria:
            return False
        
        self.compariser.count_point_comparison()

        # Compare Points
        is_eq = True
        for i in range(len(self.vector)):
            if not self.compariser.eq(self.vector[i], other.vector[i]):
                is_eq = False
                break

        return is_eq

    def __ne__(self, other: Any) -> bool:
        # Inequality: returns True if not equal
        if not isinstance(other, Point) or self.number_of_cryteria != other.number_of_cryteria:
            return True
        
        self.compariser.count_point_comparison()

        # Compare Points
        is_ne = False
        for i in range(len(self.vector)):
            if self.compariser.ne(self.vector[i], other.vector[i]):
                is_ne = True
                break

        return is_ne

    def __ge__(self, other: "Point") -> bool:
        # Greater than or equal: returns True if self is lexicographically larger or equal to other
        if not isinstance(other, Point) or self.number_of_cryteria != other.number_of_cryteria:
            return NotImplemented
        
        self.compariser.count_point_comparison()

        # Compare Points
        is_ge = True
        for i in range(len(self.vector)):
            if not self.compariser.ge(self.vector[i], other.vector[i]):
                is_ge = False
                break

        return is_ge

    def __gt__(self, other: "Point") -> bool:
        # Greater than: returns True if self is lexicographically larger than other
        if not isinstance(other, Point) or self.number_of_cryteria != other.number_of_cryteria:
            return NotImplemented
        
        self.compariser.count_point_comparison()

        # Compare Points
        is_gt = True
        for i in range(len(self.vector)):
            if not self.compariser.gt(self.vector[i], other.vector[i]):
                is_gt = False
                break

        return is_gt

    def __repr__(self) -> str:
        return f"Point({self.vector})"
    
    def __len__(self) -> int:
        return len(self.vector)
    
    def __getitem__(self, key) -> Any:
        return self.vector[key]
    
    def __hash__(self) -> Any:
        return hash(self.vector)
    
    def distance_to(self, other: "Point") -> Any:
        return np.sqrt(np.sum( (self[i] - other[i])**2 for i in range(len(self)) ))


def Gauss(number_of_cols: int, number_of_rows: int, mean: float = 3.0, std_dev: float = 2.5) -> np.ndarray:
    return np.random.normal(mean, std_dev, size=(number_of_rows, number_of_cols))

def Exponential(number_of_cols: int, number_of_rows: int, scale: float = 1.0) -> np.ndarray:
    return np.random.exponential(scale, size=(number_of_rows, number_of_cols))

def Poisson(number_of_cols: int, number_of_rows: int, lam: int = 2) -> np.ndarray:
    return np.random.poisson(lam, size=(number_of_rows, number_of_cols))

def points_to_numpy_array(points_list: List["Point"]) -> np.ndarray:
    return np.array([point.vector for point in points_list])



if __name__ == "__main__":
    print(np.array((1, 2, 3)) < np.array((0, 3, 4)))
