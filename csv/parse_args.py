import argparse
import collections
import backtrader as bt

MAINSIGNALS = {
    'longshort': bt.SIGNAL_LONGSHORT,
    'longonly' : bt.SIGNAL_LONG,
    'shortonly': bt.SIGNAL_SHORT,
}


EXITSIGNALS = {
    'longexit': bt.SIGNAL_LONGEXIT,
    'shortexit': bt.SIGNAL_LONGEXIT,
}


def parse_args():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Sample for Signal concepts')

    parser.add_argument('--data', required=False,
                        default='simple.csv',
                        help='Specific data to be read in')

    parser.add_argument('--outfile', required=False,
                        default='result.csv',
                        help='Result File Path')

    # parser.add_argument('--fromdate', required=False, default=None,
    #                     help='Starting date in YYYY-MM-DD format')

    # parser.add_argument('--todate', required=False, default=None,
    #                     help='Ending date in YYYY-MM-DD format')

    # parser.add_argument('--cash', required=False, action='store',
    #                     type=float, default=50000,
    #                     help=('Cash to start with'))

    # parser.add_argument('--smaperiod', required=False, action='store',
    #                     type=int, default=30,
    #                     help=('Period for the moving average'))

    # parser.add_argument('--exitperiod', required=False, action='store',
    #                     type=int, default=5,
    #                     help=('Period for the exit control SMA'))

    # parser.add_argument('--signal', required=False, action='store',
    #                     default='longshort', choices=MAINSIGNALS,
    #                     help=('Signal type to use for the main signal'))

    # parser.add_argument('--exitsignal', required=False, action='store',
    #                     default=None, choices=EXITSIGNALS,
    #                     help=('Signal type to use for the exit signal'))

    # MYSQL options
    parser.add_argument('--mysql_host', required=False,
                        default='localhost',
                        help='Mysql Host')

    parser.add_argument('--mysql_user', required=False,
                        default='test',
                        help='Mysql User Name')

    parser.add_argument('--mysql_passwd', required=False,
                        default='12345678',
                        help='Mysql Password')

    parser.add_argument('--mysql_database', required=False,
                        default='test',
                        help='Mysql Database Name')

    parser.add_argument('--mysql_table', required=False,
                        default='sma',
                        help='Mysql Table Name')

    # Plot options
    # parser.add_argument('--plot', '-p', nargs='?', required=False,
    #                     metavar='kwargs', const=True,
    #                     help=('Plot the read data applying any kwargs passed\n'
    #                           '\n'
    #                           'For example:\n'
    #                           '\n'
    #                           '  --plot style="candle" (to plot candles)\n'))

    return parser.parse_args()
