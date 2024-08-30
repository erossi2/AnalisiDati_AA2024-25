#In case it doesn't work you have to install vector: pip install vector
print("Hello World!")

print("That was easy, right? Now let's load some libraries! ")

import vector

p1 = vector.obj(px=1,py=0,pz=0,E=1)
p2 = vector.obj(px=1.5,py=0,pz=0,E=200)

print ("the sum of the momenta is ", p1+p2)
