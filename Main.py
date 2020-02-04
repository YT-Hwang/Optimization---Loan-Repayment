# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:09:46 2019

@author: Yun Hwang
"""

'''
1. Objective Function: N = -[ln(1-[(PV*i)/PMT])/ln(1+i)]

    N = number of month remaining
    PV = Present value or outstanding loan balance
    PMT = Monthly Payment
    i = monthly interest rate (APR / 12)

2. Constraints:
    a) PMT1 + PMT2 + PMT3 + PMT4 + PMTn = X(how much one can afford)
    b) total time should be less than desired time.
    c)
    
3. Find the Max N for that specific allocation.
4. Find the Min N for the entire combination of allocation from 3.
'''

from scipy.optimize import fmin_slsqp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import log


def obj_func(PV, PMT, APR):
    i = (APR/12)/100
    N = round(-(log(1-((PV*i)/PMT))/log(1+i)))
    return N

obj_func(3000, 100, 6)
    
def eq_const1(PMT, affordable_money):
    total_PMT = sum(PMT) - affordable_money
    return total_PMT


My_Loans = {
    'Name' : ['BOA', 'Sapire','Southwest','SallieMae'],
    'Principal' : [2959.59, 7672.04, 5597.32, 22766.63],
    'APR' : [6, 4, 4, 5]
}
My_Loans = pd.DataFrame(My_Loans)

PMT = []
PV = My_Loans['Principal']
APR = My_Loans['APR']


N1 = obj_func(PV[0], PMT =  ,APR[0])
N2 = obj_func(PV[1], PMT =  ,APR[1])
N3 = obj_func(PV[2], PMT =  ,APR[2])


for i in My_Loans.iloc[:,0]:
    print(i)
    
    
sum = 12
cand = list(range(sum))
arr_size = len(cand)

def find3Numbers(cand, arr_size, sum): 
    answers = []
    # Fix the first element as A[i] 
    for i in range( 0, arr_size-2): 
  
        # Fix the second element as A[j] 
        for j in range(i + 1, arr_size-1):  
              
            # Now look for the third number 
            for k in range(j + 1, arr_size): 
                if cand[i] + cand[j] + cand[k] == sum: 
                    print("Triplet is", cand[i], 
                          ", ", cand[j], ", ", cand[k]) 
                    answers = answers.append([cand[i], cand[j], cand[k]])
                    
    return answers  
    

answers = find3Numbers(cand, len(cand), sum)



PMT_opt = fmin_slsqp(obj_func, np.array([0, 0]), eqcons=[eq_const1()])


        


answers = []
# Fix the first element as A[i] 
for i in range(0, arr_size-2): 
  
    # Fix the second element as A[j] 
    for j in range(i + 1, arr_size-1):  
          
        # Now look for the third number 
        for k in range(j + 1, arr_size): 
            if cand[i] + cand[j] + cand[k] == sum: 
                answers.append([cand[i], cand[j], cand[k]])
                    
