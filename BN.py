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
        pass
        return 0
        
        
    def computeJointProb(self, evid):
        prob1 = 1
        for num in range(len(self.prob)):
            prob1 *= self.prob[num].computeProb(evid)[evid[num]]
        return prob1


def addLst(l1):
    st1 = '0b'
    out = ''
    for i in l1:
        st1 += str(i)
    num1 = int(st1,2)
    num1+=1
    st2 = bin(num1)
    for i in st2[2:]:
        out += i
    return list(out)
