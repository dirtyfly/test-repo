import matplotlib.pyplot as plt
import random

# from mpl_toolkits.mplot3d import Axes3D


cluster_num = 2
learnrate = 0.2
radius = 0  # nao implementado, nao ha vizinhos - NAO VEM QUE NAO TEM !

#veclis = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1], [0.25, 0.65, 0.55, 0.95], [0.24, 0.64, 0.54, 0.94],
#          [0.05, 0.05, 0.55, 0.95], [0.44, 0.74, 0.54, 0.94], [1, 0.95, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]

#for k in range(0, 250):
#    veclis.append([random.random(), random.random(), random.random(), random.random()])
veclis=list()
for k in range(0, 210):
    # veclis.append([0,random.random(),random.random(),random.random()])
    veclis.append([ random.uniform(random.uniform(0,0.2), random.uniform(0.2,0.3)), random.uniform(random.uniform(0,0.2), random.uniform(0.2,0.3))])
    veclis.append([ random.uniform(random.uniform(0.7,0.9), random.uniform(0.8,1)), random.uniform(0.8, 0.9)])
    veclis.append([ random.uniform(0.3, 1), random.uniform(0.4, 0.7)])
    veclis.append([ random.uniform(random.uniform(0.5,0.6), random.uniform(0.5,0.6)), random.uniform(random.uniform(0.5,0.7), random.uniform(0.4,0.7))])
for k in range(0, 100):
    # veclis.append([0,random.random(),random.random(),random.random()])
    veclis.append([ random.uniform(0.1,0.2), random.uniform(0.7, 0.8)])
# veclis=[[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[0.1,0.1,0.1,0.1],[0.1,0.1,0.1,0.1]]
# 'randomly' generated list
# vecsom=[[0.2,0.6,0.5,0.9],[0.8,0.4,0.7,0.3],[0.5,0.7,0.5,0.6],[0.5,0.7,0.5,0.6]]
# vecsom=[[0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5]]

vecsom = list()  ### Le Random
#for k in range(0, 7):
#    vecsom.append([random.random(), random.random(), random.random(), random.random()])
for k in range(0, 4):
    vecsom.append([random.random(), random.random()])
for vecs in vecsom:
    plt.scatter(vecs[0], vecs[1], color='red')
currlearnrate = learnrate

for vec in veclis:
    print vec[0]
    print vec[1]
    plt.scatter(vec[0], vec[1], color='blue')

for iteracao in range(0, 100):  # num de runs
    for vec in veclis:
        # print vecsom
        # print vec	#debug
        closest_vecsom = 0
        mindist = 1000
        for idxvs, vs in enumerate(vecsom):
            somadist = 0
            # print idxvs
            # print range(0,len(vs))		#debug
            for i in range(0, len(vs)):
                somadist = somadist + (vs[i] - vec[i]) ** 2
            # print somadist
            if somadist < mindist:
                closest_vecsom = idxvs
                mindist = somadist
        # update closest
        for i in range(0, len(vecsom[closest_vecsom])):
            oldval = vecsom[closest_vecsom][i]
            # print vecsom[closest_vecsom][i]
            vecsom[closest_vecsom][i] = (oldval + learnrate * (vec[i] - oldval))
        print str(closest_vecsom) + ":" + str(vecsom)
    # 'plt.scatter(vecsom[0],vecsom[1],color='red')
    for vecs in vecsom:
        plt.scatter(vecs[0], vecs[1], color='red')
    learnrate = learnrate - learnrate / 4
print "-------------------"
print veclis
print vecsom
for vecs in vecsom:
    plt.scatter(vecs[0], vecs[1], color='black', marker='^')

plt.show()
