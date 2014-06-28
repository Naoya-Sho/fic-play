############
##Plot the list of x0 and x1

import matplotlib.pyplot as plt
import random as random
import numpy as np
fig, ax = plt.subplots()

gamename = 'Matpenny'
players = [0,1]

# setting up the payoff matrix
pay = ((1,-1),(-1,1),
       (-1,1),(1,-1)) 

def sep(a, pay):
    return ((pay[0][a], pay[1][a]),
            (pay[2][a], pay[3][a]))

xmat = np.empty((len(players), len(players)))

# Best response function
def br(p,x):
    xmat[p] = (1-x, x)

    expay = np.dot(np.array(sep(p, pay)), xmat[p])

    if expay[0] == expay[1]:
        return random.randint(0,1)

    else:
        return expay.argmax()

## plot x0 and x1 and save the figure

def playgame(trials):

    x0 = random.uniform(0,1)
    x1 = random.uniform(0,1)

    for i in range(1000):
        a0 = br(0, x0)
        a1 = br(1, x1)
        x0.append(x[i]+(a[1]-x[i])/(i+2))
        x1.append(x[i]+(a[0]-x[i])/(i+2))

    xaxis = range(trials)
    ax.plot(xaxis, x0, 'b-',label = 'Player0 x')
    ax.plot(xaxis, x1, 'r-',label = 'Player1 x')
    ax.legend()
    plt.title('ts = '+ str(trials - 1), color='k')
    plt.savefig(gamename + str(trials-1) + '.pdf',transparent=True, bbox_inches='tight', pad_inches=0)
    plt.close()


###################
## plot the histogram and save the figure
# make a list of x0(T-1)

iter = 200
terminalx0 = []

for j in range(iter + 1):
    
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

    terminalx0.append(x0_values[trials - 1])

# plot the list in histogram

plt.xlim(0,1)
n, bins, patches = plt.hist(terminalx0, 4)

plt.title('ts = '+ str(trials - 1)+ ','+' N = '+ str(iter), color='k')

plt.setp(patches, 'facecolor', 'g')
plt.savefig(gamename + '_hist' + str(trials-1) +'_'+ str(iter) +'.pdf',transparent=True, bbox_inches='tight', pad_inches=0)
plt.show()

