import neo4j
import os
# print(os.listdir())
neo4jdb = neo4j.Connector("http://localhost:7474", ("neo4j", "12345")) # local password of neo4j database
# neo4jdb = neo4j.Connector("http://192.168.122.61:7474", ("neo4j", "12345")) # local password of neo4j database
with open("cypher-out.cypher", "r") as fh:
#with open("eot/wowool/samples/cypher-out.cypher", "r") as fh:
   lines = fh.readlines()
for i, cypher_query in enumerate(lines):
   print(i, cypher_query)
   neo4jdb.run(cypher_query)
