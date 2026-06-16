import math

def calculate_rpm(Pulse_c,encoder_p,time):
    rpm = (Pulse_c / encoder_p) * (60 / time)
    return rpm
x = 0
y = 0
pulse = []
encoder = []
rpm = []
distance = []
d =0

time = float(input(f"Time (seconds): "))

for i in range(4):
    pulse.append(int(input(f"Pulse Count{i+1}: ")))
    encoder.append(int(input(f"Encoder Pulses per Revolution{i+1}: ")))
    rpm.append(calculate_rpm(pulse[i], encoder[i], time))
    distance.append(22*rpm[i])
    d += distance[i]

d = d / 4
x = x + d * (math.cos(30))
y = y + d * (math.sin(30))


for i in range(4):
    print(f"RPM {i+1}: {rpm[i]}")
    print(f"Distance {i+1}: {distance[i]}")

print(d)
distance[0] = 22*rpm[0]


if rpm[0] == rpm[1]:
    print("straight")
elif rpm[0] <= 0 and rpm[1] > 0:
    print("right")
elif rpm[0] > 0 and rpm[1] <= 0:
    print("left")

