import numpy as np

from M04_Local_Maps import local_maps, UNKNOWN, MAP_SIZE
from M02_Robot_Communication import calculate_distance



COMMUNICATION_THRESHOLD = 4


def merge_maps(robot1, robot2):

    distance = calculate_distance(robot1, robot2)

    print(" MAP MERGING ")

    print(robot1, "<->", robot2)
    print("Distance =", round(distance, 2))

    if distance > COMMUNICATION_THRESHOLD:

        print("Communication : LOW")
        print("Map merging : NOT ALLOWED")

        return

    print("Communication : HIGH")
    print("Map merging : ALLOWED")

    map1 = local_maps[robot1]
    map2 = local_maps[robot2]

    original_map1 = map1.copy()
    original_map2 = map2.copy()

    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):

            value1 = original_map1[y, x]
            value2 = original_map2[y, x]

            if value1 != UNKNOWN and value2 == UNKNOWN:

                map2[y, x] = value1

            elif value2 != UNKNOWN and value1 == UNKNOWN:

                map1[y, x] = value2

    print("Map merging completed.")