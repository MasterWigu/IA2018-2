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
        def computeProbAux(parTemp, evid, probs):
            if parTemp == []:
                return probs
            else:
                return computeProbAux(parTemp[1:] ,evid, probs[evid[parTemp[0]]] )
        probT = computeProbAux(self.parents, evid, self.prob)
        return (1-probT, probT)

            
class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def computePostProb(self, evid):
        opts = [0]*evid.count([])
        pn = 0
        pnn = 0
        for i in range(2**evid.count([])):
            optsTemp = opts.copy()
            newEvid = [evid[i] if evid[i] != [] else optsTemp.pop() for i in range(len(evid))]
            pn += self.computeJointProb([i if i != -1 else 1 for i in newEvid])
            pnn += self.computeJointProb([i if i != -1 else 0 for i in newEvid])
            if i < 2**evid.count([]) - 1:
                opts = addLst(opts)
        return pn / (pn + pnn)
        
        
    def computeJointProb(self, evid):
        prob1 = 1
        for num in range(len(self.prob)):
            prob1 *= self.prob[num].computeProb(evid)[evid[num]]
        return prob1

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