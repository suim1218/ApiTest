import time, sys
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append('./ApiManager/tasks')

# 指定测试用例为当前文件夹下的 views 目录
BASE_PATH = BASE_DIR.replace("\\", "/")
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_task.py')

Report = BASE_PATH + "/templates/"

if __name__ == "__main__":
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = Report + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='接口测试报告',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
