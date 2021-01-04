# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong


import configparser
import os,sys
import logging

def read_config():
    """
    读取配置
    :return: 返回配置对象
    """
    config = configparser.ConfigParser()  # 类实例化
    ini_path = os.getcwd() + '\\config.ini'
    config.read(ini_path)
    config.add_section('mysqldb')
    config.set('mysqldb','msqlserver','192.168.4.131')
    config.set('mysqldb', 'msqdb', 'app.exam')
    config.set('mysqldb', 'msqusername', 'root')
    config.set('mysqldb', 'msqpassword', '123456!@#')
    config.set('mysqldb', 'msqcoding', 'utf8')
    return config

class Init_Config(object):
    """
    初始化配置
    """
    def __init__(self):
        sys.path.append(os.getcwd())
        config = read_config()
        self.msqlserver = config['mysqldb']['msqlserver']
        self.msqdb = config['mysqldb']['msqdb']
        self.msqusername = config['mysqldb']['msqusername']
        self.msqpassword = config['mysqldb']['msqpassword']
        self.msqcoding = config['mysqldb']['msqcoding']
