'''
 Main
'''
import os
import pandas as pd
from datetime import datetime
from trade import Trade
from load_data import load_data
from calculate import calculate
from write_csv import write_csv

def main():
    csv_filename = 'tick_data.csv'
    out_csv      = 'resule.csv'
    data_dict = load_data(csv_filename)
    calculate(data_dict)
    write_csv(data_dict, out_csv)

if __name__ == '__main__':
    main()