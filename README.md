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

## Code overview

The code is built to get data manually as a start.

### 1. RPM function (Revolution Per Minute)
- This function focuses on getting the information (manually for now) and calculate it to get the speed for motors. (Lines from 3-5)
- We used this function in a for loop and to get information also, to calculate every and each motor alone. (Lines from 16-21)
- When we get the speeds and distances for each motor, we could know whether the robot is going in which direction. (forward, backward, left or right) (Lines from 36-41)

### 2. Localization
- Localization needs distance that the robot moved to get **X** and **Y** and by adding the previous distance to know what was the starting point for the robot. (Lines 24 and 25)
- Improted math to do sin() and con().

### 3. Distance 
- distance, is the original distance that we have, and why multiblied by 22, because the circumference of the wheel that we have is ≈ 22cm (it is actually 21.99 cm), so we times how many rovulotion per minute by the circumference of teh wheel to get the final distance. (Line 20)
- d, it is the distance that we use for the equation (all distances from the motors divided by 4) (Line 23)

### 4. Coditions 
**NOTE: [0] IS FRONT RIGHT
        [1] IS FRONT LEFT
        [2] IS BACK RIGHT
        [3] IS BACK LEFT
        
#### a. When both are moving is the same direction
- That means it is backward or forward according to the sign of their RPM.

#### b. When one is stopped (FR or FL) and others are working
- That means that the robot is rotating arount the left wheel, so our *Pivot* is the left wheel.(*Pivot* is a new word which means the main point that we are totating around)
- To get the Pivot we will use
$$\text{Rotation Angle} = \frac{\text{Distance of Outer Wheel } (A) \times 360}{2\pi \times \text{Distance to Pivot } (l)}$$
- This is simbly take the revolution (speed) of the motor, multiplied by 360 to get the precentage, divided by 2π to know the circumference and finally, * 29.5 the radius (the length between the two wheels).

#### c. When each side motors are moving it differnt dirctions
- That means that the robot is moving around itself, which means that the *Pivot* is half the L (the length between the 2 wheels).
- The formula for it is
$$\text{Rotation Angle} = \frac{l}{2}$$

#### d. When each side motors are moving but in different speeds
- That means that the *Pivot* is beside the robot, which means we have to get the velovity for each side first.
$$\text{velocity} = \frac{d_1 + d_2}{2 \times \text{time}}$$
- After we get the velocity we need to know how far the *Pivot* from the robot,
$$\text{Rotation Angle} = -\frac{L}{2} \times \frac{v_r + v_l}{v_r - v_l}$$
the negative make the right side is negative and the left side is positive in outputs, L/2 is to know where is the center of the robot so we can know the starting point of this output (for example if the output is 5cm, so the *Pivot* is away from the center of the rbot by 5cm to the left)and finally Vr + Vl is to get the total Velocity and then divide it to the differnece btween them.

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
- Publish robot position
