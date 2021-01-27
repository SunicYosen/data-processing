'''
 Load data time_stamp,security_id,value,volume
'''
import os
import pandas as pd
from datetime import datetime
from trade import Trade

def load_data(csv_filename):
    data_dict = {}

    if not os.path.exists(csv_filename):
        print("[-]: CSV file {} doesn't exist!".format(csv_filename))
        return data_dict

    data_frames   = pd.read_csv(csv_filename, parse_dates=True)
    # print(data_frames['time_stamp'])

    for index,time_stamp in enumerate(data_frames['time_stamp']):

        security_id = data_frames['security_id'][index]
        value       = data_frames['value'][index]
        volume      = data_frames['volume'][index]

        trade       = Trade(time_stamp=time_stamp, security_id=security_id, value=value, volume=volume)

        if security_id not in data_dict.keys():
            data_dict.update({security_id:[]})

        data_dict[security_id].append(trade)

    return data_dict

if __name__ == '__main__':
    csv_filename = 'tick_data.csv'
    load_data(csv_filename)