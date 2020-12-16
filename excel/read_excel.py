"""
Read Excel
"""
#! /usr/bin/env python3

import pandas as pd

def read_excel(excel_file = 'data_origin.xlsx', sheet_name='Sheet1'):
    data_frame = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')
    
    return data_frame

if __name__ == '__main__':
    excel_file = 'data_origin.xlsx'
    read_excel(excel_file=excel_file, sheet_name='Sheet1')
