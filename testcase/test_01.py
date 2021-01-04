# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong
from url_api.bidding import Oalogin
from models.db_con import Db_Connection
import unittest
import time
from random import randrange


mysql_db=Db_Connection()




class Mycount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   #类的前置，执行这个类一开始要执行的东西
        pass
    @classmethod
    def tearDownClass(self): #类的后置，执行完整个类之后，要执行的东西
        pass

    def setUp(self):  #用例的前置，执行每条用例前要执行的东西
        pass
    def tearDown(self):  #用例的后置，执行每条用例后要执行的东西
        pass


