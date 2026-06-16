# Localization-by-Encoders-
Problem

A mobile robot using only GPS may not have enough accuracy for precise movement between waypoints. GPS can have errors due to signal limitations, environment, or delays.

The robot needs another way to estimate its movement while it is moving, such as:

Distance traveled
Motor speed (RPM)
Current X and Y position
Solution

Improve the position accuracy by adding a localization method using wheel encoder data.

The robot uses information from ROS topics (such as distance, RPM, encoder values, etc.) and applies calculations to estimate its position using odometry.

The current code represents the algorithm only. The RPM and distance values are manually entered for testing, but the next step is converting it into a ROS format where the data will be received automatically.

How does the localization work?

The localization system uses the robot's wheel movement information.

The ROS topics provide:

Encoder pulses
RPM
Distance traveled

The algorithm converts this information into the robot's position:

X coordinate
Y coordinate

This allows the robot to estimate its position between GPS updates.

What is odometry?

Odometry is a method used to estimate a robot's position by comparing the current position with the starting position and tracking the movement between them.

It helps the robot move from one waypoint to another because it continuously updates where the robot is.

How does the algorithm work?
1. Calculate RPM
RPM=
Encoder PPR
Pulse Count
	​

×
Time
60
	​


Where:

Pulse Count = encoder pulses detected
Encoder PPR = pulses per revolution
Time = measurement period
2. Calculate distance

The encoder rotations are converted into distance:

Revolutions=
Encoder PPR
Pulse Count
	​

Distance=Revolutions×Wheel Circumference

For a robot moving straight:

d=
4
D
1
	​

+D
2
	​

+D
3
	​

+D
4
	​

	​


The average distance of the wheels is used as the robot's movement distance.

3. Calculate X and Y position

The robot position is updated using:

X=X+dcos(θ)
Y=Y+dsin(θ)

Where:

X = robot position on X-axis
Y = robot position on Y-axis
d = distance traveled
θ = robot direction

Example:

If the robot moves 20 cm at 30°:

X=X+20cos(30)
Y=Y+20sin(30)

The robot position is updated continuously.

Accuracy Improvement

GPS accuracy can be improved by combining multiple localization methods:

GPS → provides global position
Odometry → provides continuous movement tracking

Using both methods together helps reduce errors and gives a more accurate estimate of the robot's position.
