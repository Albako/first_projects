import timeit
import sys
from algorithms.sort import bubble_sort, quick_sort
import random

#Algorytm 1. – własna implementacja sortowania bąbelkowego
def bubble_sort_r(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
# Przykład użycia:
listunia = [1234, 50, 300, 15, 6, 64, 34, 25, 12, 22, 11, 90]
print("Lista przed sortowaniem:", listunia)
bubble_sort_r(listunia)
print("Lista po sortowaniu:", listunia)
print()

#Algorytm 2. – import implementacji sortowania bąbelkowego z zewnętrznej biblioteki – bubble_sort z algorithms.sort
listunia = [1234, 50, 300, 15, 6, 64, 34, 25, 12, 22, 11, 90]
print("Lista przed sortowaniem bąbelkowym:", listunia)
bubble_sort(listunia)
print("Lista po sortowaniu bąbelkowym:", listunia)
print()

#Algorytm 3. – import implementacji sortowania szybkiego z zewnętrznej biblioteki – quick_sort z algorithms.sort
listunia = [1234, 50, 300, 15, 6, 64, 34, 25, 12, 22, 11, 90]
print("Lista przed sortowaniem szybkim:", listunia)
quick_sort(listunia)
print("Lista po sortowaniu szybkim:", listunia)

#Porównanie wydajności importowanych „bubble_sort” oraz „quick_sort”
listunia = [1234, 50, 300, 15, 6, 64, 34, 25, 12, 22, 11, 90]
print("Lista przed sortowaniem bąbelkowym:", listunia)
def measure_bubble_sort_time():
    start_time = timeit.default_timer()
    bubble_sort(listunia)
    end_time = timeit.default_timer()
    return end_time - start_time
bubble_sort(listunia)
print("Lista po sortowaniu bąbelkowym:", listunia)
czas_sortowania = measure_bubble_sort_time()
print(f"Czas sortowania bąbelkowego: {czas_sortowania} sekundy")

#Kod programu z funkcją mierzenia czasu pracy do „Algorytm 3” (w Pythonie)
listunia = [1234, 50, 300, 15, 6, 64, 34, 25, 12, 22, 11, 90]
print("Lista przed sortowaniem szybkim:", listunia)
def measure_quicksort_time():
    start_time = timeit.default_timer()
    quick_sort(listunia)
    end_time = timeit.default_timer()
    return end_time - start_time
quick_sort(listunia)
print("Lista po sortowaniu szybkim:", listunia)
czas_sortowania_quicksort = measure_quicksort_time()
print(f"Czas sortowania quicksort: {czas_sortowania_quicksort} sekundy")

#Kod programu mającego za zadanie porównać wydajność „Algorytm 2” oraz „Algorytm 3”
sys.setrecursionlimit(100000)
def generate_sorted_data(size, sorted_percentage, reverse_sorted=False, proper_sorted_percentage=None):
    data = [i for i in range(size)]
    random.shuffle(data)
    if reverse_sorted:
        sorted_size = int(size * sorted_percentage)
        data[-sorted_size:] = sorted(data[-sorted_size:], reverse=True)
    elif proper_sorted_percentage is not None:
        sorted_size = int(size * proper_sorted_percentage)
        data[:sorted_size] = sorted(data[:sorted_size])
    else:
        sorted_size = int(size * sorted_percentage)
        data[:sorted_size] = sorted(data[:sorted_size])
    return data
def measure_sorting_time(sort_function, data):
    start_time = timeit.default_timer()
    sort_function(data)
    end_time = timeit.default_timer()
    return end_time - start_time
def compare_sorting_algorithms(size):
    sorted_percentages = [0.25, 0.5, 1.0]
    for sorted_percentage in sorted_percentages:
        data_bubble_random = generate_sorted_data(size, sorted_percentage)
        data_quick_random = data_bubble_random.copy()
        data_bubble_reverse = generate_sorted_data(size, sorted_percentage, reverse_sorted=True)
        data_quick_reverse = data_bubble_reverse.copy()
        data_bubble_proper = generate_sorted_data(size, sorted_percentage, proper_sorted_percentage=sorted_percentage)
        data_quick_proper = data_bubble_proper.copy()
        time_bubble_random = measure_sorting_time(bubble_sort,data_bubble_random)
        time_quick_random = measure_sorting_time(quick_sort,data_quick_random)
        time_bubble_reverse = measure_sorting_time(bubble_sort,data_bubble_reverse)
        time_quick_reverse = measure_sorting_time(quick_sort,data_quick_reverse)
        time_bubble_proper = measure_sorting_time(bubble_sort,data_bubble_proper)
        time_quick_proper = measure_sorting_time(quick_sort,data_quick_proper)
        print(f"Rozmiar danych: {size}, Stopień posortowania: {sorted_percentage * 100}% (Losowo)")
        print(f"Czas sortowania bąbelkowego: {time_bubble_random} sekundy")
        print(f"Czas sortowania quicksort: {time_quick_random} sekundy")
        print()
        print(f"Rozmiar danych: {size}, Stopień posortowania: {sorted_percentage * 100}% (Odwrotnie posortowane)")
        print(f"Czas sortowania bąbelkowego: {time_bubble_reverse} sekundy")
        print(f"Czas sortowania quicksort: {time_quick_reverse} sekundy")
        print()
        print(f"Rozmiar danych: {size}, Stopień posortowania: {sorted_percentage * 100}% (Właściwie posortowane)")
        print(f"Czas sortowania bąbelkowego: {time_bubble_proper} sekundy")
        print(f"Czas sortowania quicksort: {time_quick_proper} sekundy")
        print()

compare_sorting_algorithms(1000)
compare_sorting_algorithms(5000)
compare_sorting_algorithms(10000)
