from typing import Any, List
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

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


def Gauss(number_of_cols: int, number_of_rows: int, mean: float = 1.0, std_dev: float = 2.5) -> np.ndarray:
    return np.random.normal(mean, std_dev, size=(number_of_rows, number_of_cols))

def Exponential(number_of_cols: int, number_of_rows: int, scale: float = 1.0) -> np.ndarray:
    return np.random.exponential(scale, size=(number_of_rows, number_of_cols))

def Poisson(number_of_cols: int, number_of_rows: int, lam: int = 1) -> np.ndarray:
    return np.random.poisson(lam, size=(number_of_rows, number_of_cols))

def points_to_numpy_array(points_list: List["Point"]) -> np.ndarray:
    return np.array([point.vector for point in points_list])

def plot_points_with_nondominated(X, P_nondominated):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    X = np.array(X)
    P_nondominated = np.array(P_nondominated)
    
    num_criteria = X.shape[1]
    
    if num_criteria == 2:
        # Plotowanie 2D
        plt.scatter(X[:, 0], X[:, 1], c='skyblue', label='Zbiór punktów')
        plt.scatter(P_nondominated[:, 0], P_nondominated[:, 1], c='red', label='Punkty niezdominowane', s=100, edgecolor='k')
        
        plt.xlabel('Kryt. 1')
        plt.ylabel('Kryt. 2')
        plt.title('Wizualizacja punktów z zaznaczonymi punktami niezdominowanymi (2D)')
        plt.legend()
        plt.show()
    elif num_criteria == 3:
        # Plotowanie 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], c='skyblue', label='Zbiór punktów')
        ax.scatter(P_nondominated[:, 0], P_nondominated[:, 1], P_nondominated[:, 2], c='red', label='Punkty niezdominowane', s=100, edgecolor='k')
        
        ax.set_xlabel('Kryt. 1')
        ax.set_ylabel('Kryt. 2')
        ax.set_zlabel('Kryt. 3')
        ax.set_title('Wizualizacja punktów z zaznaczonymi punktami niezdominowanymi (3D)')
        ax.legend()
        plt.show()
    else:
        raise ValueError("Liczba kryteriów musi być równa 2 lub 3, aby można było wykonać wykres.")

def algorithm_metrics_string(count_points, count_coords, time_ms):
    out_text  = f"Porównania pary punktów: {count_points}\n"
    out_text += f"Porównania pary współrzędnych: {count_coords}\n"
    out_text += f"Czas: {time_ms:.3f} [ms]\n"
    return out_text

def algorithm_summary_table_string(results):
    out_text  = "     Algorytm   |  Por. pkt  |  Por. wsp. | Czas [ms] | Non-dominated count\n"
    out_text += "-" * 65 + "\n"

    for result in results:
        out_text += f"{result['name']:15} | {result['count_points']:10} | {result['count_coords']:10} | {result['time']:9.3f} | {result['nondominated_count']:8}\n"
    
    return out_text

def run_algorithm(X, algorithm, compariser, algorithm_name):
    # Ustalamy liczbę kryteriów
    number_of_criteria = len(X[0])
    X_points = [Point(number_of_criteria, point_coords, compariser) for point_coords in X]
    
    compariser.reset_counters()
    start = time.perf_counter_ns()
    P: List[Point] = algorithm(X_points)
    stop = time.perf_counter_ns()
    count_points = compariser.comparison_count_points
    count_coords = compariser.comparison_count_coords
    time_ms = (stop - start) / 10**6
    nondominated_count = len(P)
    
    out_text  = f"Wyniki dla {algorithm_name}:\n"
    out_text += algorithm_metrics_string(count_points, count_coords, time_ms)

    print(out_text)

    # convert Points to numpy for output
    P_out = points_to_numpy_array(P)

    result_dict = {
        "nondominated_points": P_out,
        "name": algorithm_name,
        "count_points": count_points,
        "count_coords": count_coords,
        "time": time_ms,
        "nondominated_count": nondominated_count
    }

    return result_dict, out_text



if __name__ == "__main__":
    print(np.array((1, 2, 3)) < np.array((0, 3, 4)))
