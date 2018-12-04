# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.prob = prob
        self.parents = parents
    
    def computeProb(self, evid):
        if (len(self.parents) == 2):
            prob1 = self.prob[evid[self.parents[0]]][evid[self.parents[1]]]
        elif (len(self.parents) == 1):
            prob1 = self.prob[evid[self.parents[0]]]
        else:
            prob1 = self.prob[0]
        return [1-prob1, prob1]

            
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):
        opts = [0]*getOpt(evid)
        pn = 0
        pnn = 0
        for i in range(2**getOpt(evid)):
            print(opts)
            print(evid)
            newEvid = combineEvids(evid, opts)

            pn += self.computeJointProb(forceEvidTF(newEvid, 1))
            pnn += self.computeJointProb(forceEvidTF(newEvid, 0))
            if i < 2**getOpt(evid) - 1:
                opts = addLst(opts)


        return pn / (pn + pnn)
        
        
    def computeJointProb(self, evid):
        prob1 = 1
        for num in range(len(self.prob)):
            prob1 *= self.prob[num].computeProb(evid)[evid[num]]
        return prob1


def getOpt(evid):
    cont = 0
    for i in evid:
        if i == []:
            cont+=1
    return cont

def forceEvidTF(evid, num):
    evid2 = []
    for i in evid:
        if i == -1:
            evid2.append(num)
        else:
            evid2.append(i)
    return evid2

def combineEvids(evid, option):
    e = 0
    evid2 = []
    for i in range(len(evid)):
        if evid[i] == []:
            evid2.append(option[e])
            e +=1
        else:
            evid2.append(evid[i])
    return evid2


def addLst(l1):
    r = len(l1)
    st1 = '0b'
    out = [0]*r
    for i in l1:
        st1 += str(i)
    num1 = int(st1,2)
    num1+=1
    st2 = bin(num1)
    for i in range(-len(st2[2:]), 0, 1):
        out[i] = int(st2[i])
    return out