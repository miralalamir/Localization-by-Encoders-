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


for i in range(4):
    print(f"RPM {i+1}: {rpm[i]}")
    print(f"Distance {i+1}: {distance[i]}")

print(d)


# 0 = r
# 1 = l
# 2 = r
# 3 = l

if rpm[0] == rpm[1]:
    print("straight")
elif rpm[0] == 0 and rpm[1] > 0:
    print("right")
    rotation = (rpm[1]*360) / 2*(math.pi*29.5)
elif rpm[0] == 0 and rpm[1] < 0:
    print("left")
    rotation = (rpm[0]*360) / 2*(math.pi*29.5)
elif rpm[0] > 0 and rpm[1] < 0:
    print("left")
    roation = 29.5/2 #29.5 is the length between the wheels
    # rotation = (rpm[1] * 29.5) / (rpm[0] - rpm[1])
elif rpm[0] > 0 and rpm[1] > 0:
    print("left")
    roation = 29.5/2
    # rotation = (rpm[0] * 29.5) / (rpm[1] - rpm[0])
elif rpm[0] > rpm [1] or rpm[0] < rpm[1]:
    #turn right
    vr = (distance[0] + distance[2]) / (2 *time)
    vl = (distance[1] + distance[3]) / (2 *time)
    rotation = -(29.5/2) * ((vr + vl) / (vr - vl)) # it will be the same to get the right as positive and left as negative
    


print(rotation)
x = x + d * (math.cos(rotation))
y = y + d * (math.sin(rotation))

print(x,y)