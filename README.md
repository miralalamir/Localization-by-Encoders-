# Robot Localization Using Odometry

## Problem

A mobile robot using only GPS may not have enough accuracy for precise movement between waypoints. GPS can have errors due to signal limitations, environment, or delays.

The robot needs another way to estimate its movement while it is moving, such as:

- Distance traveled
- Motor speed (RPM)
- Current X and Y position

---

## Solution

Improve the position accuracy by adding a **localization method** using wheel encoder data.

The robot uses information from ROS topics (such as distance, RPM, encoder values, etc.) and applies calculations to estimate its position using **odometry**.

The current code represents the algorithm only. The RPM and distance values are manually entered for testing, but the next step is converting it into a ROS format where the data will be received automatically.

---

## How does the localization work?

The localization system uses the robot's wheel movement information.

The ROS topics provide:

- Encoder pulses
- RPM
- Distance traveled

The algorithm converts this information into the robot's position:

- X coordinate
- Y coordinate

This allows the robot to estimate its position between GPS updates.

---

## What is Odometry?

Odometry is a method used to estimate a robot's position by comparing the current position with the starting position and tracking the movement between them.

It helps the robot move from one waypoint to another because it continuously updates where the robot is.

---

## Algorithm

### 1. Calculate RPM

$$
RPM=\frac{Pulse\ Count}{Encoder\ PPR}\times\frac{60}{Time}
$$

Where:

- Pulse Count = encoder pulses detected
- Encoder PPR = pulses per revolution
- Time = measurement period

---

### 2. Calculate Distance

The encoder rotations are converted into distance:

$$
Revolutions=\frac{Pulse\ Count}{Encoder\ PPR}
$$

$$
Distance=Revolutions \times Wheel\ Circumference
$$

For straight movement:

$$
d=\frac{D_1+D_2+D_3+D_4}{4}
$$

The average wheel distance is used as the robot movement distance.

---

### 3. Calculate X and Y Position

$$
X=X+d\cos(\theta)
$$

$$
Y=Y+d\sin(\theta)
$$

Where:

- X = robot position on X-axis
- Y = robot position on Y-axis
- d = distance traveled
- θ = robot direction

Example:

If the robot moves 20 cm at 30°:

$$
X=X+20\cos(30)
$$

$$
Y=Y+20\sin(30)
$$

The robot position updates continuously.

---

## Accuracy Improvement

GPS accuracy can be improved by combining multiple localization methods:

- GPS → provides global position
- Odometry → provides continuous movement tracking

Using both methods together reduces errors and gives a more accurate robot position estimate.

---

## Next Step

Convert the current algorithm into a ROS node:

- Subscribe to encoder topics
- Receive real-time motor data
- Calculate odometry
- Publish robot position
