'''
 Trade
'''

class Trade:
    def __init__(self, time_stamp  = '', security_id = '', value       = '', volume      = ''):
        self.time_stamp  = time_stamp
        self.security_id = security_id
        self.value       = value
        self.volume      = volume
        self.avg         = ''
        self.signal      = ''