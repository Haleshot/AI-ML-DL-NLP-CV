# Vacuum Cleaner World and PEAS Description

## Table of Contents
- [Aim](#aim)
- [Vacuum Cleaner World](#vacuum-cleaner-world)
  - [Identifying Precepts and Actions](#identifying-precepts-and-actions)
  - [Rationality of the Agent](#rationality-of-the-agent)
- [PEAS Description](#peas-description)
  - [Part Picking Robot](#part-picking-robot)
  - [Satellite Image Analysis](#satellite-image-analysis)
- [Output](#output)

## Aim
The aim of this project is to develop a simple vacuum cleaner world with only two locations and to tabulate PEAS descriptions for two different agents: the Part Picking Robot and the Satellite Image Analysis agent.

## Vacuum Cleaner World
The vacuum cleaner world is a simple scenario where a vacuum agent operates in an environment with two locations, labeled A and B. The agent's goal is to clean up dirt in the locations.

### Identifying Precepts and Actions
The agent perceives its environment through sensors, and its actions are performed through actuators. In the vacuum cleaner world, the agent's percepts include information about its current location and whether there is dirt in the location. The agent's actions include moving left, moving right, sucking up dirt, or doing nothing.

### Rationality of the Agent
In the vacuum cleaner world, a simple agent function can be defined as follows: if the current location is dirty, then the agent should suck up the dirt; otherwise, it should move to the other location. This agent function is rational as it selects actions based on the current percept to achieve the goal of cleaning up the dirt.

## PEAS Description
PEAS stands for Performance measure, Environment, Actuators, and Sensors. It provides a framework to describe the key aspects of an intelligent agent.

### Part Picking Robot
- Performance measure: The performance measure for the Part Picking Robot can be the number of correctly picked parts within a given time frame.
- Environment: The environment for the robot is a warehouse or manufacturing facility with shelves containing parts.
- Actuators: The robot uses its mechanical arms to pick up parts and place them in designated locations.
- Sensors: The robot's sensors detect the location of the parts, the state of the shelves, and any obstacles.

### Satellite Image Analysis
- Performance measure: The performance measure for the Satellite Image Analysis agent can be the accuracy of its analysis in identifying specific features or objects.
- Environment: The environment for the agent is satellite imagery captured from space.
- Actuators: The agent performs image processing and analysis algorithms to extract relevant information from the images.
- Sensors: The agent's sensors receive satellite images as input for analysis.

## Output
Here is a screenshot of the output obtained from running the program:

![Output](https://user-images.githubusercontent.com/57552973/184404969-1e52aed3-0724-44bf-862d-e67a3f1de124.png)