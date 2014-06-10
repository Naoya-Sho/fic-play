import matplotlib.pyplot as plt
import random as random
from __future__ import division

fig, ax = plt.subplots()

players = [0,1]

trials = 201
current_x0 = 0.5
current_x1 = 0.5

# setting up the payoff function

def pay0(a,b):
    if a == b:
        return 1
    else:
        return -1

def pay1(a,b):
    if a != b:
        return 1
    else:
        return -1

# best response function using the payoff function 
def br0(x):
    if x * pay0(0,0) + (1-x) * pay0(0,1) > x * pay0(1,0) + (1-x) * pay0(1,1):
        return 0

    elif x * pay0(0,0) + (1-x) * pay0(0,1) < x * pay0(1,0) + (1-x) * pay0(1,1):
        return 1

    else:
        return random.randint(0,1)

def br1(x):
    if x * pay1(0,0) + (1-x) * pay1(1,0) > x * pay1(0,1) + (1-x) * pay1(1,1):
        return 0

    elif x * pay1(0,0) + (1-x) * pay1(1,0) < x * pay1(0,1) + (1-x) * pay1(1,1):
        return 1

    else:
        return random.randint(0,1)

# can be combined by using class?OOP later on


x0_values = []
x1_values = []
xaxis = range(trials)

for i in range(trials):
    a0 = br0(current_x0)
    a1 = br1(current_x1)

    x0_values.append(current_x0)
    current_x0 = current_x0 + (a1-current_x0)/(i + 2)

    x1_values.append(current_x1)
    current_x1 = current_x1 + (a0-current_x1)/(i + 2)

ax.plot(xaxis, x0_values, 'b-')
ax.plot(xaxis, x1_values, 'r-')
plt.show()


