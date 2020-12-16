"""
Write excel
"""

#! /usr/bin/env python3

import openpyxl

def write_excel(companies, file_name='results.xlsx'):

    wb        = openpyxl.Workbook()
    ws        = wb.create_sheet('Result')
    menu_row  = ['ticker', 'Assets', 'Sales', 'Innovation', 'Risk', 'CSP', 'Differentiation', 'ROA', 'Sic_2', 'CSP_Diff', 'CSP_Inno']
    ws.append(menu_row)

    for key in companies:
        companies[key].get_assets()
        companies[key].get_sales()
        companies[key].get_innovation()
        companies[key].get_risk()
        companies[key].get_csp()
        companies[key].get_differentiation()
        companies[key].get_csp_diff()
        companies[key].get_csp_inno()
        companies[key].get_sic_2_actual()

        try:
            roa = companies[key].ROA[2001]
        except:
            roa = None

        company_row = [companies[key].name, \
                       companies[key].assets, \
                       companies[key].sales, \
                       companies[key].innovation, \
                       companies[key].risk, \
                       companies[key].csp, \
                       companies[key].differentiation, \
                       roa, \
                       companies[key].sic_2_actual, \
                       companies[key].csp_diff, \
                       companies[key].csp_inno]

        # Remove none row
        if(None in company_row):
            # print(company_row)
            continue

        ws.append(company_row)

    wb.save(file_name)

    print("[+] Info: Write Excel Done!")
