# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:46:16 2019

@author: Jorge Ramirez

This script searches inside DeadPins.txt and sees if they show up inside
MatchedPins.csv. If it does, then it prints it out.

Why? Because DeadPins.txt does not have the firmware name/# of the pins, but
MatchedPins.csv does.

"""

import PinMatcher  # import other script we wrote
import csv

def pull_deadpins(filepath="resources/DeadPins.txt"):
    
    with open(filepath) as f:  # open .rpt file
        raw_data = f.readlines()    # create list "raw_data" from report file

    return raw_data


def identify_deadpins():
    identified_deadpins = []
    deadpins_list = pull_deadpins()  # pull in our dead pin list
    master_list = PinMatcher.match_csv_to_rpt()  # pull in our reference
    
    for line in deadpins_list:
        for reference in master_list:
            if line[:19].strip() == reference[0].strip():  
              # [:19] for first column, [0] for first column
                identified_deadpins.append(reference)  # reference is dead 
                
    PinMatcher.gen_csv(master_list=identified_deadpins, csvpath="DeadPins.csv")   
             
    return identified_deadpins

    
