# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong

import main_init
from sqlalchemy import create_engine
import pandas as pd
import pymysql

config = main_init.Init_Config()


class Db_Connection(object):
    def __init__(self):
        self.mqlengine = create_engine(
            f"mysql+pymysql://{config.msqusername}:{config.msqpassword}@{config.msqlserver}/{config.msqdb}",
            encoding=config.msqcoding)

    def obtain_mysql_df(self, sql):
        try:
            df = pd.read_sql(sql, self.mqlengine)
            return df
        except Exception as eromsg:
            print(eromsg)


    def obtain_mysql_count(self, sql):
        try:
            df = pd.read_sql(sql, self.mqlengine)
            return len(df)
        except Exception as eromsg:
            print(eromsg)


    def mysql_to_sql(self, df, table):
        df.to_sql(table, con=self.mqlengine, index=False, if_exists='append')

    def commit_sql(self, sql):
        try:
            conn = pymysql.connect(host=config.msqlserver,
                                   user=config.msqusername,
                                   password=config.msqpassword,
                                   db=config.msqdb,
                                   # charset=config.msqcoding,
                                   )
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as eromsg:
            print(eromsg)
            return False

    def all(self, sql):
        try:
            conn = pymysql.connect(host=config.msqlserver,
                                   user=config.msqusername,
                                   password=config.msqpassword,
                                   db=config.msqdb,
                                   # charset=config.msqcoding,
                                   )
            cursor = conn.cursor()
            cursor.execute(sql)
            result =cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as eromsg:
            print(eromsg)

    def all_chall(self,sql,params):
        try:
            conn = pymysql.connect(host=config.msqlserver,
                                   user=config.msqusername,
                                   password=config.msqpassword,
                                   db=config.msqdb,
                                   # charset=config.msqcoding,
                                   )
            cursor = conn.cursor()
            cursor.execute(sql,params)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except Exception as eromsg:
            print(eromsg)
