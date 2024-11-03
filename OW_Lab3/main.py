from algorithms import *
from utils import *
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == "__main__":
    # 1
    # Przykładowe dane
    # X = [(5, 5, 0), (3, 6, -1), (4, 4, 2), (5, 3, -2), (3, 3, 1), (1, 8, -1), (3, 4, 0), (4, 5, 1), (3, 10, 2), (6, 6, -3), (4, 1, 1), (3, 5, -2)]
    X = [(5,5), (3,6), (4,4), (5,3), (3,3), (1,8), (3,4), (4,5), (3,10), (6,6), (4, 1), (3, 5)] 
    

    # X = Gauss(10, 3)
    # X1 = Gauss(5000, 7)
    # X2 = Exponential(5000, 7)
    # X3 = Poisson(5000, 7)
    # print("Gauss:\n", X1)
    # print("Exponential:\n", X1)
    # print("Poisson:\n", X1)

    # Compariser with counter
    compariser1 = ComparisonCounter()
    number_of_criteria = len(X[0])
    # Create a list of points for optimisation
    X_points = [Point(number_of_criteria , point_coords, compariser1) for point_coords in X]

    # 1
    start = time.perf_counter_ns()
    P = naive_nondominated_sort(X_points)
    stop = time.perf_counter_ns()

    print("Punkty niezdominowane P(X):")
    # for point in P:
    #     print(point)
    P_nondominated = points_to_numpy_array(P)
    print(P_nondominated)
    plot_points_with_nondominated(X, P_nondominated)
    alg1_count_points = compariser1.comparison_count_points
    alg1_count_coords = compariser1.comparison_count_coords
    alg1_time = (stop-start)/10**6
    alg1_nondominated_count = len(P)
    print(f"Porównania pary punktów: {compariser1.comparison_count_points}")
    print(f"Porównania pary współrzędnych: {compariser1.comparison_count_coords}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")

    
    # 2
    # Uruchomienie algorytmu
    # Reset Compariser counter
    compariser1.reset_counters()

    start = time.perf_counter_ns()
    P = nondominated_sort_with_filtering(X_points)
    stop = time.perf_counter_ns()

    # print("Punkty niezdominowane P(X):")
    # for point in P:
    #     print(point)
    alg2_count_points = compariser1.comparison_count_points
    alg2_count_coords = compariser1.comparison_count_coords
    alg2_time = (stop-start)/10**6
    alg2_nondominated_count = len(P)
    print(f"Porównania pary punktów: {compariser1.comparison_count_points}")
    print(f"Porównania pary współrzędnych: {compariser1.comparison_count_coords}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")


    # 3
    # Uruchomienie algorytmu
    # Reset Compariser counter
    compariser1.reset_counters()

    start = time.perf_counter_ns()
    P = naive_nondominated_sort_without_filtering(X_points)
    stop = time.perf_counter_ns()

    # print("Punkty niezdominowane P(X):")
    # for point in P:
        # print(point)
    alg3_count_points = compariser1.comparison_count_points
    alg3_count_coords = compariser1.comparison_count_coords
    alg3_time = (stop-start)/10**6
    alg3_nondominated_count = len(P)
    print(f"Porównania pary punktów: {compariser1.comparison_count_points}")
    print(f"Porównania pary współrzędnych: {compariser1.comparison_count_coords}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")


    # 4
    # Reset Compariser counter

    compariser1.reset_counters()

    start = time.perf_counter_ns()
    P = ideal_point_algorithm(X_points)
    stop = time.perf_counter_ns()
        
    alg4_count_points = compariser1.comparison_count_points
    alg4_count_coords = compariser1.comparison_count_coords
    alg4_time = (stop-start)/10**6
    alg4_nondominated_count = len(P)
    print(f"Porównania pary punktów: {compariser1.comparison_count_points}")
    print(f"Porównania pary współrzędnych: {compariser1.comparison_count_coords}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")


    print( "Algorytm |  Por. pkt |  Por. wsp.  | Czas [ms] | Non-dominated count")
    print(f"1. NNDS  | {alg1_count_points:10} | {alg1_count_coords:10} | {alg1_time:9.3f} | {alg1_nondominated_count:8}")
    print(f"2. Filt  | {alg2_count_points:10} | {alg2_count_coords:10} | {alg2_time:9.3f} | {alg2_nondominated_count:8}")
    print(f"3. Wrong | {alg3_count_points:10} | {alg3_count_coords:10} | {alg3_time:9.3f} | {alg3_nondominated_count:8}")
    print(f"4. Ideal | {alg4_count_points:10} | {alg4_count_coords:10} | {alg4_time:9.3f} | {alg4_nondominated_count:8}")
