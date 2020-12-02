#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.tool import EntityGraph

graph_config = {
  "links" : [
          {   "from"      : { "expr" : "flying" },
              "to"        : { "expr" : "Battery"},
              "relation"  : { "label" : "transition" }
          },
        {       "from"      : { "expr" : "EngineType" },
                "to"        : { "expr" : "Range"},
                "relation"  : { "label" : "Efficiency" }
        }         
      ]
}

try:
    english = Analyzer(language="english")
    entities = Domain( "english-entity" )
    # rule = Domain( source = """ rule:{ 'user' '\:' {(<>)+}=USER }; """)
    myrule = Domain("/share/neo4jgithub/eot-wowool-samples/eot/wowool/samples/flyingrules.dom")
    doc = english("New battery technology has emerged. The new technology is called lithium-ion, the abbreviation is li-ion. Lithium has a battery density of 500 Wh/l. This battery type can be used with electric engines, hybrid engines (a combination of ICE engines and electric engines) or with hydrogen engines. Using a lithium battery aircrafts can reach up to 200 km/h or 130 mp/h and have a range of 160 km or 100 miles")
    #doc = english("A plane has a lithium-ion battery inside.")
    doc = entities(doc)
    doc = myrule(doc)
    # print(doc)
    requested_concepts = set(['EngineType','Battery', 'flying'])
    concept_filter = lambda concept : concept.uri in requested_concepts
    for concept in Concept.iter(doc, concept_filter)  :
        # print( f"Tagname: {concept.uri}, literal: {concept.literal:<20}, stem={concept.stem}" )
        # Unpack concept
        print({**concept})
    
    print("-"*10)
    graphit = EntityGraph( graph_config )
    # returns a panda dataframe.
    # graphit.slots['Document'] = {"data":"hello"}
    results = graphit(doc)

    print( results.df_from)
    print("-"*10)
    print( results.df_relation)
    print("-"*10)
    print( results.df_to)
    print("-"*10)

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

