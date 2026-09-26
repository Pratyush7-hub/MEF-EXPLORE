import numpy as np
from itertools import combinations

from Robot_Communication import robots, calculate_distance

COMMUNICATION_THRESHOLD = 4

def create_graph():

    graph = {}

    # Every robot is a node
    for robot in robots:

        graph[robot] = []

    # Check every pair of robots
    for robot1, robot2 in combinations(robots.keys(), 2):

        distance = calculate_distance(robot1, robot2)

        # If robots are within communication range
        if distance <= COMMUNICATION_THRESHOLD:

            graph[robot1].append(robot2)
            graph[robot2].append(robot1)

    return graph

def show_graph():

    graph = create_graph()

    print(" DYNAMIC COMMUNICATION GRAPH ")

    for robot in graph:

        print(robot, "->", graph[robot])


# MAIN

if __name__ == "__main__":

    print(" CURRENT ROBOT POSITIONS ")

    for robot, position in robots.items():

        print(robot, "=", position)

    show_graph()