good_sum = False

while not good_sum:
    x1=[2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6] # possible duration of a jitter
    x1 = np.repeat(x1,26)
   
    # pick 228 values to match number of total trials (incl. fillers)
    x_r_1 = random.sample(x1, 228) # fixation cross
    x_r_2 = random.sample(x1, 228) # inter cue interval (ICI)
    
    # create dataframe out of the same
    df_1 = pd.DataFrame({'Freq_1': x_r_1}) # fixation
    df_2 = pd.DataFrame({'Freq_2': x_r_2}) # ICI

    
    df_conc = pd.concat([df_1, df_2], axis=1) #make a new dataframe 
    sum_1 = df_conc["Freq_1"].sum() #sum of fix jitters
    sum_2 = df_conc["Freq_2"].sum() #sum of ICI jitters
    
    #limit the maximum duration of the experimnt 
    if sum_1 + sum_2 > 1811: # 1811 = maximum time of 43,48 minutes
        good_sum = False 
    elif sum_1 + sum_2 <= 1811:
        good_sum = True
        jitters_fix = x_r_1
        jitters_ICI = x_r_2
