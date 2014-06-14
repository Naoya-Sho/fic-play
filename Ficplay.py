############
##Plot the list of x0 and x1

import matplotlib.pyplot as plt
import random as random
from __future__ import division

fig, ax = plt.subplots()

players = [0,1] # not used yet
gamename = 'Matpenny'


trials = 201
current_x0 = random.uniform(0,1)
current_x1 = random.uniform(0,1)

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

## plot x0 and x1 and save the figure
x0_values = []
x1_values = []

for i in range(trials):
    a0 = br0(current_x0)
    a1 = br1(current_x1)

    x0_values.append(current_x0)
    current_x0 = current_x0 + (a1-current_x0)/(i + 2)

    x1_values.append(current_x1)
    current_x1 = current_x1 + (a0-current_x1)/(i + 2)


xaxis = range(trials)
ax.plot(xaxis, x0_values, 'b-',label = 'Player0 x')
ax.plot(xaxis, x1_values, 'r-',label = 'Player1 x')
ax.legend()
plt.title('ts = '+ str(trials - 1), color='k')
plt.savefig(gamename + str(trials-1) + '.png',transparent=True, bbox_inches='tight', pad_inches=0)
plt.close()

###################
## plot the histogram and save the figure
# make a list of x0(T-1)

iter = 200
terminalx0 = []

for j in range(iter + 1):
    
    terminalx0.append(x0_values[trials - 1])

    current_x0 = random.uniform(0,1)
    current_x1 = random.uniform(0,1)
    x0_values = []
    x1_values = []

    for i in range(trials):
        a0 = br0(current_x0)
        a1 = br1(current_x1)

        x0_values.append(current_x0)
        current_x0 = current_x0 + (a1-current_x0)/(i + 2)

        x1_values.append(current_x1)
        current_x1 = current_x1 + (a0-current_x1)/(i + 2)

# plot the list in histogram
n, bins, patches = plt.hist(terminalx0, 15, normed = 1)

plt.title('ts = '+ str(trials - 1)+ ','+' N = '+ str(iter), color='k')

plt.setp(patches, 'facecolor', 'g')
plt.savefig(gamename + '_hist' + str(trials-1) +'_'+ str(iter) +'.png',transparent=True, bbox_inches='tight', pad_inches=0)
plt.show()

