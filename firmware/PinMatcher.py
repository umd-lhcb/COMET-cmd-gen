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

# method to take report_list and grab pin # and firmware name
def match_csv_to_rpt():
    
    firmware_list = pull_report()  # get list of tuples from report
    cometdcb_list = pull_csv()     # get list of tuples from csv

    '''
    this nested for loop works to separate CometA and CometB into 4 lists,
    CometA J1, CometA J2, CometB J1, CometB J2 using string manipulation.
    i.e. since yipeng's CSV file is uniform, A or B is always located at column 0
    at index 6, and J1 or J2 is always located at column 0 at index 9.
    '''
    
    A_J1, B_J1, A_J2, B_J2 = [],[],[],[]
    all_comet_lists = [A_J1, B_J1, A_J2, B_J2]
    
    for line in cometdcb_list:   # remember each line is a tuple with 4 columns
        if line[0][6] == "A":
            if line[0][9] == "1":
                A_J1.append(line)
            else:
                A_J2.append(line)
                
        if line[0][6] == "B":
            if line[0][9] == "1":
                B_J1.append(line)
            else:
                B_J2.append(line)
    
    master_list = []
    for cometlist in all_comet_lists:  # now match pin numbers on one list to the other
        for line in cometlist:
            pass
        pass
    
            
    
    
    
    return all_comet_lists

def identify_matches():
    
    pass
    

