import matplotlib.pyplot as plt
import math
import random


def getBasis(i, t, n):
    result = (math.factorial(n - 1)/(math.factorial(i)*math.factorial(n - 1 - i))) * pow(t, i) * pow(1 - t, n - 1 - i)
    return result


def bezier(points, n):
    result_points = []

    step = 0.01
    if n <= 4:
        t = 0

        while t <= 1:
            x = y = 0

            for i in range(n):
                temp = getBasis(i, t, n)
                x += points[i][0] * temp
                y += points[i][1] * temp
            result_points.append(list([x, y]))
            t += step

    else:
        num_points = 0
        for i in range(0, len(points)):
            num_points += 1
            if num_points % 4 == 0:
                mid_coord_x = (points[i - 1][0] + points[i][0]) / 2
                mid_coord_y = (points[i - 1][1] + points[i][1]) / 2
                temp = points[i]
                points[i] = list([mid_coord_x, mid_coord_y])
                points.insert(i+1, temp)
                num_points += 1

        k = math.ceil(num_points / 4)
        num = 0
        it = 0
        minus = -1
        for z in range(0, k):
            t = 0

            num += 4
            it += 1
            minus += 1
            if z == k - 1 and num_points < k * 4:
                while t <= 1:
                    x = y = 0
                    j = -1
                    for i in range(num - 4 - minus, num - (k*4 - num_points)):
                        j += 1
                        temp = getBasis(j, t, num - (k*4 - num_points) - (num - 4 - minus))
                        x += points[i][0] * temp
                        y += points[i][1] * temp
                    result_points.append(list([x, y]))
                    t += step

            else:
                while t <= 1:
                    x = y = 0

                    j = -1
                    for i in range(num - 4 - minus, num - minus):
                        j += 1
                        temp = getBasis(j, t, 4)
                        x += points[i][0] * temp
                        y += points[i][1] * temp
                    result_points.append(list([x, y]))
                    t += step

    return result_points


def main():
    points = []
    num_points = 0
    ax = plt.axes()
    while True:
        print('Введите "1", чтобы ввести координаты точек')
        print('Введите "2", чтобы изменить координаты точек')
        print('Введите "3", чтобы вывести график')
        print('Введите "0", чтобы выйти из программы')
        command = int(input('> '))

        if command == 2:
            if len(points) == 0:
                print('Вы еще не ввели координаты точек, поэтому невозможно изменить их')
            else:
                while True:
                    print('Координаты какой точки вы хотите изменить?')
                    print('Введите 0, если хотите выйти из пункта изменения координат')
                    num_point = int(input('> '))
                    if num_point == 0:
                        break
                    while num_point > num_points:
                        print('Данной точки не существует, введите другую')
                        num_point = int(input('> '))
                    print('Старые координаты точки', num_point, ': ', points[num_point-1])
                    point = list(map(int, input(f'Новые координаты точки {num_point}: ').split(',')))
                    points[num_point-1] = point

        elif command == 1:
            n = int(input('Введите количество точек: '))
            print('Введите "1", если хотите сами задать координаты точек')
            print('Введите "2", если хотите, чтобы координаты точек выбрались случайно')
            print('Введите "0", чтобы выйти из программы')
            command_1 = int(input('> '))
            if command_1 == 1:
                for i in range(0, n):
                    point = list(map(int, input(f'Координаты {i+1} точки: ').split(',')))
                    points.append(point)
                num_points = len(points)

            elif command_1 == 2:
                for i in range(0, n):
                    point = list([random.randint(0, 20), random.randint(0, 10)])
                    points.append(point)
                num_points = len(points)
            elif command_1 == 3:
                quit()

        elif command == 3:
            if len(points) == 0:
                print('Вы еще не ввели ни одной точки\n')
            else:
                result_points = bezier(points.copy(), n)
                plt.plot(*zip(*points))[0]
                plt.plot(*zip(*result_points))[0]
                ax.legend(['Заданая ломаная', 'Составная кривая Безье'])
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                plt.show()

        elif command == 0:
            quit()


main()
