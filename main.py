from algorithms import *
from utils import *

if __name__ == "__main__":
    # 1
    # Przykładowe dane
    X = [(5,5), (3,6), (4,4), (5,3), (3,3), (1,8), (3,4), (4,5), (3,10), (6,6), (4,1), (3,5)]

    # Uruchomienie algorytmu
    start = time.perf_counter_ns()
    P, comparison_count, coordinate_comparison_count = naive_nondominated_sort(X)
    stop = time.perf_counter_ns()

    print("Punkty niezdominowane P(X):")
    for point in P:
        print(point)
    print(f"Porównania pary punktów: {comparison_count}")
    print(f"Porównania pary współrzędnych: {coordinate_comparison_count}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")


    # 2
    # Przykładowe dane
    X = [(5,5), (3,6), (4,4), (5,3), (3,3), (1,8), (3,4), (4,5), (3,10), (6,6), (4,1), (3,5)]

    # Uruchomienie algorytmu
    start = time.perf_counter_ns()
    P, comparison_count, coordinate_comparison_count = nondominated_sort_with_filtering(X)
    stop = time.perf_counter_ns()

    print("Punkty niezdominowane P(X):")
    for point in P:
        print(point)
    print(f"Porównania pary punktów: {comparison_count}")
    print(f"Porównania pary współrzędnych: {coordinate_comparison_count}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")

    # 3
    # Uruchomienie algorytmu
    start = time.perf_counter_ns()
    P, comparison_count, coordinate_comparison_count = naive_nondominated_sort_without_filtering(X)
    stop = time.perf_counter_ns()

    print("Punkty niezdominowane P(X):")
    for point in P:
        print(point)
    print(f"Porównania pary punktów: {comparison_count}")
    print(f"Porównania pary współrzędnych: {coordinate_comparison_count}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")


    # 4
    # Przykładowe dane
    X = [(5,5), (3,6), (4,4), (5,3), (3,3), (1,8), (3,4), (4,5), (3,10), (6,6), (4,1), (3,5)]

    # Uruchomienie algorytmu
    start_time = time.perf_counter_ns()
    P, comparison_count, coordinate_comparison_count = ideal_point_algorithm(X)
    end_time = time.perf_counter_ns()

    # Wyświetlanie wyników
    print("Punkty niezdominowane P(X):")
    for point in P:
        print(point)

    print(f"Porównania pary punktów: {comparison_count}")
    print(f"Porównania pary współrzędnych: {coordinate_comparison_count}")
    print(f"Czas: {(stop-start)/10**6:.3f} [ms]")