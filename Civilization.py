import uuid
import numpy as np

ALP=np.array([1,0,0,0])
BET=np.array([0,1,0,0])
GAM=np.array([0,0,1,0])
THE=np.array([0,0,0,1])



class Human:
    race=None
    nation=None
    lifelimit=8
    def __init__(self,*race):
        self.age=0
        self.name=uuid.uuid1()
        self.conservative=1
        if len(race)!=0: #first generation
            self.race=race[0]
        else:
            pass
        self.marryed=False
        self.combination=None
            # self.born
    def grown(self):
        self.age+=1
    def isMarryed(self):
        return self.marryed
    def isDeath(self):
        if self.age>8:
            return True
        else:
            return False
        
    def born(self,father,mother):
        self.race=father.race/2+mother.race/2

class Nation:
    def __init__(self):
        self.members=[]     #all human (class Human)
        self.population=0   #polupation
        self.consevative=0  #Possiblity of marry with other race
        self.marryage=2     #legal marry age
        self.lifelimit=8    #death age
    def addMember(self,element):
        self.members.append(element)
        self.population+=1
    def initMembers(self,number,race):
        self.population+=number
        for i in range(number):
            n=Human(race,initial='f')
            self.addMember(n)
    def marry(self):
        for i in self.members:
            if i.isMarryed():
                continue
            elif i.age>self.marryage:
                for j in self.members:
                    if j.isMarryed():
                        continue
                    elif j.age>self.marryage:
                        if np.random.rand()>0.5:
                            i.marryed=True
                            j.marryed=True
                            i.combination=j.name
                            j.combination=i.name
    
    def update(self):
        for i in self.members:
            i.grown()
            if i.isDeath():
                self.members.remove(i)
                self.population-=1




class World:
    def __init__(self,num):
        self.nations=[]
        for i in range(num):
            self.nations.append(Nation)
        
    



