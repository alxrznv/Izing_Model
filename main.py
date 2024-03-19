import numpy as np
import random

J = -1

def fill2D(arr):
    for i in range(N):
        arr[i] = 1

def E_spin(arr, x, y):
    E = 0

    #1 условие центральный элемент
    if x > 0 and x < n - 1 and y > 0 and y < n - 1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[y + 1][x])

    #2 условие верхний левый
    elif x == 0 and y == 0:
        E = -J * arr[y][x] * (arr[y][n - 1] + arr[y][x + 1] + arr[n - 1][x] + arr[y + 1][x])

    #3 условие верхняя грань
    elif x > 0 and x < n - 1 and y == 0:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][x + 1] + arr[n - 1][x] + arr[y + 1][x])

    #4 условие правый нижний
    elif x == n - 1 and y == n - 1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][0] + arr[y - 1][x] + arr[0][x])

    #5 условие нижняя грань
    elif x > 0 and x < n - 1 and y == n - 1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[0][x])
    #6 условие левая грань
    elif x == 0 and y > 0 and y < n - 1:
        E = -J * arr[y][x] * (arr[y][n - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[y + 1][x])
    #7 условие правая грань
    elif x == n - 1 and y > 0 and y < n - 1:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][0] + arr[y - 1][x] + arr[y + 1][x])
    #8 условие нижний левый
    elif x == 0 and y == n - 1:
        E = -J * arr[y][x] * (arr[y][n - 1] + arr[y][x + 1] + arr[y - 1][x] + arr[0][x])
    #9 условие верхний правый
    elif x == n - 1 and y == 0:
        E = -J * arr[y][x] * (arr[y][x - 1] + arr[y][0] + arr[n - 1][x] + arr[y+1][x])

    return E

def E_system(arr):
    E_sys = 0
    for y in range(n):
        for x in range(n):
            E_sys += E_spin(arr, x, y)

    E_sys /= 2

    return E_sys

def conf_file(array):
    with open(r'C:\Users\User\PycharmProjects\Izing Model\config.txt', 'w') as fout:
        rows, cols = array.shape
        for i in range(rows):
            for j in range(cols):
                fout.write(f'{i} {j} 0 {array[i][j]}\n')


def plot_gp():
    script = """
set terminal png font "Verdana,14" size 1000, 1000
set output "Ising_model-1maxx.png"
plot [-1:4][-1:4] 'config.txt' using ($1-($3/4)):($2-($4/4)):($3/2):($4/2) with vectors notitle, 'config.txt' using 1:2 pt 7 notitle
"""
    with open(r'C:\Users\User\PycharmProjects\Izing Model\plot.plt', 'w') as file:
        file.write(script)

def albert2Dmin(arr):
    arrone = np.ones(N)
    arrone2 = arrone.reshape(n, n)
    min_energy = E_system(arrone2)
    E = 0
    for conf_num in range(1, 2**N):
        for i in range(N):
            if arr[i] == 1:
                arr[i] = -1
                break
            else:
                arr[i] = 1
        arr2 = arr.reshape(n, n)
        E = E_system(arr2)
        if E < min_energy:
            min_energy = E
            conf_file(arr2)
    print(min_energy, 'минимальная энергия')

def albert2Dmax(arr):
    arrone = np.ones(N)
    arrone2 = arrone.reshape(n, n)
    max_energy = E_system(arrone2)
    E = 0
    for conf_num in range(1, 2**N):
        for i in range(N):
            if arr[i] == 1:
                arr[i] = -1
                break
            else:
                arr[i] = 1
        arr2 = arr.reshape(n, n)
        E = E_system(arr2)
        if E > max_energy:
            max_energy = E
            conf_file(arr2)
    print(max_energy, 'максимальная энергия')

n = int(input("Введите размер матрицы: "))
N = n**2
arr = np.zeros(N)
fill2D(arr)

albert2Dmax(arr)
plot_gp()
