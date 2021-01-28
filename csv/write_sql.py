'''
 write SQL
'''

import mysql.connector
# import pandas as pd

def write_sql(result_csv, args=None):

    mydb = mysql.connector.connect(
      host=args.mysql_host,
      user=args.mysql_user,
      password=args.mysql_passwd,
      database=args.mysql_database
    )

    mycursor = mydb.cursor()

    new_table_script = "CREATE TABLE {} (time_stamp VARCHAR(255), \
                                          security_id VARCHAR(255),\
                                          value FLOAT, \
                                          volume INT, \
                                          sma FLOAT, \
                                          signal FLOAT);".format(args.mysql_table)

    mycursor.execute(new_table_script)

    load_csv_script = "load data local infile {} \
                       replace into table sma IGNORE {} LINES \
                       fields terminated by ',' lines terminated by '\n';".format(result_csv, 1)

    mycursor.execute(load_csv_script)

    mydb.commit()

    # data = pd.read_csv(result_csv)

    # for i in data.values():
    #     j = tuple(i)
    #     sql = """INSERT INTO sma ({})""".format(j)
    #     mycursor.execute(sql)
    #     mydb.commit()