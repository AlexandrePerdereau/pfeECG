#!/usr/bin/env python
# coding: utf-8

# In[1]:



from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

import wfdb


# In[13]:


file = open('./mit-bih-arrhythmia-database-1.0.0/RECORDS')
records = file.readlines()
file.close()


# In[12]:





# In[3]:



annotation = wfdb.rdann('./mit-bih-arrhythmia-database-1.0.0/100', 'atr', sampfrom=0, sampto=110000,return_label_elements=['symbol'],summarize_labels=True)
annotation.fs = 10
wfdb.plot_wfdb(annotation=annotation, time_units='minutes')


# In[26]:


help(wfdb.Annotation)


# In[73]:


wfdb.show_ann_labels()


# In[75]:


good = ['N']
leftBundleBlocks = ['L']
rightBundleBlocks = ['R']
atrialContraction = ['A']
ventricularContraction = ['V']
paced = ['/']
ventricularEscape = ['E']
ventricularFlutterWave = ['!']


# In[6]:




ids = np.in1d(annotation.symbol, good)
# We want to know only the positions
NORMAL = annotation.sample[ids]

ids = np.in1d(annotation.symbol, leftBundleBlocks)
# We want to know only the positions
LBB = annotation.sample[ids]

ids = np.in1d(annotation.symbol, rightBundleBlocks)
# We want to know only the positions
RBB = annotation.sample[ids]

ids = np.in1d(annotation.symbol, atrialContraction)
# We want to know only the positions
APC = annotation.sample[ids]

ids = np.in1d(annotation.symbol, ventricularContraction)
# We want to know only the positions
PVC = annotation.sample[ids]

ids = np.in1d(annotation.symbol, ventricularEscape)
# We want to know only the positions
VEB = annotation.sample[ids]

ids = np.in1d(annotation.symbol, paced)
# We want to know only the positions
PAB = annotation.sample[ids]


# In[62]:


def segmentation(typeBeat):

    liste = []

    for e in records:
        signals, fields = wfdb.rdsamp('./mit-bih-arrhythmia-database-1.0.0/' + e[0:-1], channels = [0]) 

        ann = wfdb.rdann('./mit-bih-arrhythmia-database-1.0.0/' + e[0:-1], 'atr')
       
        ids = np.in1d(ann.symbol, typeBeat)
        imp_beats = ann.sample[ids]
        beats = (ann.sample)
        for i in imp_beats:
            beats = list(beats)
            j = beats.index(i)
            if(j!=0 and j!=(len(beats)-1)):
                x = beats[j-1]
                y = beats[j+1]
                diff1 = abs(x - beats[j])//2
                diff2 = abs(y - beats[j])//2
                liste.append(signals[beats[j] - diff1: beats[j] + diff2, 0])
    
    liste = liste[1:]                
    return liste


# In[76]:


NORMAL = segmentation(good) 
LBB = segmentation(leftBundleBlocks)
RBB = segmentation(rightBundleBlocks)
APC = segmentation(atrialContraction)
PVC = segmentation(ventricularContraction)
VEB = segmentation(ventricularEscape)
PAB = segmentation(paced)
VFW = segmentation(ventricularFlutterWave)


# In[89]:



plt.plot(LBB[0])
plt.plot(LBB[500])


# In[90]:


len(LBB)

