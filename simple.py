from numpy.random import seed
from numpy.random import rand
import random
import math
import numpy
import numpy as np
import matplotlib.pyplot as plt

class simple_cell():
    num  = 0
    def __init__(self, dnk = None,t = None):
        self.t = t
        simple_cell.num += 1
        if dnk is None:
            return
        self.dnk = dnk
        self.death_rate = dnk[0]
        self.rep_rate = dnk[1]
        self.mutation_chance = dnk[2]
    def update(self,a):
        rand  = random.random()
        death = (self.death_rate  + 0.0005*a)
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
            r = random.randrange(0,2)
            i  = 0
            if r == 0:
                dnk2 = [0.1,0.3,0]
                return simple_cell(dnk2,1)
            if r == 1:
                dnk2 = [0.05,0.3,0]
                return simple_cell(dnk2,2)
        
        return simple_cell(dnk2,0)
        pass




def main(n):
    mutation = []
    reproduction = []
    death = []
    number_of_creature = n
    cells = []
    number = []
    seed(1)
    death_c = 0.1
    rep_c = 0.2
    mut_c = 0
    for i in range(n):
        cells.append(simple_cell([death_c,rep_c,mut_c],0))
    cycle = 0
    while cycle != 200 :
        #print(cycle)
        #print(len(cells))
        dell = []
        mutation.append([0,0,0,0,0,0,0,0,0,0])
        reproduction.append([0,0,0,0,0,0,0,0,0,0])
        death.append([0,0,0,0,0,0,0,0,0,0])
        
        # print(type(cells))
        for k in cells:
            # print(type(k))
            death[cycle][int(k.death_rate*10)] += 1
            reproduction[cycle][int(k.death_rate*10)] += 1
            mutation[cycle][int(k.death_rate*10)] += 1
        # print("cek sta ")

        for i in range(len(cells)):
            t = cells[i].update(len(cells))
            if t == -1:
                dell.append(cells[i])
            if t == 0:
                continue
            if type(simple_cell()) == type(t):
                cells.append(t)
            # print(type(k))
        #print(len(dell))

        for z in dell:
            del cells[cells.index(z)]
            a = simple_cell.num
            simple_cell.num -= 1
            print(simple_cell.num-a)
        
        number.append([0,0,0])
        for i in cells:
            print(i.t)
            number[-1][i.t] += 1
            pass
        
        #number.append(len(cells))
        #number.append(len(cells))
        
        cycle += 1
    #numpy.savetxt("death.txt",death)
    #numpy.savetxt("reproduction.txt",reproduction)
    ##numpy.savetxt("mutation.txt",mutation)
    #numpy.savetxt("number.txt",number)
    return number
brojevi = []
for i in range(20):
    brojevi.append(main(10))
print(len(brojevi),len(brojevi[0]))
for i in brojevi:
    plt.plot(i,alpha=0.5)
#plt.plot(1.15**numpy.linspace(1,50,50))
plt.show()
