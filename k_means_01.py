import random
from math import sqrt

import matplotlib.pyplot as plt


def euclideandistance(individual, seed):
    dist = 0
    for idx, elem_seed in enumerate(seed):
        dist += (individual[idx] - elem_seed) ** 2
    dist = sqrt(dist)
    return dist


# buscar seed mais proxima

def get_seed(individual, seeds):
    lowest_dist = 1000
    currseed = 0
    for idx, seed in enumerate(seeds):
        distance = euclideandistance(individual[1:], seed)
        if distance < lowest_dist:
            lowest_dist = distance
            currseed = idx
    return currseed


def get_color(num):
    if num == 0:
        return 'yellow'
    elif num == 1:
        return 'blue'
    elif num == 2:
        return 'green'
    elif num == 3:
        return 'red'
    elif num == 4:
        return 'black'
    elif num == 5:
        return 'magenta'
    elif num == 6:
        return 'cyan'
    else:
        return 'gray'


clusternumber = 6

# veclis=[[0,1,1,0,0],[0,0,0,0,1],[0,1,0,0,0],[0,0,0,1,1],[0,0.25,0.65,0.55,0.95],[0,0.24,0.64,0.54,0.94],[0,0.05,0.05,0.55,0.95],[0,0.44,0.74,0.54,0.94],[0,1,0.95,0,0],[0,1,0,0,0],[0,1,0,0,0]]
# veclis=[[0,1,1],[0,0,0.5],[0,1,0],[0,0,1],[0,0.25,0.65],[0,0.24,0.64]]
veclis = list()
for k in range(0, 210):
    # veclis.append([0,random.random(),random.random(),random.random()])
    veclis.append([0, random.uniform(random.uniform(0,0.2), random.uniform(0.2,0.3)), random.uniform(random.uniform(0,0.2), random.uniform(0.2,0.3))])
    veclis.append([0, random.uniform(random.uniform(0.7,0.9), random.uniform(0.8,1)), random.uniform(0.8, 0.9)])
    veclis.append([0, random.uniform(0.3, 1), random.uniform(0.4, 0.7)])
for k in range(0, 100):
    # veclis.append([0,random.random(),random.random(),random.random()])
    veclis.append([0, random.uniform(0.1,0.2), random.uniform(0.7, 0.8)])

for i in veclis:
    plt.scatter(i[1], i[2], color=get_color(i[0]))
plt.show()

# colocar seeds ao calhas
veckmeans = list()  ### Le Random
for k in range(0, clusternumber):
    # veckmeans.append([random.random(),random.random(),random.random()])
    veckmeans.append([random.random(), random.random()])

for xx in range(0, 10):
    # ver qual a seed
    for i in veclis:
        i[0] = get_seed(i, veckmeans)

    # debug plot

    for i in veclis:
        plt.scatter(i[1], i[2], color=get_color(i[0]))

    for i, seed in enumerate(veckmeans):
        plt.scatter(seed[0], seed[1], color=get_color(i), marker='x')

    plt.savefig(str(xx) + 'A' + 'foo.png')

    # recentrar os centroides

    for i in range(0, len(veckmeans)):
        for ix, elem in enumerate(veckmeans[i]):
            veckmeans[i][ix] = 0
        cnt = 0
        for idx, elem in enumerate(veclis):
            if elem[0] == i:
                cnt = cnt + 1
                for ix, elem in enumerate(veckmeans[i]):
                    # print elem#for itm in range(0,len(elem)):
                    veckmeans[i][ix] = veckmeans[i][ix] + veclis[idx][ix + 1]

        for ix, elem in enumerate(veckmeans[i]):
            # print veckmeans[i][ix]
            if cnt > 0:
                veckmeans[i][ix] = veckmeans[i][ix] / cnt
            print veckmeans[i][ix]

    for i in veclis:
        plt.scatter(i[1], i[2], color=get_color(i[0]))
    for i, seed in enumerate(veckmeans):
        plt.scatter(seed[0], seed[1], color=get_color(i), marker='x')

    plt.savefig(str(xx) + 'B' + 'foo.png')

plt.savefig(str(xx) + 'FINAL' + 'foo.png')
print xx
plt.show()
