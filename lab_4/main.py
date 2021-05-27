import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from copy import deepcopy


def calculating_four_bit_code(window_left, window_right, window_bot, window_top, point):

    code = 0
    n1 = 0b0001  # левее окна
    n2 = 0b0010  # правее окна
    n3 = 0b0100  # ниже окна
    n4 = 0b1000  # выше окна
    x = point[0]
    y = point[1]

    if x < window_left:
        code = int(bin(code), 2) ^ int(bin(n1), 2)

    if x > window_right:
        code = int(bin(code), 2) ^ int(bin(n2), 2)

    if y < window_bot:
        code = int(bin(code), 2) ^ int(bin(n3), 2)

    if y > window_top:
        code = int(bin(code), 2) ^ int(bin(n4), 2)

    return bin(code)


def algorithm_Cohen_Sutherland(window_left, window_right, window_bot, window_top, lines):

    alg_lines = deepcopy(lines)

    result_lines = []

    for i in range(len(alg_lines)):

        code_1 = calculating_four_bit_code(window_left, window_right, window_bot, window_top, alg_lines[i][0])
        code_2 = calculating_four_bit_code(window_left, window_right, window_bot, window_top, alg_lines[i][1])

        x1 = alg_lines[i][0][0]
        y1 = alg_lines[i][0][1]
        x2 = alg_lines[i][1][0]
        y2 = alg_lines[i][1][1]

        delete_line_flag = False
        swap_flag = False

        while True:

            if int(code_1, 2) == 0 and int(code_2, 2) == 0:
                break

            if int(code_1, 2) & int(code_2, 2) != 0:
                delete_line_flag = True
                break

            if int(code_1, 2) == 0:
                swap_flag = True

                x1, x2 = x2, x1
                y1, y2 = y2, y1
                code_1, code_2 = code_2, code_1

            if x1 < window_left:
                y1 = y1 + (y2 - y1) * (window_left - x1) / (x2 - x1)
                x1 = window_left

            elif y1 < window_bot:
                x1 = x1 + (x2 - x1) * (window_bot - y1) / (y2 - y1)
                y1 = window_bot

            elif x1 > window_right:
                y1 = y1 + (y2 - y1) * (window_right - x1) / (x2 - x1)
                x1 = window_right

            elif y1 > window_top:
                x1 = x1 + (x2 - x1) * (window_top - y1) / (y2 - y1)
                y1 = window_top

            code_1 = calculating_four_bit_code(window_left, window_right, window_bot, window_top, [x1, y1])

        if not delete_line_flag:

            if swap_flag:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
                code_1, code_2 = code_2, code_1
                swap_flag = False

            alg_lines[i][0][0] = x1
            alg_lines[i][1][0] = x2
            alg_lines[i][0][1] = y1
            alg_lines[i][1][1] = y2

            result_lines.append(alg_lines[i])

    return result_lines


def main():

    print('Отсечение отрезков прямоугольным окном')

    while True:

        print('\nВведите "1", чтобы начать работу программы')
        print('Введите "0", чтобы выйти из программы')
        command = int(input('> '))

        if command == 1:

            lines = []

            num_lines = int(input('Введите количество отрезков: '))

            for i in range(num_lines):
                point_first = list(map(float, input(f'\nВведите координаты начала {i + 1}-го отрезка: ').split(',')))
                point_second = list(map(float, input(f'Введите координаты конца {i + 1}-го отрезка: ').split(',')))
                lines.append([point_first, point_second])

            window_ok = False

            while not window_ok:

                window_left = float(input('\nВведите левую границу окна: '))
                window_right = float(input('Введите правую границу окна: '))
                window_bot = float(input('Введите нижнюю границу окна: '))
                window_top = float(input('Введите верхнюю границу окна: '))

                if window_left >= window_right or window_bot >= window_top:
                    print('Вы ввели некорректные границы окна')
                else:
                    window_ok = True

            rect = Rectangle((window_left, window_bot), window_right - window_left, window_top - window_bot,
                             linewidth=1, fill=False, edgecolor='black')

            rect1 = Rectangle((window_left, window_bot), window_right - window_left, window_top - window_bot,
                              linewidth=1, fill=False, edgecolor='black')

            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.add_patch(rect)

            result_lines = algorithm_Cohen_Sutherland(window_left, window_right, window_bot, window_top, lines)

            for i in range(len(lines)):
                x = []
                y = []
                for j in range(2):
                    x.append(lines[i][j][0])
                    y.append(lines[i][j][1])
                plt.plot(x, y, color='blue')

            plt.axis('auto')
            plt.show()

            fig1 = plt.figure()
            ax1 = fig1.add_subplot(111)
            ax1.add_patch(rect1)

            for i in range(len(lines)):
                x = []
                y = []
                for j in range(2):
                    x.append(lines[i][j][0])
                    y.append(lines[i][j][1])
                plt.plot(x, y, color='blue')

            for i in range(len(result_lines)):
                x = []
                y = []
                for j in range(2):
                    x.append(result_lines[i][j][0])
                    y.append(result_lines[i][j][1])
                plt.plot(x, y, color='red')

            plt.axis('auto')
            plt.show()

        elif command == 0:
            quit()


main()
