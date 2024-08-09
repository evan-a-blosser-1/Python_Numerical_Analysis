""" Statistics Python Package
        -code adapted from MATH4753 for R


"""
#
import numpy as np
from scipy.stats import norm


##############################
#%% `alpha_ci`:  Confidence Interval 
def Alpha_ci(perr,sample):
    """ Confidence Interval Calculator
            This is a function that takes a desired percentage of confidence, 
            ie a 94% confidence interval, and a vector of sample data as inputs. 
            Then the confidence interval is calculated.
    Args:
        perr (int or float): Percentage of confidence
        sample (array-like): A vector of sample data/a column of data
    
    Returns:
        list: A confidence interval for the given data
    """
    if perr > 1:
        print(f"| You have entered the pertentage {perr} %")
        x_deci = perr/100
        percent=perr
    else:
        x_deci = perr
        percent=perr*100
    ###################
    ### Begin Calc ####
    alpha    = 1- x_deci
    mu       = np.mean(sample)
    sigma    = np.std(sample)
    sam_size = len(sample)
    ########################
    # Norm Dist: mu=0, sig=1
    z_alpha =   norm.ppf((1-alpha/2), loc=0, scale=1)
    #################################################
    ############## Confidence Interval ##############
    Conf_Int_low = mu - z_alpha * (sigma/np.sqrt(sam_size))
    Conf_Int_up  = mu + z_alpha * (sigma/np.sqrt(sam_size))
    ## OUTPUT #############################################
    Confidence_OUT_Message = f"""
{'-'*42}
| {percent}% of the data falls in 
|    the interval:
| ({Conf_Int_low}) <--> ({Conf_Int_up})
{'-'*42}
    """
    print(Confidence_OUT_Message)
    
    return [Conf_Int_low, Conf_Int_up]
#######################################
#%% `z_score`: Outliers within standard devs. 

def z_score(x):
    """Z-score & outlier calculations

    Args:
        x (array): a numpy array (if list or DataFrame, change!)

    Returns:
        list: Z-scores for a data set, the squared values
    """
    ####################### z-score 
    z = (x - np.mean(x))/np.std(x)
    ####################### Outliers
    # z-value
    outlier_z = z[np.abs(z) > 3]
    # Outlier value
    outliers  = x[np.abs(z) > 3]
    ####################### Possible outliers
    poss_out_z   = z[(np.abs(z) >= 2) & (np.abs(z) <= 3)]
    poss_outlier = x[(np.abs(z) >= 2) & (np.abs(z) <= 3)]
    #####################################################
    # Out
    outlier_list = [z,outlier_z,outliers,poss_out_z,poss_outlier]
    ##########################
    Outlier_Out_MEssage = f"""
{'-'*42}
| z = {z}
{'-'*42}
| For the z-outlier: {outlier_z}
| The outliers are:
{outliers} 
{'-'*42}
| For the z-possible: {poss_out_z}
| The possible outliers are:
{poss_outlier} 
{'-'*42}
    """    
    print(Outlier_Out_MEssage)
    return outlier_list 
#################################
#%% 


