# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:14:44 2019

@author: Jorge Ramirez
"""

def pull_report(filepath="COMET_20ELKs_Pins.rpt"):  # method to open .rpt file and pull relevant lines
    
    with open(filepath) as f:  # open txt file
        raw_data = f.readlines()    # create list "raw_data" from file
    

    return raw_data



def gen_list():
    
    
    
    pass
    
