#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from copy import copy
import re

#getting files
file = '../input_files/ListNuclei.csv'
el_z = '../input_files/El_Z.csv' #atomic numbers [0] and elemental symbols [1]
half = '../input_files/HalfLives.csv' #nuclides [0] and half-lives (s) [1]
nuc = pd.read_csv(file,delimiter=',',comment=None,header=0) #the comment=None ignores the pound symbols in cells
elz = pd.read_csv(el_z,delimiter=',',header=0)
t12 = pd.read_csv(half,delimiter=',',header=0)
nuc['P1n'],nuc['P2n'] = pd.to_numeric(nuc['P1n'], downcast="float"),pd.to_numeric(nuc['P2n'], downcast="float")


#for any chain where no neutron emission happens (or none happens past a certain point)
def basic(nuclide,p_list):
    STABLE = np.load('../input_files/Stable_dict.npy',allow_pickle=True)
    STABLE = STABLE.tolist()
    
    #startup + the first one (not in the while loop in case we start with a stable guy)
    #can't exclude the stable guy just bc he's first!
    if nuclide in nuc['Nuclide'].unique():
        ind = nuc[nuc['Nuclide']==nuclide].index.values[-1]
        Z = nuc['Z'][ind]
        N = nuc['N'][ind]
        A = nuc['A'][ind]
        P1n = nuc['P1n'][ind]
        P2n = nuc['P2n'][ind]
        T12 = nuc['Half-Life'][ind]

        if P1n == -1:
            p_list.extend((nuclide,T12,P1n))
        elif P2n == -1 :
            p_list.extend((nuclide,T12,round(100 - P1n,3)))
        else:
            p_list.extend((nuclide,T12,round(100 - P1n - P2n,3)))
    else:
        Element = re.findall('[a-zA-Z]+',nuclide)[0]
        Z = int(elz['Z'][elz[elz['Element']==Element].index].values[-1])
        A = int(re.findall('\d+',str(nuclide))[0])
        N = A-Z
        T12 = t12['T12'][t12[t12['Nuclide']==nuclide].index].values[-1]
        p_list.extend((nuclide,T12,100)) #don't need to signal that it's outside the csv

    Z += 1
    N -= 1
    A = Z+N
    
    #no neutron emission
    while nuclide != STABLE[A]:
        nuclide = str(A)+str(elz['Element'][elz[elz['Z']==Z].index].values[-1])
        if nuclide in nuc['Nuclide'].unique(): #if it's in the list of nuclides
            ind = nuc[nuc['Nuclide']==nuclide].index.values[-1]
            P1n = nuc['P1n'][ind]
            P2n = nuc['P2n'][ind]
            T12 = nuc['Half-Life'][ind]

            if P1n == -1:
                p_list.extend((nuclide,T12,P1n))
            elif P2n == -1 :
                p_list.extend((nuclide,T12,round(100 - P1n,3)))
            else:
                p_list.extend((nuclide,T12,round(100 - P1n - P2n,3)))
        else: #if it's not in the list of nuclides
            T12 = t12['T12'][t12[t12['Nuclide']==nuclide].index].values[-1]
            p_list.extend((nuclide,T12,100))

        Z += 1
        N -= 1
        A = Z+N
        
    return p_list


#takes into account the possibility of P1n and P2n values being nonzero

def P1nP2n(idx,p_lists):
    #this function is for all P1n != 0 or P2n != 0
    
    magic = int(3**idx)
    for ii in range(0,2*magic): 
        #This will triple the number of rows 
        #and duplicate what's in the current rows up to the idx+1 (current nuclide & half-life, not its P val bc that'll differ)
        p_lists.append(p_lists[ii][0:3*idx+2])
        
    for ii in range(0,magic):
        #pull nuclide from list & corresponding vals
        #some will be the same as nu, some will be nu with 1+ fewer neutrons
        #that's the whole point of doing this!
        #last val in list will be half life, not nuclide, so we've gotta go back one more index
        
        end_nuc_1 = str(p_lists[magic+ii][-2])
        end_nuc_2 = str(p_lists[2*magic+ii][-2])

        #this isn't the problem; it actually fixes a lot of things!
        if end_nuc_1 != end_nuc_2:
            end_nucs = [end_nuc_1,end_nuc_2]
        else:
            end_nucs = [end_nuc_1]

        for end_nuc in end_nucs:
            if (p_lists[ii][-1] != 'DUPLICATE') and (end_nuc in nuc['Nuclide'].unique()):
                ind = nuc[nuc['Nuclide']==end_nuc].index.values[-1]
                Z0 = nuc['Z'][ind]
                N0 = nuc['N'][ind]
                A0 = nuc['A'][ind]
                P1n_ = nuc['P1n'][ind]
                P2n_ = nuc['P2n'][ind]
                #this condition includes the condition that P1n_ == -1
                if P1n_ != 0.0000:
                    p_lists[magic+ii].append(round(P1n_,4))
                    #next nuclide
                    Z = Z0 + 1
                    N = N0 - 2
                    A = Z+N
                    nuclide = str(A)+str(elz['Element'][elz[elz['Z']==Z].index].values[-1])
                    p_lists[magic+ii] = basic(nuclide,p_lists[magic+ii])
                else:
                    #we want to take the P0n value from the list that we're copying it from and then do basic
                    #this will make a duplicate list to p_lists[ii] that we'll have to delete later
                    #so we may as well just reset the entire list to be a duplicate
                    p_lists[magic+ii] = copy(p_lists[ii])
                    #creates a flag in the last element that we can pick up on to delete the row later!
                    p_lists[magic+ii].append('DUPLICATE')
                if P2n_ != 0.0000:
                    p_lists[2*magic+ii].append(round(P2n_,4))
                    #next nuclide
                    Z = Z0 + 1
                    N = N0 - 3
                    A = Z+N
                    nuclide = str(A)+str(elz['Element'][elz[elz['Z']==Z].index].values[-1])
                    p_lists[2*magic+ii] = basic(nuclide,p_lists[2*magic+ii])
                else:
                    p_lists[2*magic+ii] = copy(p_lists[ii])
                    #creates a flag in the last element that we can pick up on to delete the row later!
                    p_lists[2*magic+ii].append('DUPLICATE')
            else:
                #we still wanna do the duplicate here 
                #for values that aren't in the main csv and therefore have no P1n/P2n (too small Qß1/2n vals)
                p_lists[magic+ii] = copy(p_lists[ii])
                p_lists[2*magic+ii] = copy(p_lists[ii])
                #creates a flag in the last element that we can pick up on to delete the row later!
                p_lists[magic+ii].append('DUPLICATE')
                p_lists[2*magic+ii].append('DUPLICATE')

    return p_lists


#the part of the program that actually runs
def main(nuclide,filepath='./',Print=False,noNULL=False):

    
    #startup
    if nuclide in nuc['Nuclide'].unique():
        ind = nuc[nuc['Nuclide']==nuclide].index.values[-1]
        Z = nuc['Z'][ind]
        N = nuc['N'][ind]
        A = nuc['A'][ind]
        P1n = nuc['P1n'][ind]
        P2n = nuc['P2n'][ind]

        #initializing the print lists with the first nuclide & no neutron emission
        p_lists = [[]]   
        p_lists[0] = basic(nuclide,p_lists[0])

        for idx,nu in enumerate(p_lists[-1][::2]): #odd elements == all nuclides
            p_lists = P1nP2n(idx,p_lists)

        for row in p_lists:
            if type(row[-1]) != str:
                row.pop()
        #printing to console
        if Print == True:
            for row in p_lists:
                if row[-1] != 'DUPLICATE':
                    print(row)

        #making a csv
        frame_lists = []
        for row in p_lists:
            if row[-1] != 'DUPLICATE':
                frame_lists.append(row)
        frame = pd.DataFrame(frame_lists)
        frame.replace({np.nan: None})
        if noNULL == False:
            filename = str(filepath)+'Decay_Chains_'+str(nuclide)+'.csv'
            frame.to_csv(filename,index=False,header=False,float_format='%.3f')
        else:
            for idx,col in enumerate(frame):
                if idx % 3 == 0: #for the Pxn values (floats)
                    frame[col].fillna(-2.0,inplace=True)
                else: #(both nuclides and half lives are strings)
                    frame[col].fillna('-2.0',inplace=True)
            filename = str(filepath)+'Decay_Chains_'+str(nuclide)+'_Filled.csv'
            frame.to_csv(filename,index=False,header=False,float_format='%.3f')

    else:
        print('The entered nuclide either does not undergo ß- decay \n or does not have sufficient Qß values to allow for neutron emissions.')
