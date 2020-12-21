"""
Company Class
['year', 'ticker', 'sic_2', 'csp_annual', 'rd_expense', 'ad_intensity_industry', 'sales_annual', 'debt_to_assets', 'red', 'constituency', 'ROA']
"""
#! /usr/bin/env python3

class Company:
    def __init__(self):
        self.name = ''
        self.assets_total = {}
        self.roa_annual = {}
        self.sales_annual = {}
        self.rd_expense	= {}
        self.sic = {}
        self.debt_to_assets = {}
        self.firm_id = {}	
        self.rd_spending = {}	
        self.csp_annual = {}	
        self.ad_intensity_industry = {}	
        self.southafrica_dum = {}	
        self.sic_2 = {}	
        self.patent_num_2 = {}	
        self.cited_num_2 = {}	
        self.red = {}	
        self.constituency = {}	
        self._merge = {}	
        self.ROA = {}
        self.csp = None
        self.innovation = None
        self.differentiation = None
        self.valid = True


    def get_assets_total_cal(self, weight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            assets_total_cal = 0
            for key in weight_dict:
                assets_total_cal = assets_total_cal + self.assets_total[key] * weight_dict[key]

            # assets = self.assets_total[1998]*0.25 \
            #     + self.assets_total[1999]*0.5 \
            #     + self.assets_total[2000]*1.0

        except:
            assets_total_cal = None
            print('[-] {}:{} assets_total_cal ERROR!'.format(self.name, weight_dict))
            self.valid = False

        return assets_total_cal

    def get_sales_annual_cal(self, weight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            sales_annual_cal = 0
            for key in weight_dict:
                sales_annual_cal = sales_annual_cal + self.sales_annual[key] * weight_dict[key]

        except:
            sales_annual_cal = None
            print('[-] {}:{} get_sales_annual_cal ERROR!'.format(self.name, weight_dict))
            self.valid = False

        return sales_annual_cal

    def get_rd_expense_cal(self, weight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            rd_expense_cal = 0
            for key in weight_dict:
                rd_expense_cal += self.rd_expense[key] * weight_dict[key]

        except:
            rd_expense_cal = None
            print('[-] {}:{} rd_expense_cal ERROR!'.format(self.name, weight_dict))
            self.valid = False

        return rd_expense_cal

    def get_debt_to_assets_cal(self, weight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            debt_to_assets_cal = 0
            for key in weight_dict:
                debt_to_assets_cal += self.debt_to_assets[key] * weight_dict[key]
            
        except:
            debt_to_assets_cal = None
            print('[-] {}:{} debt_to_assets_cal ERROR!'.format(self.name, weight_dict))
            self.valid = False


        return debt_to_assets_cal

    def get_csp_annual_cal(self, weight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            csp_annual_cal = 0
            for key in weight_dict:
                csp_annual_cal += self.csp_annual[key] * weight_dict[key]

        except:
            csp_annual_cal = None
            print('[-] {}:{} csp_annual_cal ERROR!'.format(self.name, weight_dict))
            self.valid = False

        return csp_annual_cal

    def get_ad_intensity_industry_cal(self, weight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            ad_intensity_industry_cal = 0

            for key in weight_dict:
                ad_intensity_industry_cal += self.ad_intensity_industry[key] * weight_dict[key]

        except:
            ad_intensity_industry_cal = None
            print('[-] {}:{} ad_intensity_industry_cal ERROR!'.format(self.name, weight_dict))
            self.valid = False

        return ad_intensity_industry_cal

    def get_sic_2_actual(self):
        sic_2_actual = None
        for key in self.sic_2:
            if(self.sic_2[key] != None):
                sic_2_actual = self.sic_2[key]

        self.sic_2_actual = sic_2_actual

    # def get_csp_diff(self):
    #     try:
    #         self.csp_diff =  self.csp * self.differentiation
    #     except:
    #         self.csp_diff = None

    # def get_csp_inno(self):
    #     try:
    #         self.csp_inno = self.csp * self.innovation
    #     except:
    #         self.csp_inno = None

    def set_valid(self, year_array=range(1991,2014)):
        check_array = [
            self.assets_total,
            self.roa_annual,
            self.sales_annual,
            self.rd_expense,
            self.sic,
            self.debt_to_assets,
            self.firm_id,
            self.rd_spending,
            self.csp_annual,
            self.ad_intensity_industry,	
            self.southafrica_dum,
            self.sic_2,	
            self.patent_num_2,
            self.cited_num_2,
            # self.red,	
            # self.constituency,	
            self._merge
        ]

        for year in year_array:
            if self.valid == False:
                break

            for item in check_array:
                if year not in item.keys():
                    self.valid = False
