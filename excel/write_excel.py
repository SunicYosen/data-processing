"""
Write excel
ticker	assets_total	ROA_annual	sales_annual	rd_expense	sic	debt_to_assets	firm_id	RD_spending	csp_annual	ad_intensity_industry	
southafrica_dum	sic_2	patent_num_2	cited_num_2	red	constituency	_merge	ROA
"""

#! /usr/bin/env python3

import pandas as pd
import numpy as np
import openpyxl

def write_excel(companies, file_name='results.xlsx'):

    wb          = openpyxl.Workbook()
    ws          = wb.create_sheet('Result')
    years_array = range(1994, 2014)
    menu_row    = ['year', 'ticker', 'sic_2','firm_id', 'assets_total', 'csp_annual', 'rd_expense', 'ad_intensity_industry', 'sales_annual', 'debt_to_assets', 'red', 'constituency', 'ROA']
    ws.append(menu_row)

    for key in companies:
        companies[key].set_valid()

    for year in years_array:
        weight_dict = {year-3:0.25, year-2:0.5, year-1:1.0}
        for key in companies:
            if (companies[key].valid):

                companies[key].get_sic_2_actual()
                csp_annual_cal = companies[key].get_csp_annual_cal(weight_dict=weight_dict)
                rd_expense_cal = companies[key].get_rd_expense_cal(weight_dict=weight_dict)
                ad_intensity_industry_cal = companies[key].get_ad_intensity_industry_cal(weight_dict=weight_dict)
                sales_annual_cal = companies[key].get_sales_annual_cal(weight_dict=weight_dict)
                assets_total_cal = companies[key].get_assets_total_cal(weight_dict=weight_dict)
                debt_to_assets_cal = companies[key].get_debt_to_assets_cal(weight_dict=weight_dict)

                try:
                    roa          = companies[key].roa_annual[year]
                    red          = companies[key].red[year]
                    constituency = companies[key].constituency[year]
                    firm_id      = companies[key].firm_id[year]
                except:
                    roa = None
                    red = None
                    constituency = None
                    firm_id = None

                compare_row = [ companies[key].sic_2_actual, 
                                assets_total_cal,
                                csp_annual_cal, 
                                rd_expense_cal, 
                                ad_intensity_industry_cal, 
                                sales_annual_cal, 
                                debt_to_assets_cal, 
                                roa
                ]

                company_row = [ year, 
                                companies[key].name, 
                                companies[key].sic_2_actual,
                                firm_id,
                                assets_total_cal,
                                csp_annual_cal, 
                                rd_expense_cal, 
                                ad_intensity_industry_cal, 
                                sales_annual_cal, 
                                debt_to_assets_cal, 
                                red, 
                                constituency, 
                                roa
                ]

                # Remove none row
                for data in compare_row:
                    if (pd.isnull(data) or data==None):
                        continue

                ws.append(company_row)

    wb.save(file_name)

    print("[+] Info: Write Excel Done!")
