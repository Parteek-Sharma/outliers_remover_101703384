# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:47:20 2020

@author: Parteek Sharma
"""

#%%  imports
import numpy as np
import sys
#%%define outliers function
def delete_outliers(data):
    quantile1, quantile3= np.percentile(data,[25,75])
    iqr=quantile3-quantile1
    lower_bound_val = quantile1 -(1.5 * iqr) 
    upper_bound_val = quantile3 +(1.5 * iqr)
    count = 0
    for i in range(len(data)-1,0,-1):
        if data[i]<lower_bound_val or data[i]>upper_bound_val:
            data=np.delete(data,i)
            count = count + 1
    return (data,count)            



def main():
    # %% dataset input
    filename = sys.argv[1]
    try:
        data = np.genfromtxt(filename, delimiter=',')    
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    #%%run function
    # data = np.genfromtxt('outlier_dataset.csv', delimiter=',')
    (data,deleted) = remove_outliers.delete_outliers(data)
    print(len(data))
    #%% dataset & output
    filename = sys.argv[2]
    try:
        np.savetxt(filename,data, delimiter=',')
        print("number of rows deleted: ",deleted)    
    except OSError:
        print('cannot open', filename)
        sys.exit(0)