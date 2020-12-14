import numpy as np

def get_indexes():
    if(is_logged):
        return indexes
    return []

def get_login_status():
    return is_logged

def login(name, password):
    is_logged = True
    return None

is_logged = False
indexes = ['TSLA', 'F']