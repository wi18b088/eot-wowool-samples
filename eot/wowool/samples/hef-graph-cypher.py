#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.tool.entity_graph import EntityGraph
from eot.io import InputProviders
import pathlib


# Check if external configuration exists
# Check for HEFrules.dom in /mnt/inout/config/
# Check for graphconfig.py in /mnt/inout/config/
external_config_file_path = "/mnt/inout/config/"
rule_file_name = "HEFrules.dom"
external_config_file_name = "graphconfig.py"

if pathlib.Path(external_config_file_path + rule_file_name).is_file():
    myrule = Domain(external_config_file_path + rule_file_name)
else:
    myrule = Domain(rule_file_name)

if pathlib.Path( external_config_file_path + external_config_file_name).is_file():
    import importlib.util
    spec = importlib.util.spec_from_file_location("hef-config", external_config_file_path + external_config_file_name)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)

    try:
        graph_config = config_module.graph_config
    except AttributeError:
        from graphconfig import graph_config
else:
    from graphconfig import graph_config

try:
    english = Analyzer(language="english")
    entities = Domain( "english-entity" )

    f = open("cypher-out.cypher", "w")
    webpage = open("index.html", "w")
    for i, ip in enumerate(InputProviders( "../../../docs")):
        print(f"Processing File no {i}: {ip.id()}")
        doc = english(ip)
        doc = entities(doc)
        doc = myrule(doc)
        requested_concepts = set(['EngineType','Battery', 'Flying','Range', 'BatteryDensity', 'EnginePower', 'Manufacturer', 'City', 'Time', 'Price', 'Website','Reference_Title', 'Reference_Name', 'Year', 'Speed', 'Management', 'System'])
        concept_filter = lambda concept : concept.uri in requested_concepts
        for concept in Concept.iter(doc)  :
                # print( f"Tagname: {concept.uri}, literal: {concept.literal:<20}, stem={concept.stem}" )
                # Unpack concept
                print({**concept})
        
        print("-"*10)
        graphit = EntityGraph( graph_config )
        
        from pathlib import Path
        filename = Path(ip.id()).stem
        graphit.slots = {}
        graphit.slots['Document'] = {"data": filename}
        graphit.slots['Title'] = {"expr":"Reference_Title"}
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
            f.write(f"{neo4j_query}\n")

        for neo4j_query in cs(results):
                print(neo4j_query)

        from eot.wowool.tool.entity_graph.d3js_graph import D3JSGraphStream

        webpage.write("<html><body>")
        webpage.write("""<div id="graphid"></div>""")
        out = D3JSGraphStream(webpage, filter = lambda c: c.uri != 'NP' )
        out( None, results, "graphid")
        webpage.write("</body></html>")

    f.close()
    webpage.close()

except Error as ex:
    print("Exception:",ex)
