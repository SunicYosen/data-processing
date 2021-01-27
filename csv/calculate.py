'''
 calculate avg
'''
from datetime import datetime
from trade import Trade

def calculate(dict_data):
    for key in dict_data.keys():
        print(key)
        data_array = dict_data[key]

        pre_data = Trade()
        for index, data in enumerate(data_array):
            if data.time_stamp == pre_data.time_stamp:
                data.avg    = pre_data.avg
                data.signal = data.value - data.avg

                continue
            
            total_value  = 0.0
            total_number = 0
            for j in range(index, len(data_array)):
                if (datetime.strptime(str(data_array[j].time_stamp),"%Y-%m-%d %H:%M:%S") - datetime.strptime(str(data.time_stamp),"%Y-%m-%d %H:%M:%S")).seconds > 900:
                    break

                total_value  += data_array[j].value
                total_number += 1

            data.avg = total_value / total_number
            data.signal = data.value - data.avg

            pre_data.time_stamp = data.time_stamp
            pre_data.avg        = data.avg
            pre_data.security_id= data.security_id
            pre_data.volume     = data.volume
            pre_data.value      = data.value
            pre_data.signal     = data.signal
