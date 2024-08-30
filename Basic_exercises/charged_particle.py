import math
import vector

from particle import particle

class charged_particle(particle):
    def __init__(self,px,py,pz,m=-1,e=-1,charge=None):
        if charge is None:
            print("warning! Charge not specified! Given default charge=0")
            self.charge=0
        else:
            self.charge=charge
        if(m!=-1):
            self._m = m
            self._e = math.sqrt(m**2+(px**2+py**2+pz**2))
        if(e!=-1):
            self._e = e
            if(e**2-(px**2+py**2+pz**2)<0):
                print("warning! E>p+m, unphysical particle! ")
            self._m = math.sqrt(e**2-(px**2+py**2+pz**2))
        super().__init__(px,py,pz,m)#Method to extend the behavior of the parent class’s constructor
            #self.p4=(self.px,self.py,self.pz,self.e)
        self.p4=vector.obj(px=px,py=py,pz=pz,E=e)

    def charged_particle_p4(self,lorentz_p4,charge):
        return charged_particle(px=lorentz_p4.px,py=lorentz_p4.py,pz=lorentz_p4.pz, e=lorentz_p4.E,charge=charge)


    def __add__(self,other):
        sum_p4=self.p4+other.p4
        sum_charge=self.charge+other.charge
        return self.charged_particle_p4(lorentz_p4=sum_p4,charge=sum_charge)
    def __str__(self):
        return ("px = "+str(self.p4.px)+" py = "+str(self.p4.py)+" pz = "+str(self.p4.pz)+" E = "+str(self.p4.E)+" charge = "+str(self.charge))
def charged_particle_p4(lorentz_p4,charge):
    return charged_particle(px=lorentz_p4.px,py=lorentz_p4.py,pz=lorentz_p4.pz, e=lorentz_p4.E,charge=charge)
