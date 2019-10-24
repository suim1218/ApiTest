import json
import unittest
from ddt import ddt, file_data, unpack
import requests
import pymysql
import os
#连接数据库
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_PATH = BASE_DIR.replace("\\", "/")
Report = BASE_PATH + "/ApiManager/reports/"
filename = Report +  'result.html'
print(filename)