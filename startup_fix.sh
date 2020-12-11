#!/bin/bash

#####################################################################################################################
# This will fix the regex in /usr/local/lib/python3.8/dist-packages/eot/wowool/tool/entity_graph/entity_graph.py    #
# on line 312                                                                                                       #
#####################################################################################################################

# run with
# /share/neo4jgithub/eot-wowool-samples/startup_fix.sh
# after starting the container

sed -i 's/link_index = re\.match("\.\*_(\[0-9\])+", uri)\.group(1)/link_index = re\.match("\.\*_(\[0-9\]+)", uri)\.group(1)/' /usr/local/lib/python3.8/dist-packages/eot/wowool/tool/entity_graph/entity_graph.py
echo "[A-Z]([a-z]){0,5}\." >> /usr/local/lib/python3.8/dist-packages/eot/wowool/package/lxware/english.abbrev
echo "startup script was executed."
