'''This is an implementation of an algorithm that verifies that all 2-caps in f_3^4 on a given list of 2-caps are affinely
equivalent. The 2-caps on the list were found using an algorithm written by Jaron Wang, who was a previous
undergraduate researcher on this project. All possible 2-caps are known to be affinely equivalent to at least
one 2-cap on this list, so if all 2-caps on the list are affinely equivalent to all other 2-caps on the list then all 2-
caps are affinely equivalent in F_3^4. This algorithm takes an arbitrary 2-cap from the list, applies an affine
transformation to it, and then checks if the given 2-cap is on the list. If it is, delete it from the list, and then
apply a new affine transformation to the initial arbitrary 2-cap and repeat the process until all 2-caps are deleted
from the list or until all valid affine transformations have been exhausted. If it were the case that all 2-caps were
not affinely equivalent, this code would never stop running because there are too many valid affine transformations.'''

import numpy as np
import pickle
import os
import time
import sys
import re


cap_path = os.path.join(os.path.join(os.getcwd(), '4Dcaps.txt'))
file1 = open(cap_path, 'r')
capStrings = file1.read()
caps = re.findall('\(0 0 0 0\)\(0 0 0 1\)\(0 0 1 0\)\(0 1 0 0\)\(1 0 0 0\)\(. . . .\)\(. . . .\)\(. . . .\)\(. . . .\)',
                 capStrings)
caps += re.findall('\(0 0 0 0\)\(0 0 0 1\)\(0 0 1 0\)\(0 1 0 0\)\(. . . .\)\(1 0 0 0\)\(. . . .\)\(. . . .\)\(. . . .\)',
                 capStrings)
for i in range(len(caps)):
    caps[i] = caps[i].replace(' ','')
    caps[i] = caps[i].replace('(','')
    caps[i] = caps[i].replace(')','')
    capIter = iter(caps[i])
    cap = np.empty(9, object)
    for j in range(9):
        vect = np.empty(4, int)
        for k in range(4):
            vect[k] = next(capIter)
        cap[j] = vect
    caps[i] = cap
cap = caps[0]  # this is the cap that we will map to every other cap
caps = caps[1:] # this is the list that caps will be deleted from

mats = np.load('matrices.npy')
# loading this file takes a while, so running in Jupyter Notebook allows us to
# only load this once instead of every time we want to debug


# apply affine transformations of the form T(x) = Ax + v where v = 0.
# apply Ax to every x vector in cap, test if new cap is on list
# and delete it from caps if so. if not move on to next A.
verified = 0  # number of verified caps out of 12
for A in mats:
    newCap = set()  # this is the transformed cap, which is constructed below by multiplying every vector by A
    newCap.add(tuple(np.mod(np.matmul(A, np.transpose(cap[0])), 3)))
    for i in range(1, len(cap)):
        newCap.add(tuple(np.mod(np.matmul(A, np.transpose(cap[i])), 3)))
    for currCap in caps:  # check if new cap is equal to any of the remaining caps
        count = 0
        for vect in currCap:
            if tuple(vect) not in newCap:  # check if every vector is in the new cap
                break
            count += 1
            if count == 9:
                verified = verified + 1
                print(str(verified) + " caps verified")
                caps.remove(currCap)
                print(str(len(caps)) + ' caps remaining')
                print("initial cap:\n" + str(cap)+'\n')
                print("cap is being multiplied by \n" + str(A)+'\n')
                print("cap becomes: \n" + str(newCap)+'\n')
                print(
                    "which is equal to the following cap that's still on the list\n" + str(currCap))
                print("cap has been removed from list\n\n\n")
                if verified == 12:
                    sys.exit('Solution Found')
