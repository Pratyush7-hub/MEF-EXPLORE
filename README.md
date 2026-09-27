# MEF-Explore

## Communication-Constrained Multi-Robot Entropy-Field-Based Exploration

This project focuses on implementing a multi-robot exploration framework for exploring an unknown environment under communication constraints. The complete system is being developed step by step, where each individual component is implemented and tested before integrating it with the next stage.

## Current Implementation

The implementation is being developed in the following sequence:

1. **Map Generation**
   - Creation of a 2D occupancy grid environment
   - 10 × 10 grid with free cells, unknown cells, and obstacles
   - Initial placement of 3 robots in the environment

2. **Robot Communication and Movement**
   - Definition of robot positions and movement
   - Movement in four directions: UP, DOWN, LEFT, and RIGHT
   - Boundary and obstacle checking
   - Calculation of distance between robots
   - Communication based on the distance between robots

3. **Dynamic Communication Graph**
   - Representation of robots as nodes in a communication graph
   - Communication links are created dynamically based on the distance between robots
   - The graph changes as the robots move through the environment

4. **Local Map Generation**
   - Each robot maintains its own local map
   - Robots sense their surrounding cells
   - The sensed information is used to update the corresponding local map

5. **Map Sharing and Map Merging**
   - Communication is divided into high-communication and low-communication conditions
   - High communication allows robots to share their explored map information
   - Low communication allows limited information exchange, such as robot positions
   - Local maps are merged when communication conditions allow map sharing

6. **Frontier Detection**
   - Frontiers are identified from the locally explored maps
   - A frontier represents an unknown cell adjacent to an explored free cell
   - The detected frontiers are used as potential exploration targets

7. **Entropy Calculation**
   - Implementation of the entropy formulation used in the MEF-Explore approach
   - Calculation of frontier-related and robot-related entropy
   - Combination of these terms to obtain the total entropy

8. **MEF-Based Goal Selection**
   - Selection of exploration goals using the entropy-field-based strategy
   - Integration of frontier information, robot positions, and communication constraints

9. **Autonomous Multi-Robot Exploration**
   - Autonomous movement of the robots toward selected exploration goals
   - Continuous sensing, communication, map updating, and goal selection during exploration

10. **Simulation and Evaluation**
    - Complete simulation of the multi-robot exploration system
    - Evaluation of exploration performance under communication constraints
    - Analysis of the obtained results with respect to the MEF-Explore methodology

## Current Stage

At the current stage, the initial components of the framework have been implemented and tested manually. The map, robot movement, communication conditions, dynamic communication graph, local maps, map merging, and frontier detection have been developed and verified individually.

For these initial stages, different robot positions, movements, communication conditions, and map-sharing situations have been considered manually to understand and verify the behaviour of each component.

The entropy-based MEF-Explore strategy and autonomous exploration are being implemented progressively after the individual components are verified.

## Project Structure

## Project Structure

## Project Structure

<pre>
pratyush_24255/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── M01_Map.py
│   ├── M02_Robot_Communication.py
│   ├── M03_Dynamic_Graph.py
│   ├── M04_Local_Maps.py
│   ├── M05_Map_Merging.py
│   ├── M06_Frontier_Detection.py
│   ├── M09_Simulation.py
│   ├── M10_Test_Map_Merging.py
│   └── M11_Test_Frontier_Detection.py
│
├── results/
│
└── report/
</pre>

## Requirements

- Python 3.x
- NumPy
- Matplotlib

Install the required packages using:

```bash
pip install -r requirements.txt