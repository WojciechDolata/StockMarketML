import numpy as np

class CompanyStock(object):
    def __init__(self, index, name, url, description):
        self.index = index
        self.name = name
        self.url = url
        self.description = description

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def get_url(self):
        return self.url

    def get_description(self):
        return self.description

