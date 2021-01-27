'''
    write CSV
'''

import os
import csv

def write_csv(dict_data, out_filename='resule.csv'):
    with open(out_filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time_stamp','security_id','value','volume','moving_avg','signal'])
        for key in dict_data.keys():
            data_array = dict_data[key]
            for data in data_array:
                write_row = [data.time_stamp, data.security_id, data.value, data.volume, data.avg, data.signal]
                writer.writerow(write_row)

    print('[+]: Write Done!')
