## Sample program - [link](https://bridgesuncc.github.io/tutorials/testing/python/tut_sllist_p1.py.html)
from dotenv import dotenv_values
config = dotenv_values("../../.env")    ## load as dictionary

name = config['bridges_username']
bridges_key = config['bridges_api']

from bridges.bridges import *
from bridges.sl_element import *
import sys

def main():
    bridges = Bridges(1, name, bridges_key)
    bridges.set_title('A Singly Linked List Example')
    bridges.set_description('A singly linked list of 4 nodes')
    
    st0 = SLelement(e="GG")
    st1 = SLelement(e="Lamont Kyler")
    st2 = SLelement(e="Gladys Serino")
    st3 = SLelement(e="Karol Soderman")
    st4 = SLelement(e="Starr McGinn")

    # link the elements
    st0.next = st1
    st1.next = st2
    st2.next = st3
    st3.next = st4

    # we want to see these names in the visualization so we will 
    #set them as the nodes' labels. We will retrieve the nodes' 
    #generic data for the label
    st0.label = st0.value
    st1.label = st1.value
    st2.label = st2.value
    st3.label = st3.value
    st4.label = st4.value

    # tell Bridges the head of the list
    bridges.set_data_structure(st0)

    # visualize
    bridges.visualize()


if __name__ == "__main__":
    main()
