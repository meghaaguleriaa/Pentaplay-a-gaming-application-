from settings import *
from src.entities.enemy import Enemy
import random


SHIP_TYPES = [
    "enemyBlack3",
    "enemyBlue3",
    "enemyGreen3",
    "enemyRed3"
]


def get_ship_type(ship_types):

    if isinstance(ship_types, str):
        return ship_types

    return random.choice(ship_types)


def create_grid(ship_types="enemyBlack3"):

    enemies = []

    rows = 2
    columns = 7

    start_x = 180
    start_y = 80

    gap_x = 100
    gap_y = 90

    for row in range(rows):

        for col in range(columns):

            x = start_x + col * gap_x
            y = start_y + row * gap_y

            enemies.append(
                Enemy(
                    x,
                    y,
                    get_ship_type(ship_types)
                )
            )

    return enemies


def create_triangle(ship_types="enemyBlue3"):

    enemies = []

    start_x = 330
    start_y = 80

    gap_x = 80
    gap_y = 70

    for row in range(5):

        for col in range(row + 1):

            x = start_x + (col - row / 2) * gap_x
            y = start_y + row * gap_y

            enemies.append(
                Enemy(
                    x,
                    y,
                    get_ship_type(ship_types)
                )
            )

    return enemies


def create_diamond(ship_types="enemyGreen3"):

    enemies = []

    start_x = 360
    start_y = 70

    gap_x = 80
    gap_y = 70

    rows = [
        1,
        3,
        5,
        3,
        1
    ]

    for row, count in enumerate(rows):

        for col in range(count):

            x = start_x + (col - (count - 1) / 2) * gap_x
            y = start_y + row * gap_y

            enemies.append(
                Enemy(
                    x,
                    y,
                    get_ship_type(ship_types)
                )
            )

    return enemies


def create_v(ship_types="enemyRed3"):

    enemies = []

    start_x = 180
    start_y = 70

    gap_x = 90
    gap_y = 70

    for i in range(5):

        enemies.append(
            Enemy(
                start_x + i * gap_x,
                start_y + i * gap_y,
                get_ship_type(ship_types)
            )
        )

        enemies.append(
            Enemy(
                start_x + 720 - i * gap_x,
                start_y + i * gap_y,
                get_ship_type(ship_types)
            )
        )

    return enemies


def create_cross(ship_types=SHIP_TYPES):

    enemies = []

    center_x = WIDTH // 2
    start_y = 70

    gap = 80

    for i in range(5):

        enemies.append(
            Enemy(
                center_x,
                start_y + i * gap,
                get_ship_type(ship_types)
            )
        )

    for i in range(5):

        enemies.append(
            Enemy(
                center_x - 2 * gap + i * gap,
                start_y + 2 * gap,
                get_ship_type(ship_types)
            )
        )

    return enemies


def create_arrow(ship_types=SHIP_TYPES):

    enemies = []

    center_x = WIDTH // 2
    start_y = 70

    gap_x = 80
    gap_y = 70

    rows = [
        1,
        3,
        5,
        7
    ]

    for row, count in enumerate(rows):

        for col in range(count):

            x = center_x + (col - (count - 1) / 2) * gap_x
            y = start_y + row * gap_y

            enemies.append(
                Enemy(
                    x,
                    y,
                    get_ship_type(ship_types)
                )
            )

    enemies.append(
        Enemy(
            center_x,
            start_y + 4 * gap_y,
            get_ship_type(ship_types)
        )
    )

    enemies.append(
        Enemy(
            center_x,
            start_y + 5 * gap_y,
            get_ship_type(ship_types)
        )
    )

    return enemies


def create_hollow_rectangle(ship_types=SHIP_TYPES):

    enemies = []

    start_x = 200
    start_y = 70

    gap_x = 80
    gap_y = 70

    rows = 4
    columns = 8

    for row in range(rows):

        for col in range(columns):

            if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:

                x = start_x + col * gap_x
                y = start_y + row * gap_y

                enemies.append(
                    Enemy(
                        x,
                        y,
                        get_ship_type(ship_types)
                    )
                )

    return enemies