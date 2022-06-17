# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position
# after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math
vd = 0
hd = 0
while True:
    s = input()
    if not s:
        break
    dir, dis = s.strip().split(" ")
    if dir == "UP":
        vd += int(dis)
    if dir == "DOWN":
        vd -= int(dis)
    if dir == "LEFT":
        hd -= int(dis)
    if dir == "RIGHT":
        hd += int(dis)

res = int(round(math.sqrt(vd**2 + hd**2)))
print(res)
