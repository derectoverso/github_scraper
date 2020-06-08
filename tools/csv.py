# -*- coding: utf-8 -*-
# CSV tools
# Version 1.0.0
# Date: 07/June/2020

import csv

# Write fields names to CSV header
def write_header_to_csv(file_name, dict_header):
    if file_name is None:
        print("No file name passed for CSV file.")
        return

    try:
        with open(file_name, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=dict_header)
            writer.writeheader()
    except IOError:
        print("I/O error")

# Write fields values to CSV body
def write_dict_to_csv(file_name, data_dict):
    if file_name is None:
        print("No file name passed for CSV file.")
        return
    
    try:
        with open(file_name, 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data_dict[0].keys())
            for item in data_dict:
                writer.writerow(item)
    except IOError:
        print("I/O error")