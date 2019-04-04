# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:14:44 2019

@author: Jorge Ramirez
"""

import csv

# method to open .rpt file and pull relevant lines
def pull_report(filepath="COMET_20ELKs_Pins.rpt"):
    report_list = []
    
    with open(filepath) as f:  # open .rpt file
        raw_data = f.readlines()    # create list "raw_data" from report file
    raw_data = raw_data[12:]  # strip out the header
    
      # manually grab the first and second columns from raw_data  
      # save both columns into a tuple
    for line in raw_data:
        firmware_name = line[:20]    # first column
        firmware_pin = line[20:24]   # second column
        
        report_list.append((firmware_name.strip(),firmware_pin.strip()))  
            # append new tuple to list, use .strip() to remove whitespace
                        
    return report_list

# method to open .csv file and save each row as a tuple
def pull_csv(filepath="CometDcbFullMapping.csv"):
    
    csv_list = [tuple(row) for row in csv.reader(open(filepath, 'r'))]  # list comprehension!
    del csv_list[0]  # strip out header
    
    return csv_list  


'''

Keep identifiers A/B and J1/J2 from comet

'''

# method to take report_list and grab pin # and firmware name
def match_csv_to_rpt():
    
    report_list = pull_report()
    
    
    
    pass
    
