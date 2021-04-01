import sys
import matplotlib.pyplot as plt


def matrixMulp(matrix_a, matrix_b):
    w, h = len(matrix_b[0]), len(matrix_a)
    result = [[0 for x in range(w)] for y in range(h)]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


points = [[float(point) for point in [*input(f'Координаты точки {i}: ').split(','), 1]]
          for i in range(1, int(input("Введите количество точек: ")) + 1)]


command = 0


while command != 4:
    print("Нажмите <1>, чтобы вывести изображение фигуры\nНажмите <2>, чтобы отразить фигуру\n"
          "Нажмите <3>, чтобы задать точки для новой фигуры\nНажмите <4>, чтобы выйти")
    command = int(input(">"))
    if command == 1:
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        z = [p[2] for p in points]
        temp = [x, y, z]
        max_length = max(max(temp))
        OX = [0, max_length * 1.25]
        OY = [0, max_length * 1.25]
        OZ = [0, max_length * 1.25]
        null_arr = [0, 0]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, label='parametric curve')
        ax.plot(OX, null_arr, null_arr, label='parametric curve', alpha=0.3)
        ax.plot(null_arr, OY, null_arr, label='parametric curve', alpha=0.3)
        ax.plot(null_arr, null_arr, OZ, label='parametric curve', alpha=0.3)
        ax.legend(['Исходная фигура', 'Ось X', 'Ось Y', 'Ось Z'])
        plt.show()

    elif command == 2:
        T = [[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]
        print("Отразить фигуру относительно плоскости XOY? 1 - да 0 - нет")
        flag = int(input(">"))
        if flag == 1:
            T[2][2] = -1
        flag = 0
        print("Отразить фигуру относительно плоскости YOZ? 1 - да 0 - нет")
        flag = int(input(">"))
        if flag == 1:
            T[0][0] = -1
        flag = 0
        print("Отразить фигуру относительно плоскости ZOX? 1 - да 0 - нет")
        flag = int(input(">"))
        if flag == 1:
            T[1][1] = -1
        flag = 0
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        z = [p[2] for p in points]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z, label='parametric curve')
        mirror = matrixMulp(points, T)
        x1 = [p[0] for p in mirror]
        y1 = [p[1] for p in mirror]
        z1 = [p[2] for p in mirror]
        ax.plot(x1, y1, z1, label='parametric curve', color='orange')
        temp = [x, y, z, x1, y1, z1]
        max_length = max(max(temp))
        OX = [0, max_length * 1.25]
        OY = [0, max_length * 1.25]
        OZ = [0, max_length * 1.25]
        null_arr = [0, 0]
        ax.plot(OX, null_arr, null_arr, label='parametric curve', alpha=0.3)
        ax.plot(null_arr, OY, null_arr, label='parametric curve', alpha=0.3)
        ax.plot(null_arr, null_arr, OZ, label='parametric curve', alpha=0.3)
        ax.legend(['Исходная фигура', 'Отраженная фигура',
                  'Ось X', 'Ось Y', 'Ось Z'])
        ax.set_box_aspect([1, 1, 1])
        plt.show()

    elif command == 3:
        points = [[float(point) for point in [*input(f'Кординаты точки {i}: ').split(
            ','), 1]] for i in range(1, int(input("Введите количество точек: ")) + 1)]
    elif command == 4:
        sys.exit()
    else:
        print("Неверная команда")
