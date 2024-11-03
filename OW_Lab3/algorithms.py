import numpy as np
import matplotlib.pyplot as plt
import time
from typing import List

from utils import *


# Algorytm naiwny bez filtracji:
# def naive_nondominated_sort(X):
#     n = len(X)
#     P = []
#     dominated = [False] * n  # Tablica śledząca, czy punkt został zdominowany

#     comp_cnt = ComparisonCounter()

#     for i in range(n):
#         if dominated[i]:
#             continue  # Jeśli punkt jest już zdominowany, pomijamy go
#         Y = X[i]
#         for j in range(n):
#             if i == j or dominated[j]:
#                 continue

#             comp_cnt.comparison_count_points += 1

#             # print(f"Iter ({i}, {j}) | Y={Y} Xj={X[j]}")
#             if (comp_cnt.le(Y[0], X[j][0]) and
#                 comp_cnt.le(Y[1], X[j][1])):
#                 # Y dominuje X[j]
#                 # print(f"Del Xj! | Y{Y} <= Xj{X[j]}")
#                 dominated[j] = True
#             elif (comp_cnt.le(X[j][0], Y[0]) and
#                   comp_cnt.le(X[j][1], Y[1])):
#                 # X[j] dominuje Y
#                 # print(f"Del Y! | Xj{X[j]} <= Y{Y}")
#                 dominated[i] = True
#                 break  # Nie ma sensu dalej sprawdzać, Y jest zdominowany
#         if not dominated[i]:
#             P.append(Y)  # Dodajemy Y do listy punktów niezdominowanych

#     return P, comp_cnt.comparison_count_points, comp_cnt.comparison_count_coords
def naive_nondominated_sort(X: List["Point"]):
    n = len(X)
    P = []
    dominated = [False] * n  # Tablica śledząca, czy punkt został zdominowany

    

    for i in range(n):
        if dominated[i]:
            continue  # Jeśli punkt jest już zdominowany, pomijamy go
        Y = X[i]
        for j in range(n):
            if i == j or dominated[j]:
                continue

            # print(f"Iter ({i}, {j}) | Y={Y} Xj={X[j]}")
            if Y <= X[j]:
                # Y dominuje X[j]
                # print(f"Del Xj! | Y{Y} <= Xj{X[j]}")
                dominated[j] = True
            elif X[j] <= Y:
                # X[j] dominuje Y
                # print(f"Del Y! | Xj{X[j]} <= Y{Y}")
                dominated[i] = True
                break  # Nie ma sensu dalej sprawdzać, Y jest zdominowany
        if not dominated[i]:
            P.append(Y)  # Dodajemy Y do listy punktów niezdominowanych

    return P



# Algorytm naiwny z filtracją punktow zdominowanych:
def nondominated_sort_with_filtering(X: List["Point"]):
    P = []  # Lista punktów niezdominowanych
    X_list = X.copy()  # Kopia listy X, aby nie modyfikować oryginału


    while len(X_list) > 0:
        Y = X_list[0]  # Wybieramy pierwszy punkt z listy
        i = 1
        while i < len(X_list):
            X_j = X_list[i]

            # Sprawdzenie czy Y dominuje X_j
            # if (comp_cnt.le(Y[0], X_j[0]) and
            #     comp_cnt.le(Y[1], X_j[1])):
            if Y <= X_j:
                # Y dominuje X_j
                X_list.pop(i)
            elif X_j <= Y:
                # X_j dominuje Y
                X_list.pop(0)  # Usuwamy Y
                Y = X_j  # Aktualizujemy Y
                i = 1  # Resetujemy i, bo lista się zmieniła
            else:
                i += 1

        # Dodajemy Y do listy punktów niezdominowanych
        P.append(Y)
        # Filtracja: usuwamy z X_list wszystkie punkty zdominowane przez Y
        i = 0
        while i < len(X_list):
            point = X_list[i]
            # Sprawdzanie, czy Y dominuje point
            if Y <= point:
                X_list.pop(i)
            else:
                i += 1

        # X_list = [point for point in X_list if not ((Y[0] <= point[0] and Y[1] <= point[1]) )] #and (Y[0] < point[0] or Y[1] < point[1]))]
        # Usuwamy Y z X_list
        if Y in X_list:
            X_list.remove(Y)
        # Sprawdzamy, czy w X_list został tylko jeden punkt
        if len(X_list) == 1:
            P.append(X_list[0])
            break
    return P



# Przykład błędnego wyniku w przypadku usunięcia X(i) i pominięcia filtracji
def naive_nondominated_sort_without_filtering(X: List["Point"]):
    n = len(X)
    P = []
    X_list = X.copy()

    i = 0
    while i < len(X_list):
        Y = X_list[i]
        is_dominated = False
        for j in range(len(X_list)):
            if i == j:
                continue
            if X_list[j] <= Y:
                # X_list[j] dominuje Y
                is_dominated = True
                break
        if not is_dominated:
            P.append(Y)
        # Usuwamy Y z listy, ale nie filtrujemy zdominowanych punktów
        X_list.pop(i)
    return P



# Algorytm naiwny oparty o punkt idealny (szkic):
def calculate_ideal_point(X: List["Point"]):
    k = len(X[0])  # Wymiar przestrzeni
    xmin = Point(k, [min(point[i] for point in X) for i in range(k)], X[0].compariser)
    return xmin

def calculate_distances(X: List["Point"], xmin):
    distances = []
    for idx, point in enumerate(X):
        dist = point.distance_to(xmin)
        distances.append((dist, idx))
    return distances

def ideal_point_algorithm(X: List["Point"]) -> List[Point]:
    P: List[Point] = []  # Lista punktów niezdominowanych
    X_set = set(X)  # Zbiór punktów do przetworzenia

    xmin = calculate_ideal_point(X)

    # Obliczanie odległości do punktu idealnego
    distances = calculate_distances(X, xmin)

    # Sortowanie punktów według odległości od punktu idealnego
    distances.sort()
    sorted_points = [X[idx] for dist, idx in distances]

    for current_point in sorted_points:
        if current_point not in X_set:
            continue  # Punkt został już usunięty
        # Usuwanie zdominowanych punktów przez current_point
        dominated_points = set()
        for point in X_set:
            if point != current_point:
                if current_point <= point:
                    dominated_points.add(point)
        X_set -= dominated_points
        # Dodawanie current_point do P
        if current_point not in P:
            P.append(current_point)
        # Usuwanie current_point z X_set
        X_set.remove(current_point)
        # Sprawdzenie liczby pozostałych punktów
        if len(X_set) == 1:
            remaining_point = next(iter(X_set))
            if remaining_point not in P:
                P.append(remaining_point)
            break
    return P

