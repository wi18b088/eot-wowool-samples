#!/bin/bash

#####################################################################################################################
# This will fix the regex in /usr/local/lib/python3.8/dist-packages/eot/wowool/tool/entity_graph/entity_graph.py    #
# on line 312                                                                                                       #
#####################################################################################################################

sed -i 's/link_index = re\.match("\.\*_(\[0-9\])+", uri)\.group(1)/link_index = re\.match("\.\*_(\[0-9\]+)", uri)\.group(1)/' /usr/local/lib/python3.8/dist-packages/eot/wowool/tool/entity_graph/entity_graph.py
