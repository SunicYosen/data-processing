"""
Read Excel
ticker	assets_total	ROA_annual	sales_annual	rd_expense	sic	debt_to_assets	firm_id	RD_spending	csp_annual	ad_intensity_industry	
southafrica_dum	sic_2	patent_num_2	cited_num_2	red	constituency	_merge	ROA
"""
#! /usr/bin/env python3

import pandas as pd

def read_excel(excel_file = 'data_origin.xlsx', sheet_name='Sheet1'):
    if 'xlsx' in excel_file:
        data_frame = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')
    else:
        data_frame = pd.read_excel(excel_file, sheet_name=sheet_name, engine='xlrd')
    
    return data_frame

if __name__ == '__main__':
    excel_file = 'data_origin.xls'
    data_frame = read_excel(excel_file=excel_file, sheet_name='Sheet1')
    print(data_frame)
