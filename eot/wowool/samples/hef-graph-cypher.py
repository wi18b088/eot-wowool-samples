#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.tool import EntityGraph
from eot.io import InputProviders

graph_config = {
  "links" : [
          {   "from"      : { "expr" : "Flying", "label" :"Flying" },
              "to"        : { "expr" : "Battery", "label" :"Battery"},
              "relation"  : { "label" : "transition"}
          },
          {     "from"      : { "expr" : "EngineType" , "label" :"EngineType"},
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" }
          },
          {     "from"      : { "expr" : "BatteryDensity", "label" :"BatteryDensity" },
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" }
          }, 
          {     "from"      : { "expr" : "EnginePower" , "label" :"EnginePower"},
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" }
          },
          {     "from"      : { "expr" : "EngineType", "label" :"EngineType" },
                "to"        : { "expr" : "Manufacturer", "label" :"Manufacturer"},
                "relation"  : { "label" : "Invention" }
          }, 
          {     "from"      : { "expr" : "Time", "label" :"Time" },
                "to"        : { "expr" : "City", "label" :"City"},
                "relation"  : { "label" : "FlightTime" }
          },
          {     "from"      : { "expr" : "Price", "label" :"Price" },
                "to"        : { "expr" : "EngineType", "label" :"EngineType"},
                "relation"  : { "label" : "Cost" }
          },
          {     "from"      : { "expr" : "Price", "label" :"Price" },
                "to"        : { "expr" : "BatteryDict", "label" :"BatteryDict"},
                "relation"  : { "label" : "Cost" }
          },
          {     "from"      : { "expr" : "Year", "label" :"Year" },
                "to"        : { "expr" : "Website", "label" :"Website"},
                "relation"  : { "label" : "YearPublished" }
          },
          {     "from"      : { "expr" : "BatteryDens", "label" :"BatteryDens" },
                "to"        : { "expr" : "BatteryDict", "label" :"BatteryDict"},
                "relation"  : { "label" : "Density" }
          },
          {     "from"      : { "expr" : "EnginePower", "label" :"EnginePower" },
                "to"        : { "expr" : "EngineType", "label" :"EngineType"},
                "relation"  : { "label" : "Power" }
          },
          {     "from"      : { "expr" : "Reference_Name", "label" :"Reference_Name" }, 
                "to"        : { "expr" : "Reference_Title", "label" :"Reference_Title"  }, 
                "relation"  : { "label" : "AuthorOf" }
          }, 
          {     "from"      : { "expr" : "Website", "label" :"Website" }, 
                "to"        : { "expr" : "Reference_Name", "label" :"Reference_Name" }, 
                "relation"  : { "label" : "AffiliatedTo" }
          },                 
          {     "from"      : { "expr" : "Website", "label" :"Website" }, 
                "to"        : { "expr" : "Reference_Title", "label" :"Reference_Title"  }, 
                "relation"  : { "label" : "Source" }
          },                 
          {     "from"      : { "expr" : "Year", "label" :"Year" }, 
                "to"        : { "expr" : "Reference_Title", "label" :"Reference_Title"  },
                "relation"  : { "label" : "PublishYear" }
          },
          {     "from"      : { "expr" : "Speed", "label" :"Speed" }, 
                "to"        : { "expr" : "EngineType", "label" :"EngineType"  },
                "relation"  : { "label" : "PublishYear" }
          },  
         #{     "from"      : { "expr" : "Flying", "label" :"Flying" }, 
         #       "to"        : { "expr" : "Article_Title", "label" :"Article_Title"  },
         #       "relation"  : { "label" : "Found_in" }
         # },
         #{     "from"      : { "expr" : "BatteryDict", "label" :"Battery" }, 
         #       "to"        : { "expr" : "Article_Title", "label" :"Article_Title"  },
         #       "relation"  : { "label" : "Found_in" }
         #},
         #{     "from"      : { "expr" : "Manufacturer", "label" :"Manufacturer" }, 
         #      "to"        : { "expr" : "Article_Title", "label" :"Article_Title"  },
         #      "relation"  : { "label" : "Found_in" }
         #},
         #{     "from"      : { "expr" : "City", "label" :"City" }, 
         #      "to"        : { "expr" : "Article_Title", "label" :"Article_Title"  },
         #      "relation"  : { "label" : "Found_in" }
         #}, 
         #{     "from"      : { "expr" : "City", "label" :"City" }, 
         #      "to"        : { "expr" : "Article_Title", "label" :"Article_Title"  },
         #      "relation"  : { "label" : "Found_in" }
         #},                               

      ] #Links we can still create: We still have to get the author's of the article it self as well as the title of the article to link those together. 
}

try:
    english = Analyzer(language="english")
    entities = Domain( "english-entity" )
    # rule = Domain( source = """ rule:{ 'user' '\:' {(<>)+}=USER }; """)
    myrule = Domain("/share/neo4jgithub/eot-wowool-samples/eot/wowool/samples/HEFrules.dom")

    inputText = ""
    for i, ip in enumerate(InputProviders( "/share/neo4jgithub/eot-wowool-samples/docs")):
        inputText = f"{inputText}\n{ip.text()}"
 

    doc = english(inputText)
    doc = entities(doc)
    doc = myrule(doc)
    # print(doc)
    requested_concepts = set(['EngineType','Battery', 'Flying','Range', 'BatteryDensity', 'EnginePower', 'Manufacturer', 'City', 'Time', 'Price', 'Website','Reference_Title', 'Reference_Name', 'Year', 'BatteryDict', 'Speed'])
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

    with open("cypher-out.cypher", "w") as f:
        for neo4j_query in cs(results):
            f.write(f"{neo4j_query}\n")

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

