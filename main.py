from numpy.random import seed
from numpy.random import rand
import random
import math
import numpy
import numpy as np
import matplotlib.pyplot as plt

class simple_cell():
    num  = 0
    def __init__(self, dnk = None):
        simple_cell.num += 1
        if dnk is None:
            return
        self.dnk = dnk
        self.death_rate = dnk[0]
        self.rep_rate = dnk[1]
        self.mutation_chance = dnk[2]
        if len(dnk) != 3:
            self.death_rate *= dnk[3]
            self.rep_rate *= dnk[3]
    def update(self):
        rand  = random.random()
        death = (self.death_rate + 0.0001*simple_cell.num )
        if death > rand:
            return -1
        rand -= self.death_rate
        if self.rep_rate > rand:
            return self.reproduce()
        return 0
    def reproduce(self):
        rand = random.random()
        dnk2 = self.dnk
        if self.mutation_chance > rand:
            r = random.randrange(0,10)
            i  = 0
            if r < 5:
                i  = 1
            elif r < 7:
                i = 2
            elif r < 8:
                i = 3
            else:
                i = 3
            for j in range(i):
                r  = random.randrange(3)
                dnk2[r] = abs(dnk2[r]+random.gauss(0,0.1))
                if dnk2[r] > 1:
                    dnk2[r] = math.atan(r)/3.141/2
        return simple_cell(dnk2)
        pass




def main(n):
    mutation = []
    reproduction = []
    death = []
    number_of_creature = n
    cells = []
    number = []
    seed(1)
    for i in range(n):
        cells.append(simple_cell([0.1,0.1,0.01]))
    cycle = 0
    while cycle != 50 and len(cells) != 0:
        print(cycle)
        print(len(cells))
        dell = []
        mutation.append([0,0,0,0,0,0,0,0,0,0])
        reproduction.append([0,0,0,0,0,0,0,0,0,0])
        death.append([0,0,0,0,0,0,0,0,0,0])
        number.append(len(cells))
        # print(type(cells))
        for k in cells:
            # print(type(k))
            death[cycle][int(k.death_rate*10)] += 1
            reproduction[cycle][int(k.death_rate*10)] += 1
            mutation[cycle][int(k.death_rate*10)] += 1
        # print("cek sta ")
        for i in range(len(cells)):
            t = cells[i].update()
            if t == 1:
                dell.append(i)
            if t == 0:
                continue
            if type(simple_cell()) == type(t):
                cells.append(t)
            # print(type(k))
        for z in dell:
            del cells[z]

        cycle += 1
    numpy.savetxt("death.txt",death)
    numpy.savetxt("reproduction.txt",reproduction)
    numpy.savetxt("mutation.txt",mutation)
    numpy.savetxt("number.txt",number)
    fig = plt.figure(figsize=(8, 3))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')
    _x = np.arange(10)
    _y = np.arange(len(death))
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = death
    bottom = np.zeros_like(top)
    width = depth = 1

    ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
    ax1.set_title('Shaded')
    top  = reproduction
    ax2.bar3d(x, y, bottom, width, depth, top, shade=True)
    ax2.set_title('Shaded')
    plt.show()
main(10)
