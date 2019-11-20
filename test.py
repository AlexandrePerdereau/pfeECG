# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:33:01 2019

@author: alexa
"""

import wfdb
import matplotlib.pyplot as plt
import numpy as np

def beat_annotations(annotation):
    """ Get rid of non-beat markers """
    """'N' for normal beats. Similarly we can give the input 'L' for left bundle branch block beats. 'R' for right bundle branch block
        beats. 'A' for Atrial premature contraction. 'V' for ventricular premature contraction. '/' for paced beat. 'E' for Ventricular
        escape beat."""
    
    good = ['N']   
    ids = np.in1d(annotation.symbol, good)

    # We want to know only the positions
    beats = annotation.sample[ids]

    return beats



records =open(".\mit-bih-arrhythmia-database-1.0.0/RECORDS")
listeFichier = records.readlines()
records.close()
for fichier in listeFichier:
    sig, fields = wfdb.rdsamp('.\mit-bih-arrhythmia-database-1.0.0/'+fichier[0:-1])

