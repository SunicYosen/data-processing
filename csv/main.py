'''
 Main
'''

import os
from parse_args import parse_args
from load_data import load_data
from calculate import calculate
from write_csv import write_csv
from write_sql import write_sql

def main():
    args = parse_args()
    csv_filename = args.data
    result_csv   = args.outfile
    data_dict    = load_data(csv_filename)
    calculate(data_dict)
    write_csv(data_dict, result_csv)
    write_sql(result_csv, args=args)

if __name__ == '__main__':
    main()