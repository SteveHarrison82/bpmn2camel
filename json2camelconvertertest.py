from camel_dsl import extract_elements_from_json
import os
import unittest


class BPMNJson2CamelConvertertest(unittest.TestCase):
    def test_readjson(self):
        ju = extract_elements_from_json.JsonUtil()
        ju.find_camel_elements()


if __name__ == '__main__':
    unittest.main()
