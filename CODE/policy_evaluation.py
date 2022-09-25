import numpy as np
import pandas as pd

def the_day(dates):
    if len(data[data.Date == dates]) != 0:
        return data[data.Date == dates].days.values[0]
    else:
        return 0


def policy_difference(w ,
                      policy_start_day
                      ,policy_end_day,
                      days
                      ,df
                      ,policy_num,
                      state="",
                      beta=0.01,):
    """
   
    w : window size; threshold days before any bp to consider policy impact on bp. 
    policy_day : the day of policy implementation 
    """
    
    _ = f"{state}_p"+ np.str(policy_num)   #eg; al_p1
    last_index=0
    
                    # 
    for i in range(len(days[:410])):  
        if policy_start_day == 0 or days[i]<policy_start_day:  # before policy imposed
            df[_][i] = np.exp(-beta * np.inf)
        elif policy_start_day !=0 and policy_end_day !=0:
            if policy_start_day + 5 <= days[i] <= policy_end_day: # in b.w policy imposed and lifted
                df[_][i] = index[f"{ state.upper()}"][i]  
                last_index = df[_][i]
            elif policy_end_day < days[i] < policy_end_day + w:    # After the policy lifted with lag of W 
days    
                df[_][i] = last_index
            else:                                      
                df[_][i] = last_index * (np.exp(-beta* abs(days[i] - w - policy_end_day)))   # decay curve 
after policy was lifted.        
        else: 
            df[_][i] = index[f"{state.upper()}"][i]
            
            
    # df.fillna(0,inplace=True)


def policy_impact(data,beta,df,policy_num,state=""):
    """
    x: policy difference; difference b/w the bp and the day policy was implemented.
    w = window size; threshold days before any bp to consider policy impact on bp. 
    beta = hyperparameter
    """
    _ = "p"+ np.str(policy_num) 
    df[_] = [np.exp(-beta*x) for x in data]