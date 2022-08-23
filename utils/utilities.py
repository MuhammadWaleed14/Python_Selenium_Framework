import os
import json
import pytest


class Utilities:
    """This class will be used to have helper methods like reading json, getting project paths"""

    def get_testdata_path(self):
        """This method will return the project path"""
        return pytest.project_root+os.path.dirname(r"\testdata\'")

    def get_test_data(self, file_name):
        """Returns json test testdata as dictionary"""
        test_data_path = self.get_testdata_path() + "/" + file_name
        return self.read_from_json(test_data_path)

    def read_from_json(self, file_name):
        """This method reads the given Json file and return a dictionary"""
        with open(file_name) as file:
            products_data = json.load(file)
        return products_data

    def read_config(self, str_key):
        """reads config file and returns the value for the given key"""
        data = self.read_from_json(pytest.project_root+"/config.json")
        return data[str_key]




