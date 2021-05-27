import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import linspace
from math import radians, cos, sin


def getBasis(i, t):
    result = (math.factorial(3) / (math.factorial(i) * math.factorial(3 - i))) * pow(t, i) * pow(1 - t, 3 - i)

    return result


def matrixMulp(matrix_a, matrix_b):
    width_matrix_a = len(matrix_a[0])
    height_matrix_a = len(matrix_a)

    width_matrix_b = len(matrix_b[0])
    height_matrix_b = len(matrix_b)

    result = [[0] * width_matrix_a for i in range(height_matrix_a)]

    for i in range(height_matrix_a):
        for j in range(width_matrix_a):
            result[i][j] = list([0, 0, 0])
            for k in range(width_matrix_b):
                for l in range(height_matrix_b):
                    result[i][j][k] += matrix_a[i][j][l] * matrix_b[l][k]

    return result


def plot_wireframe(points, ax):
    x = np.array([[point[0] for point in points_row] for points_row in points])
    y = np.array([[point[1] for point in points_row] for points_row in points])
    z = np.array([[point[2] for point in points_row] for points_row in points])
    ax.plot_wireframe(x, y, z, alpha=0.7)


def plot_surface(result_points, ax, color):
    if len(result_points) != 0:
        x = np.array([[point[0] for point in points_row] for points_row in result_points])
        y = np.array([[point[1] for point in points_row] for points_row in result_points])
        z = np.array([[point[2] for point in points_row] for points_row in result_points])
        ax.plot_surface(x, y, z, color=color)


def bezier(points):
    n_patches = m_patches = 3

    count_rows = count_cols = 100

    result_points = [[0] * count_rows for i in range(count_cols)]

    u_values = linspace(0, 1, count_rows)
    v_values = linspace(0, 1, count_rows)
    rows = -1
    for u in u_values:
        cols = -1
        rows += 1
        for v in v_values:
            x = y = z = 0
            cols += 1
            for i in range(n_patches + 1):
                for j in range(m_patches + 1):
                    x += points[i][j][0] * getBasis(i, v) * getBasis(j, u)
                    y += points[i][j][1] * getBasis(i, v) * getBasis(j, u)
                    z += points[i][j][2] * getBasis(i, v) * getBasis(j, u)

            result_points[rows][cols] = (list([x, y, z]))

    return result_points


def main():
    n_patches = 4
    m_patches = 4

    points = []
    result_points = []
    turned_points = []

    print('Бикубическая поверхность Безье')
    enter = False
    while True:
        print('\nВведите "1", чтобы ввести координаты контрольных точек')
        print('Введите "2", чтобы повернуть поверхность Безье на угол')
        print('Введите "3", чтобы вывести поверхности Безье на экран')
        print('Введите "0", чтобы выйти из программы')
        command = int(input('> '))
        if command == 1:
            points = [[0] * n_patches for i in range(m_patches)]
            turned_points = []
            enter = True
            print('\nВведите координаты 16-и контрольных точек\n')

            for i in range(4):
                for j in range(4):
                    point = list(map(float, input(f'Координаты [{i + 1}][{j + 1}] точки: ').split(',')))
                    points[i][j] = point
            result_points = bezier(points.copy())

        elif command == 2:
            if not enter:
                print('\nВы еще не ввели координаты точек')
            else:
                turn_x = radians(float(input('Введите угол поворота относительно оси Х в градусах: ')))
                turn_y = radians(float(input('Введите угол поворота относительно оси Y в градусах: ')))
                turn_matrix_x = [[1, 0, 0],
                                 [0, cos(turn_x), -sin(turn_x)],
                                 [0, sin(turn_x), cos(turn_x)]]
                turn_matrix_y = [[cos(turn_y), 0, sin(turn_y)],
                                 [0, 1, 0],
                                 [-sin(turn_y), 0, cos(turn_y)]]
                turned_points = matrixMulp(matrixMulp(result_points, turn_matrix_x), turn_matrix_y)

        elif command == 3:
            if not enter:
                print('\nВы еще не ввели координаты точек')

            else:
                plt.figure()
                ax = plt.axes(projection='3d')
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.set_zlabel('Z')
                plt.title('Бикубическая поверхность Безье')
                plot_wireframe(points, ax)
                plot_surface(result_points, ax, 'orange')
                plot_surface(turned_points, ax, 'red')
                plt.show()

        elif command == 0:
            quit()


main()
