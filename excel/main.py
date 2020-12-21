"""
Main
"""

from company import Company
from read_excel import read_excel
from set_company import set_company
from write_excel import write_excel

def main():
    excel_file  = 'data_origin.xls'
    result_file = 'result.xlsx'

    data_frame  = read_excel(excel_file=excel_file, sheet_name='Sheet1')
    companies   = set_company(data_frame)
    write_excel(companies, file_name=result_file)


if __name__ == '__main__':
    main()

