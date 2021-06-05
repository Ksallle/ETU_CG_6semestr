from mpl_toolkits.mplot3d import Axes3D, art3d
import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from math import sqrt, pow, cos, sin, radians, degrees
import math
from itertools import product, combinations

n_patches = 4
m_patches = 4

fig = plt.figure()
ax = plt.axes(projection='3d')
points = [[0] * n_patches for i in range(m_patches)]


class Parallelepiped:
    def __init__(self, z_min, z_max, x_min, x_max, y_min, y_max):
        self.bot_side = np.array([[x_max, y_min, z_min],
                                  [x_max, y_max, z_min],
                                  [x_min, y_max, z_min],
                                  [x_min, y_min, z_min]])

        self.top_side = np.array([[x_max, y_min, z_max],
                                  [x_max, y_max, z_max],
                                  [x_min, y_max, z_max],
                                  [x_min, y_min, z_max]])

        self.x_min_side = np.array([[x_min, y_min, z_min],
                                    [x_min, y_max, z_min],
                                    [x_min, y_max, z_max],
                                    [x_min, y_min, z_max]])

        self.x_max_side = np.array([[x_max, y_min, z_min],
                                    [x_max, y_max, z_min],
                                    [x_max, y_max, z_max],
                                    [x_max, y_min, z_max]])

        self.y_min_side = np.array([[x_min, y_min, z_min],
                                    [x_max, y_min, z_min],
                                    [x_max, y_min, z_max],
                                    [x_min, y_min, z_max]])

        self.y_min_side = np.array([[x_min, y_max, z_min],
                                    [x_max, y_max, z_min],
                                    [x_max, y_max, z_max],
                                    [x_min, y_max, z_max]])

        self.center_bot = np.array([(x_min + x_max)/2, (y_min + y_max)/2, (z_min + z_min)/2])
        self.center_top = np.array([(x_min + x_max) / 2, (y_min + y_max) / 2, (z_min + z_min) / 2])
        self.center_x_min_side = np.array([(x_min + x_min) / 2, (y_min + y_max) / 2, (z_min + z_max) / 2])
        self.center_x_max_side = np.array([(x_max + x_max) / 2, (y_min + y_max) / 2, (z_min + z_max) / 2])
        self.center_y_min_side = np.array([(x_min + x_max) / 2, (y_min + y_min) / 2, (z_min + z_max) / 2])
        self.center_y_max_side = np.array([(x_min + x_max) / 2, (y_max + y_max) / 2, (z_min + z_min) / 2])

    def Painter_algorithm(self, x, y, z):
        depth_bot = sqrt(pow(x-self.center_bot[0], 2) + pow(y-self.center_bot[1], 2) + pow(z-self.center_bot[2], 2))
        depth_top = sqrt(pow(x - self.center_top[0], 2) + pow(y - self.center_top[1], 2) + pow(z - self.center_top[2], 2))
        depth_x_min_side = sqrt(pow(x - self.center_x_min_side[0], 2) + pow(y - self.center_x_min_side[1], 2) +
                                pow(z - self.center_x_min_side[2], 2))
        depth_x_max_side = sqrt(pow(x - self.center_x_max_side[0], 2) + pow(y - self.center_x_max_side[1], 2) +
                                pow(z - self.center_x_max_side[2], 2))
        depth_y_min_side = sqrt(pow(x - self.center_y_min_side[0], 2) + pow(y - self.center_y_min_side[1], 2) +
                                pow(z - self.center_y_min_side[2], 2))
        depth_y_max_side = sqrt(pow(x - self.center_y_max_side[0], 2) + pow(y - self.center_y_max_side[1], 2) +
                                pow(z - self.center_y_max_side[2], 2))

        list_sides_by_depth = []

        list_sides_by_depth.append(depth_bot)
        list_sides_by_depth.append(depth_top)
        list_sides_by_depth.append(depth_x_min_side)
        list_sides_by_depth.append(depth_x_max_side)
        list_sides_by_depth.append(depth_y_min_side)
        list_sides_by_depth.append(depth_y_max_side)

        list_sides_by_depth.sort(reverse=True)

        for i in range(len(list_sides_by_depth)):
            if list_sides_by_depth[i] == depth_bot:
                list_sides_by_depth[i] = self.bot_side
            elif list_sides_by_depth[i] == depth_top:
                list_sides_by_depth[i] = self.top_side
            elif list_sides_by_depth[i] == depth_x_min_side:
                list_sides_by_depth[i] = self.x_min_side
            elif list_sides_by_depth[i] == depth_x_max_side:
                list_sides_by_depth[i] = self.x_max_side
            elif list_sides_by_depth[i] == depth_y_min_side:
                list_sides_by_depth[i] = self.x_min_side
            elif list_sides_by_depth[i] == depth_y_max_side:
                list_sides_by_depth[i] = self.x_max_side

    def move_view(event):
        plt.cla()
        ax.autoscale(enable=True, axis='both')

        elev = ax.elev
        azim = ax.azim


        if event.key == "up":
            elev = elev + 10
        if event.key == "down":
            elev = elev - 10
        if event.key == "left":
            azim = azim - 10
        if event.key == "right":
            azim = azim + 10

        ax.view_init(elev=elev, azim=azim)




        x = -ax.get_xbound()[0] * sin(radians(90 - elev)) * cos(radians(azim))
        y = -ax.get_ybound()[0] * sin(radians(90 - elev)) * sin(radians(azim))
        z = -ax.get_zbound()[0] * cos(radians(90 - elev))

        Parallelepiped.Painter_algorithm(x, y, z)




        lenght = sqrt(pow(x - 0, 2) + pow(y - 0, 2) + pow(z - 0, 2))

        print(lenght)

        # plt.plot([x, 0], [y, 0], [z, 0], color='red')





        print('___________________________________________________________________________')
        print(elev)
        print(azim)

        ax.figure.canvas.draw()


def main():

    result_points = []
    turned_points = []

    print('Бикубическая поверхность Безье')
    print('\nВведите "1", чтобы ввести координаты контрольных точек')
    print('Введите "2", чтобы повернуть поверхность Безье на угол')
    print('Введите "3", чтобы вывести поверхности Безье на экран')
    print('Введите "0", чтобы выйти из программы')
    command = int(input('> '))

    if command == 1:
        turned_points = []
        enter = True
        print('\nВведите координаты 16-и контрольных точек\n')

        # for i in range(4):
        #     for j in range(4):
        #         point = list(map(float, input(f'Координаты [{i + 1}][{j + 1}] точки: ').split(',')))
        #         points[i][j] = point
        # points[0][0] = (-0.75,-0.75,-0.50)
        # points[0][1] = (-0.25,-0.75,0.00)
        # points[0][2] = (0.25,-0.75,0.00)
        # points[0][3] = (0.75,-0.75,-0.50)
        # points[1][0] = (-0.75,-0.25,-0.75)
        # points[1][1] = (-0.25,-0.25,0.50)
        # points[1][2] = (0.25,-0.25,0.50)
        # points[1][3] = (0.75,-0.25,-0.75)
        # points[2][0] = (-0.75,0.25,0.00)
        # points[2][1] = (-0.25,0.25,-0.50)
        # points[2][2] = (0.25,0.25,-0.50)
        # points[2][3] = (0.75,0.25,0.00)
        # points[3][0] = (-0.75,0.75,-0.50)
        # points[3][1] = (-0.25,0.75,-1.00)
        # points[3][2] = (0.25,0.75,-1.00)
        # points[3][3] = (0.75,0.75,-0.50)

    paral = Parallelepiped(1, 2, 1, 2, 1, 2)

    fig.canvas.mpl_connect("key_press_event", paral.move_view)

    plt.show()


main()
