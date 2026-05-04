# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:26:45 2023

@author: Galactikhan
"""
import math as mt
# S Stumpff function #########################################
def S_Stumpff(z,Stumpff_lim):
    S_Stumpff = 0
    for k in range (0,Stumpff_lim):
        S_Stumpff += ((-1)**k)*((z)**k)/mt.factorial(2*k + 3)
    return S_Stumpff
# C Stumpff function #########################################
def C_Stumpff(z,Stumpff_lim):
    C_Stumpff = 0
    for k in range(0,Stumpff_lim):
        C_Stumpff += ((-1)**k)*((z)**k)/mt.factorial(2*k + 2)
    return C_Stumpff
