import sys
import json
import unittest
from ddt import ddt, file_data, unpack
import requests
import pymysql


@ddt
class InterfaceTest(unittest.TestCase):

    def get_address(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='wang_http',
                               port=3306, charset='utf8')
        cur = conn.cursor()

        select = "SELECT address FROM apimanager_environment where status=1"
        cur.execute(select)
        # 现在获取所有数据
        all_data = cur.fetchone()
        address = "".join(tuple(all_data))
        cur.close()
        conn.close()
        return address

    @unpack
    @file_data("test_data_list.json")
    def test_run_cases(self, url, method, header, parameter_type, parameter_body, assert_type, assert_text):

        if header == "{}":
            header_dict = {}
        else:
            header_dict = json.loads(header.replace("\'", "\""))

        if parameter_body == "{}":
            parameter_dict = {}
        else:
            parameter_dict = json.loads(parameter_body.replace("\'", "\""))

        if method == "get":
            if parameter_type == "form":
                r = requests.get(self.get_address() + url, headers=header_dict, params=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)

        if method == "post":
            if parameter_type == "form":
                r = requests.post(self.get_address() + url, headers=header_dict, data=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)

            elif parameter_type == "json":
                r = requests.post(self.get_address() + url, headers=header_dict, json=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)
            else:
                raise NameError("参数类型错误")


if __name__ == "__main__":
    unittest.main()
