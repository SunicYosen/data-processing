"""
Set Company
ticker	assets_total	ROA_annual	sales_annual	rd_expense	sic	debt_to_assets	firm_id	RD_spending	csp_annual	ad_intensity_industry	
southafrica_dum	sic_2	patent_num_2	cited_num_2	red	constituency	_merge	ROA
"""

#! /usr/bin/env python3

import numpy as np
import pandas as pd
from company import Company
from read_excel import read_excel

def set_company(data_frame):
    companies = {}

    for index in range(len(data_frame)):
        data_year         = data_frame['year'][index]
        company_name      = data_frame['ticker'][index]

        print('{}:{}'.format(data_year, company_name))

        data_array        = [data_frame['assets_total'][index],
                             data_frame['ROA_annual'][index],
                             data_frame['sales_annual'][index],
                             data_frame['rd_expense'][index],
                             data_frame['sic'][index],
                             data_frame['debt_to_assets'][index],
                             data_frame['firm_id'][index],
                             data_frame['RD_spending'][index],
                             data_frame['csp_annual'][index],
                             data_frame['ad_intensity_industry'][index],
                             data_frame['southafrica_dum'][index],
                             data_frame['sic_2'][index],
                             data_frame['patent_num_2'][index],
                             data_frame['cited_num_2'][index],
                             #  data_frame['red'][index],
                             #  data_frame['constituency'][index],
                             data_frame['_merge'][index]
                            ]

        if (company_name in companies):
            companies[company_name].assets_total.update({data_year:data_frame['assets_total'][index]})
            companies[company_name].roa_annual.update({data_year:data_frame['ROA_annual'][index]})
            companies[company_name].sales_annual.update({data_year:data_frame['sales_annual'][index]})
            companies[company_name].rd_expense.update({data_year:data_frame['rd_expense'][index]})
            companies[company_name].sic.update({data_year:data_frame['sic'][index]})
            companies[company_name].debt_to_assets.update({data_year:data_frame['debt_to_assets'][index]})
            companies[company_name].firm_id.update({data_year:data_frame['firm_id'][index]})
            companies[company_name].rd_spending.update({data_year:data_frame['RD_spending'][index]})
            companies[company_name].csp_annual.update({data_year:data_frame['csp_annual'][index]})
            companies[company_name].ad_intensity_industry.update({data_year:data_frame['ad_intensity_industry'][index]})
            companies[company_name].southafrica_dum.update({data_year:data_frame['southafrica_dum'][index]})
            companies[company_name].sic_2.update({data_year:data_frame['sic_2'][index]})
            companies[company_name].patent_num_2.update({data_year:data_frame['patent_num_2'][index]})
            companies[company_name].cited_num_2.update({data_year:data_frame['cited_num_2'][index]})
            companies[company_name].red.update({data_year:data_frame['red'][index]})
            companies[company_name].constituency.update({data_year:data_frame['constituency'][index]})
            companies[company_name]._merge.update({data_year:data_frame['_merge'][index]})

            for data in data_array:
                if pd.isnull(data):
                    # print(data_year, company_name)
                    companies[company_name].valid = False
                    break
        
        else:
            company_temp = Company()
            company_temp.name = data_frame['ticker'][index]
            company_temp.assets_total.update({data_year:data_frame['assets_total'][index]})
            company_temp.roa_annual.update({data_year:data_frame['ROA_annual'][index]})
            company_temp.sales_annual.update({data_year:data_frame['sales_annual'][index]})
            company_temp.rd_expense.update({data_year:data_frame['rd_expense'][index]})
            company_temp.sic.update({data_year:data_frame['sic'][index]})
            company_temp.debt_to_assets.update({data_year:data_frame['debt_to_assets'][index]})
            company_temp.firm_id.update({data_year:data_frame['firm_id'][index]})
            company_temp.rd_spending.update({data_year:data_frame['RD_spending'][index]})
            company_temp.csp_annual.update({data_year:data_frame['csp_annual'][index]})
            company_temp.ad_intensity_industry.update({data_year:data_frame['ad_intensity_industry'][index]})
            company_temp.southafrica_dum.update({data_year:data_frame['southafrica_dum'][index]})
            company_temp.sic_2.update({data_year:data_frame['sic_2'][index]})
            company_temp.patent_num_2.update({data_year:data_frame['patent_num_2'][index]})
            company_temp.cited_num_2.update({data_year:data_frame['cited_num_2'][index]})
            company_temp.red.update({data_year:data_frame['red'][index]})
            company_temp.constituency.update({data_year:data_frame['constituency'][index]})
            company_temp._merge.update({data_year:data_frame['_merge'][index]})

            for data in data_array:
                if pd.isnull(data):
                    # print(data_year, company_name)
                    company_temp.valid = False
                    break

            companies.update({company_name:company_temp})

    return companies

if __name__ == '__main__':
    excel_file = 'data_origin.xls'
    data_frame = read_excel(excel_file=excel_file, sheet_name='Sheet1')
    companies = set_company(data_frame)
    print(companies['AA'].roa_annual)
