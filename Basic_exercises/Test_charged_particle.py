import math
import vector

p1 = vector.obj(px=1000,py=0,pz=0,E=1000)
p2 = vector.obj(px=2000,py=0,pz=0,E=2020)

print (p1+p2)

from charged_particle import *

charged_1 = charged_particle_p4(p1,1)
print (charged_1.p4,charged_1.charge)

charged_2 = charged_particle_p4(p2,-1)
print(charged_2.p4, charged_2.charge)

new_particle=charged_1+charged_2
print("sum of the two is ", new_particle)
