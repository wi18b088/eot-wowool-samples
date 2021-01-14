#!/usr/bin/env python3
import neo4j
import os
import pathlib

cypher_file_name = "cypher-out.cypher"
cypher_path = "/mnt/inout/output/hef-graph-cypher/"
neo4jdb = neo4j.Connector("http://localhost:7474", ("neo4j", "12345"))

if pathlib.Path(cypher_path + cypher_file_name).is_file():
    cypherfile = cypher_path + cypher_file_name
else:
   print("no cypher output found. Using demo file.")
   cypherfile = cypher_file_name

with open(cypherfile, "r") as fh:
   lines = fh.readlines()
for i, cypher_query in enumerate(lines):
   print(i, cypher_query)
   neo4jdb.run(cypher_query)

print("Creating Cypher finished. You can now visit localhost:7474/browser/ in your webbrowser and look at the neo4j database.")