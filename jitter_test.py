good_sum = False

while not good_sum:
    x1=[2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
    x1 = np.repeat(x1,26)
    
    x_r_1 = random.sample(x1, 228)
    x_r_2 = random.sample(x1, 228)
    
    df_1 = pd.DataFrame({'Freq_1': x_r_1})
    df_2 = pd.DataFrame({'Freq_2': x_r_2})

    
    df_conc = pd.concat([df_1, df_2], axis=1)
    sum_1 = df_conc["Freq_1"].sum()
    sum_2 = df_conc["Freq_2"].sum()
    
    if sum_1 + sum_2 > 1811: # maximum time of 43,48 minutes (all incl.)
        good_sum = False
    elif sum_1 + sum_2 <= 1811:
        good_sum = True
        jitters_fix = x_r_1
        jitters_ICI = x_r_2