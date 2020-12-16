"""
Company Class
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


    def get_assets(self, wight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            assets = 0
            for key in wight_dict:
                assets = assets + self.assets_total[key] * wight_dict[key]

            # assets = self.assets_total[1998]*0.25 \
            #     + self.assets_total[1999]*0.5 \
            #     + self.assets_total[2000]*1.0
        except:
            assets = None

        self.assets = assets

    def get_sales(self, wight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            sales = 0
            for key in wight_dict:
                sales = sales + self.sales_annual[key] * wight_dict[key]

        except:
            sales = None

        self.sales = sales

    def get_innovation(self, wight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            innovation = 0
            for key in wight_dict:
                innovation += self.rd_expense[key] * wight_dict[key]

        except:
            innovation = None

        self.innovation = innovation

    def get_risk(self, wight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            risk = 0
            for key in wight_dict:
                risk += self.debt_to_assets[key] * wight_dict[key]
            
        except:
            risk = None

        self.risk = risk

    def get_csp(self, wight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            csp = 0
            for key in wight_dict:
                csp += self.csp_annual[key] * wight_dict[key]

        except:
            csp = None

        self.csp = csp

    def get_differentiation(self, wight_dict={1998:0.25, 1999:0.5, 2000:1.0}):
        try:
            differentiation = 0

            for key in wight_dict:
                differentiation += self.ad_intensity_industry[key] * wight_dict[key]

        except:
            differentiation = None

        self.differentiation = differentiation

    def get_sic_2_actual(self):
        sic_2_actual = None
        for key in self.sic_2:
            if(self.sic_2[key] != None):
                sic_2_actual = self.sic_2[key]

        self.sic_2_actual = sic_2_actual

    def get_csp_diff(self):
        try:
            self.csp_diff =  self.csp * self.differentiation
        except:
            self.csp_diff = None

    def get_csp_inno(self):
        try:
            self.csp_inno = self.csp * self.innovation
        except:
            self.csp_inno = None
