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
          {     "from"      : { "expr" : "EngineType" },
                "to"        : { "expr" : "Range"},
                "relation"  : { "label" : "Efficiency" }
          },
          {     "from"      : { "expr" : "BatteryDensity" },
                "to"        : { "expr" : "Range"},
                "relation"  : { "label" : "Efficiency" }
          }, 
          {     "from"      : { "expr" : "EnginePower" },
                "to"        : { "expr" : "Range"},
                "relation"  : { "label" : "Efficiency" }
          },
          {     "from"      : { "expr" : "EngineType" },
                "to"        : { "expr" : "Manufacturer"},
                "relation"  : { "label" : "Invention" }
          }, 
          {     "from"      : { "expr" : "Time" },
                "to"        : { "expr" : "City"},
                "relation"  : { "label" : "FlightTime" }
          },
          {     "from"      : { "expr" : "Price" },
                "to"        : { "expr" : "EngineType"},
                "relation"  : { "label" : "Cost" }
          },
          {     "from"      : { "expr" : "Price" },
                "to"        : { "expr" : "EngineType"},
                "relation"  : { "label" : "Cost" }
          },
          {     "from"      : { "expr" : "Year" },
                "to"        : { "expr" : "Website"},
                "relation"  : { "label" : "YearPublished" }
          },
          #{     "from"      : { "expr" : "Website" },
          #      "to"        : { "expr" : "Person"}, ### Rules we have to make: Grab person from text
          #      "relation"  : { "label" : "AffiliatedTo" }
          #},

      ] #Links we can still create: 
}

try:
    english = Analyzer(language="english")
    entities = Domain( "english-entity" )
    # rule = Domain( source = """ rule:{ 'user' '\:' {(<>)+}=USER }; """)
    myrule = Domain("/share/neo4jgithub/eot-wowool-samples/eot/wowool/samples/flyingrules.dom")
    doc = english("A plane has a lithium-ion battery inside. Hydrogen engine with a range of 200 km.")
    doc = entities(doc)
    doc = myrule(doc)
    # print(doc)
    requested_concepts = set(['EngineType','Battery', 'Flying','Range', 'BatteryDensity', 'EnginePower', 'Manufacturer', 'City', 'Time', 'Price', 'Website'])
    concept_filter = lambda concept : concept.uri in requested_concepts
    for concept in Concept.iter(doc)  :
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

