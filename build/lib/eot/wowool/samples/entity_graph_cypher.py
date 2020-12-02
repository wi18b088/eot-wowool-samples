#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.tool import EntityGraph

graph_config = {
  "slots" : { "USER" : { "expr":"USER" } },
  "links" : [
          {   "from"      : { "expr" : "Person"  , "attributes" : ["gender"]  },
              "to"        : { "expr" : "Company" , "attributes" : ["country"] } ,
              "relation"  : { "label": "P2C" }
          }
          ,
          {   "from"      : { "expr" : "Person" },
              "to"        : { "expr" : "Company"},
              "relation"  : { "expr" : "Position" , "label" :"stem" }
          }
          ,
          {   "from"      : { "slot" : "USER" ,  "label": "USER"},
              "to"        : { "expr" : "Person"},
              "relation"  : { "label": "Mentions"  }
          },
          {   "from"      : { "expr" : "USER" },
              "to"        : { "slot" : "Document", "label": "Document"} ,
              "relation"  : { "label": "Mentions"  }
          }
      ]
}

try:
    english = Analyzer(language="dutch")
    entities = Domain( "dutch-entity" )
    myrule = Domain( source = """ rule:{ 'user' '\:' {(<>)+}=USER }; """)
    doc = english("user:John \n\nJan Van Den Berg werkte als hoofdarts bij Omega Pharma.")
    doc = entities(doc)
    doc = myrule(doc)
    print(doc)
    graphit = EntityGraph( graph_config )
    # returns a panda dataframe.
    graphit.slots['Document'] = {"data":"hello"}
    results = graphit(doc)

    print( results.df_from)
    print( results.df_relation)
    print( results.df_to)

    from eot.wowool.tool.entity_graph.cypher import CypherStream
    cs = CypherStream("EOT")
    for neo4j_query in cs(results):
        print(neo4j_query)

    from eot.wowool.tool.entity_graph.d3js_graph import D3JSGraphStream

    with open( "index.html", "w" ) as fh:
        fh.write("<html><body>")
        fh.write("""<div id="graphid"></div>""")
        out = D3JSGraphStream(fh, filter = lambda c: c.uri != 'NP' )
        out( None, results, "graphid")
        fh.write("</body></html>")

except Error as ex:
   print("Exception:",ex)

