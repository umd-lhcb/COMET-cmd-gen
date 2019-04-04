# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:14:44 2019

@author: Jorge Ramirez
"""

import csv

# method to open .rpt file and pull relevant lines
def pull_report(filepath="COMET_20ELKs_Pins.rpt"):
    
    with open(filepath) as f:  # open .rpt file
        raw_data = f.readlines()    # create list "raw_data" from report file
    
    report_list = raw_data[12:]  # strip out the header
    
    return report_list  


# method to open .csv file and save each row as a tuple
def pull_csv(filepath="CometDcbFullMapping.csv"):
    
    csv_list = [tuple(row) for row in csv.reader(open(filepath, 'r'))]  # list comprehension!
    del csv_list[0]  # strip out header


def gen_list():
    
    report_list = pull_report()
    
    
    
    
    pass
    
