import numpy as np

def fill2D(arr):
    for i in range(N):
        arr[i] = 1

def print2D(arr):
    size = int(np.sqrt(len(arr)))
    matrix = arr.reshape(size, size).astype(int)
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()
    print(" ")

def albert2D(arr):
    print2D(arr)
    for conf_num in range(1, 2**N):
        for i in range(N):
            if arr[i] == 1:
                arr[i] = -1
                break
            else:
                arr[i] = 1
        print2D(arr)


n = int(input("Введите размер матрицы: "))
N = n**2

arr = np.zeros(N)
fill2D(arr)
albert2D(arr)