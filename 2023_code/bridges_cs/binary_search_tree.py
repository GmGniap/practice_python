from dotenv import dotenv_values
config = dotenv_values("../../.env")    ## load as dictionary

name = config['bridges_username']
bridges_key = config['bridges_api']

from bridges.bridges import *
from bridges.bst_element import *
import sys

def main():
    bridges = Bridges(2, name, bridges_key)