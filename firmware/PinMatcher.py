# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:14:44 2019

@author: Jorge Ramirez


This code takes the csv file CometDCBFullMapping made by Yipeng and creates
a new csv file with the same exact format, but with two columns appended from
Manuel's firmware report.

The flow is as follows:

pull_report() reads the .rpt file given by Manuel and extracts info that way
    input - filepath of .prt
    output - list of tuples in the form (name, pin #)
    
pull_csv() reads yipeng's csv file into a useable python list
    input - filepath of csv file
    output - list of tuples: (FPGA pin, COMET connector, GBTx pin, Signal ID)
    
match_csv_to_rpt() uses the lists generated by pull_csv() and pull_report() to
create a new master list that combines the tuples made by pull_csv and pull_report
    input - none
    output - master list of tuples: 
        (FPGA pin, COMET connector, GBTx pin, Signal ID, firmware name, pin #)

gen_csv() uses the master list from match_csv_to_rpt() and creates a CSV file.
    input - filepath of new csv file
    output - csv file

"""

import csv

# method to open .rpt file and pull relevant lines
def pull_report(filepath="resources/COMET_20ELKs_Pins.rpt"):
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
def pull_csv(filepath="resources/CometDcbFullMapping.csv"):
    
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
            # look inside the firmware list to find the matching pin
            for pin_tuple in firmware_list:
                if line[0][15:] == pin_tuple[1]:
                    master_list.append(line+pin_tuple)
                
    return master_list

def gen_csv(master_list=match_csv_to_rpt(), csvpath="MatchedPins.csv"):
    
    with open(csvpath, 'w', newline='') as f:  # create csv file
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # initialize writer
        writer.writerow(["COMET FPGA pin","Pathfinder COMET connector", "DCB data GBTx pin"
                         ,"Signal ID", "Firmware Name", "Firmware Pin #"])
                #  column headers
                
        writer.writerows(master_list)  # write our entire list
     
    return
    

