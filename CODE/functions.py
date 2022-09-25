import pandas as pd

def read_data(path):
	# read csv
	pass


def policy_difference(w,policy_day,days,df,policy_num,state=""):
    """
    w : window size; threshold days before any bp to consider policy impact on bp. 
    policy_day : the day of policy implementation 
    days : days in the timeline [1 .... n days]
    df : Data Frame name
    policy_num : number of policies for analysis
    string : Abb. of the state

    Description : calculating the difference from 
    """
    _ = f"{state}_p"+ np.str(policy_num)  
    
    for i in range(len(days)):

        # days[i] - w > P: take difference else: try infinity
        if days[i] < policy_day:
            df[_][i] = np.inf 
        else: 
            df[_][i] = abs(days[i] - w - policy_day) 

def policy_impact(data,beta,df,policy_num,state=""):
    """
    data : passing the exponential decay value of each policy eg. dataFrame_name.policy_name (al_data.al_p5)
	beta = hyperparameter. eg: [0.001]
	df : dataframe name eg. al_data
	policy_num : policy number [1,2,3,4,5,6]

	Description: Calculating the exponential decay using the function. 
    """
    _ = "p"+ np.str(policy_num) 
    df[_] = [np.exp(-beta*x) for x in data]
    


def the_day(dates):
	"""
	Pass the date and get the index on that day. The index can be used as 
	count of days
	dates : "01/01/2020"
	"""
    if len(data[data.Date == dates]) != 0:
        return data[data.Date == dates].days.values[0]
    else:
        return 0

bp = {}  # storing breakpoint of all state in the dictionary.
def breakpoints(data,state = ""):
	"""
	data : passing the dataframe eg. al_data
	state : ""

	Description: Calculating the change in variance and mean in the time series data. 
				 To calculate the Change point method we used PELT method to calculate
				 the breakpoints. 
	"""
    model='rbf'
    X = data[f"{state}_cases"].values
    algo = rpt.Pelt(model=model).fit(X)
    result = algo.predict(pen=10)
    bp[state] = result
    # rpt.display(X,result,figsize=(8,3))
    # [plt.axvline(x) for x in range(len(6))]  # Include policy day in bp graph. *Later
    # plt.title(f"{state} Confirmed Cases")
    # plt.show()

def percent_change(data,state=""):
    # Method 2: -> % change in daily confirmed cases

    data["%_change"] = data[state+"_cases"].pct_change()
    data["%_change"].fillna(0,inplace=True)
    
def target_label_with_pelt(data,state=""):
    # METHOD 1 -> Break Point method -> [0,1] -> [No BP, BP]
    """
    Target Assigning 1 where the BP is found using PELT, otherwise 0.
        
    Problems: 1) we few BP found. in all 303 for all 50 states. 
                creating inbalance dataset.
    """
    for i in bp[state]:
        data['target_with_PELT'][i-1] = 1
    data['target_with_PELT'].fillna(0,inplace=True)
    data['target_with_PELT'] =data['target_with_PELT'].astype(int)

    
def target_conse_3(data,target): 
    """
    data = ca_data.%change
    target = ca_data.target_conse_3
    
    Target Assigning 1 when we see drop in % change in 
    number of cases for 5 consecutive days.

    Problems: 1) for cal state we found on 4 1's. which is very 
    less when considered 5 consecutive day delays.
    2) 
    """
    for i in range(5,len(data)):
        if data[i]<data[i-1]:                   # 5 - 4th day
            if data[i-1] < data[i-2]:           # 4 - 3nd day
                if data[i-2] < data[i-3]:       # 3 - 2rd day
                    if data[i-3] < data[i-4]:   # 2 - 1st day
                        # if data[i+4] < data[i-5]:
                            # target[i] = 1
                            # target[i+1] = 1
                            # target[i+2] = 1
                        target[i] = 1
        
    target.fillna(0,inplace=True)

def target_conse_3_policy(data,target,policy_day):
    """
    data= ca_data.%_change
    target = ca_data.target_conse_3_policy
    
    in this case, the decay of change of cases is 
    considered after the policy was implemented. However,
    No positive result found.
    """

    for j in policy_day:   # [34,50,100,230,300,...]
	    if data[j] < data[j+1]:
	        if data[j+1] < data[j+2]:
	            if data[j+2] < data[j+3]:
	                # target[j]   = 1
	                # target[i+1] = 1
	                # target[i+2] = 1
	                target[j+3] = 1
	                
	target.fillna(0,inplace=True)    

def policy_decay_plot(states):
	"""
	states : passing the list of all state's DataFrame in the Function.  
	
	sta = [al_data,ak_data,az_data,ar_data,ca_data,co_data,ct_data,de_data,dc_data,fl_data,ga_data,hi_data,id_data,il_data,in_data,ia_data,ks_data,ky_data,
          la_data,md_data,ma_data,mi_data,mn_data,ms_data,mo_data,mt_data,ne_data,nv_data,nh_data,nj_data,nm_data,ny_data,nd_data,oh_data,ok_data,or_data,
          pa_data,ri_data,sc_data,sd_data,tn_data,tx_data,ut_data,vt_data,va_data,wa_data,wv_data,wi_data,wy_data]
	"""

	name = [x.upper() for x in list(bp.keys())]

	fig,ax = plt.subplots(17,3,figsize=(30,80))
	fig.subplots_adjust(hspace=0.8, wspace=0.2)
	s=0

	for i in range(0,17):
	    for j in range(0,3):
	        try:
	            ax[i][j].plot(sta[s].iloc[:,8:14],linewidth=2)
	            ax[i][j].set_title(f"{name[s]}",fontsize=20,fontweight = 'bold')
	            s+=1
	        except IndexError:
	            continue
	fig.supxlabel("Days",fontsize=25,fontweight = 'bold')
	fig.supylabel("Exponential Decay",fontsize=25,fontweight = 'bold')
	# plt.legend()
	fig.suptitle("Exponential Decay Curve of Policies for each State of the USA",fontsize =25,fontweight = 'bold')
	ax[16,2].set_axis_off()
	ax[16,1].set_axis_off()
	plt.tight_layout(pad=3)
	# save_plot() function. 	
	plt.show()

def data_seperation(states):
	"""
	states: list of all states DataFrame

	return: positive_data, negative_data

	positive_data : data having target label as 1
	negative_data : data having target label as 0
	eg.
	states = [al_data,
          ak_data,az_data,ar_data,ca_data,co_data,ct_data,de_data,dc_data,fl_data,ga_data,hi_data,id_data,il_data,in_data,ia_data,ks_data,ky_data,
          la_data,md_data,ma_data,mi_data,mn_data,ms_data,mo_data,mt_data,ne_data,nv_data,nh_data,nj_data,nm_data,ny_data,nd_data,oh_data,ok_data,or_data,
          pa_data,ri_data,sc_data,sd_data,tn_data,tx_data,ut_data,vt_data,va_data,wa_data,wv_data,wi_data,wy_data]
	"""
	# collecting positive data
	for i in states:
    positive_data = positive_data.append(i[:300][i.target_conse_3 == 1].iloc[:,8:],ignore_index=True)
    negative_data = negative_data.append(i[:300][i.target_conse_3 == 0].iloc[:,8:],ignore_index=True)

    # removing null entries
    positive_data = positive_data.loc[~(positive_data.iloc[:,:6]==0).all(axis=1)] # FROM 4616 to 1443
	negative_data = negative_data.loc[~(negative_data.iloc[:,:6]==0).all(axis=1)] # FROM 22824 TO 13255
	
	return positive_data,negative_data

def combine_data(states):
	"""
	states: list of all states DataFrame
	"""

	combine_data=states[:1].iloc[29:359:,8:14]
	for st in states[1:]:
    	combine_data = combine_data.append(st.iloc[29:359:,8:14],ignore_index=True)

    # combine_data.to_csv("state_combine_data.csv")
    return combine_data