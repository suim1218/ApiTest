import json
import unittest
from ddt import ddt, file_data, unpack
import requests


@ddt
class InterfaceTest(unittest.TestCase):

    @file_data("test_data_list.json")
    @unpack
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


if __name__ == "__main__":
    unittest.main()
