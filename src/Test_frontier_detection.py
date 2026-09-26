from Robot_Communication import robots
from Local_Maps import sense_environment
from Frontier_Detection import find_frontiers, show_frontiers


print(" SENSING ")

for robot in robots:
    sense_environment(robot)


print("\n FRONTIER CELLS ")

for robot in robots:

    frontiers = find_frontiers(robot)

    print("\n", robot)
    print("Number of frontiers =", len(frontiers))
    print("Frontiers =", frontiers)


print("\n FRONTIER VISUALIZATION ")

for robot in robots:
    show_frontiers(robot)