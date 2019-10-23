import sys
import json
import unittest
from ddt import ddt, file_data, unpack
import requests


@ddt
class InterfaceTest(unittest.TestCase):

    # def get_environment_url(self):
    #     environment_all = Environment.objects.all()
    #     for environment in environment_all:
    #         if environment.status == 1:
    #             return environment.address
    #         else:
    #             pass

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
                r = requests.get('http://localhost:8001/' + url, headers=header_dict, params=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)

        if method == "post":
            if parameter_type == "from":
                r = requests.post('http://localhost:8001/' + url, headers=header_dict, data=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)

            elif parameter_type == "json":
                r = requests.post('http://localhost:8001/' + url, headers=header_dict, json=parameter_dict)
                if assert_type == "contains":
                    self.assertIn(assert_text, r.text)
                else:
                    self.assertEqual(assert_text, r.text)
            else:
                raise NameError("参数类型错误")


if __name__ == "__main__":
    unittest.main()
