# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:55:05 2020

@author: Parteek Sharma
"""
from outliers_remover_101703384.remove_outliers import remove_outliers

#%%  imports
import numpy as np
import sys
from outliers_remover_101703384.remove_outliers import remove_outliers

# %% dataset input
filename = sys.argv[1]
try:
    data = np.genfromtxt(filename, delimiter=',')    
except OSError:
    print('cannot open', filename)
    sys.exit(0)
    
#%%run function
# data = np.genfromtxt('outlier_dataset.csv', delimiter=',')
(data,deleted) = delete_outliers(data)
print(len(data))
#%% dataset & output
filename = sys.argv[2]
try:
    np.savetxt(filename,data, delimiter=',')
    print("number of rows deleted: ",deleted)    
except OSError:
    print('cannot open', filename)
    sys.exit(0)