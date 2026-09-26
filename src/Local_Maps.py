import numpy as np
from Map import grid
from Robot_Communication import robots
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

UNKNOWN = 0.5
FREE = 0
OBSTACLE = 1

MAP_SIZE = 10


def create_local_map():

    return np.full(
        (MAP_SIZE, MAP_SIZE),
        UNKNOWN
    )

local_maps = {
    "R1": create_local_map(),
    "R2": create_local_map(),
    "R3": create_local_map()
}


def update_cell(robot_name, x, y, value):

    local_maps[robot_name][y, x] = value


def show_local_map(robot_name):

    local_map = local_maps[robot_name]

    cmap = ListedColormap([
        "white",       # FREE
        "lightgray",   # UNKNOWN
        "black"        # OBSTACLE
    ])

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.pcolormesh(
        np.arange(MAP_SIZE + 1),
        np.arange(MAP_SIZE + 1),
        local_map,
        cmap=cmap,
        vmin=0,
        vmax=1,
        edgecolors="black",
        linewidth=1
    )

    # Show robot position
    x, y = robots[robot_name]

    ax.plot(
        x + 0.5,
        y + 0.5,
        'o',
        markersize=12
    )

    ax.text(
        x + 0.5,
        y + 0.5,
        robot_name,
        ha="center",
        va="center",
        fontsize=10
    )

    ax.set_xlim(0, MAP_SIZE)
    ax.set_ylim(0, MAP_SIZE)

    ax.set_xticks(np.arange(0, MAP_SIZE + 1))
    ax.set_yticks(np.arange(0, MAP_SIZE + 1))

    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.set_title(robot_name + " Local Map")

    ax.set_aspect("equal")

    plt.show()
def sense_environment(R3):

    x, y = robots[R3]

    sensor_cells = [
        (x, y),
        (x, y + 1),
        (x, y - 1),
        (x - 1, y),
        (x + 1, y)
    ]

    for cell_x, cell_y in sensor_cells:

        if cell_x < 0 or cell_x >= MAP_SIZE:
            continue

        if cell_y < 0 or cell_y >= MAP_SIZE:
            continue

        value = grid[cell_y, cell_x]

        print(
            R3,
            "sensed",
            (cell_x, cell_y),
            "=",
            value
        )

        update_cell(
            R3,
            cell_x,
            cell_y,
            value
        )
if __name__ == "__main__":

    print("Robot positions:")

    for robot, position in robots.items():
        print(robot, "=", position)

    print("\nR3 sensing environment...")

    sense_environment("R3")

    print("\nR3 local map:")

    print(local_maps["R3"])

    show_local_map("R3")
