import neo4j
neo4jdb = neo4j.Connector("http://localhost:7474", ("neo4j", "12345")) # local password of neo4j database
with open("cypher-out.cypher") as fh:
   lines = fh.readlines()
for cypher_query in lines:
   print(cypher_query)
   neo4jdb.run(cypher_query)
