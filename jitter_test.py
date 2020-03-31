## -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random
import pandas as pd

import matplotlib.pyplot as plt

randomized_3 = False

while randomized_3 == False:
    

    appended_data = []
    appended_data_2 = []
    
    for iterations in range(0,6):
        
        good_sum = False
     
        while not good_sum:
    
            randomized = False
            randomized_2 = False
        
            x1=[2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6] # possible duration of a jitter
            x1 = np.repeat(x1,5)
           
            # pick 228 values to match number of total trials (incl. fillers)
            x_r_1 = random.sample(x1, 38) # fixation cross
            x_r_2 = random.sample(x1, 38) # inter cue interval (ICI)
            
            # create dataframe out of the same
            df_1 = pd.DataFrame({'Freq_1': x_r_1}) # fixation
            df_2 = pd.DataFrame({'Freq_2': x_r_2}) # ICI
        
            
            df_conc = pd.concat([df_1, df_2], axis=1) #make a new dataframe 
            sum_1 = df_conc["Freq_1"].sum() #sum of fix jitters
            sum_2 = df_conc["Freq_2"].sum() #sum of ICI jitters
            
            if sum_1 + sum_2 > 302: #5,03 minutes per loop; 30,2 min per test (+13,3) = max. 43,5 min in total
                good_sum = False 
            elif sum_1 + sum_2 <= 302:
                good_sum = True
                jitters_fix = x_r_1
                jitters_ICI = x_r_2
        
        #limit the maximum duration of the experimnt 
        while not randomized: 
            df_conc_1 = df_conc.sample(frac=1).reset_index(drop=True)
            for i in range(0, len(df_conc_1)): 
                try:
                    if i == len(df_conc_1) - 1:
                        randomized = True                
                    elif (df_conc_1['Freq_1'][i] != df_conc_1['Freq_1'][i+1]) and (df_conc_1['Freq_1'][i] != df_conc_1['Freq_1'][i+2]) and (df_conc_1['Freq_2'][i] != df_conc_1['Freq_2'][i+1]) and (df_conc_1['Freq_2'][i] != df_conc_1['Freq_2'][i+2]):
                        continue
                    elif ((df_conc_1['Freq_1'][i] == df_conc_1['Freq_1'][i+1]) and (df_conc_1['Freq_1'][i] == df_conc_1['Freq_1'][i+2])) or ((df_conc_1['Freq_2'][i] == df_conc_1['Freq_2'][i+1]) and (df_conc_1['Freq_2'][i] == df_conc_1['Freq_2'][i+2])): # or (df_conc_1['Freq_2'][i] == df_conc_1['Freq_2'][i+2]):
                        break
                except KeyError:
                    pass
                 
        appended_data.append(df_conc_1)
   
    merged_jitters = pd.concat(appended_data, ignore_index=True)
            
    x=37

    for iteration in range(0,6):         
        if x == 227:
            randomized_3 = True
        elif (merged_jitters['Freq_1'][x] != merged_jitters['Freq_1'][x+1]) and (merged_jitters['Freq_1'][x] != merged_jitters['Freq_1'][x+2]) and (merged_jitters['Freq_2'][x] != merged_jitters['Freq_2'][x+1]) and (merged_jitters['Freq_2'][x] != merged_jitters['Freq_2'][x+2]):                                                
            x = x+38
            print("good")
        elif ((merged_jitters['Freq_1'][x] == merged_jitters['Freq_1'][x+1]) and (merged_jitters['Freq_1'][x] == merged_jitters['Freq_1'][x+2])) or ((merged_jitters['Freq_2'][x] == merged_jitters['Freq_2'][x+1]) and (merged_jitters['Freq_2'][x] == merged_jitters['Freq_2'][x+2])):
            break

merged_jitters.to_excel("Jitters_total.xlsx", index=False) 

jitters_fix = merged_jitters['Freq_1']
jitters_ICI = merged_jitters['Freq_2']

x_r_1 = jitters_fix.tolist()
x_r_2 = jitters_ICI.tolist()
