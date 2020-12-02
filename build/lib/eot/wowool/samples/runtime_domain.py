#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error

try:
    dutch = Analyzer(language="dutch")
    entities = Domain( "dutch-entity" )

    doc = dutch("Jan Van Den Berg werkte als hoofdarts bij Omega Pharma.")
    doc = entities(doc)

    mydomain = Domain( source = r"""
        rule:{ Person .. <'werken'> .. Company }= PersonWorkCompany@(verb="work");
        rule:{ Person .. Company }= PersonCompany;
    """)
    doc = mydomain(doc)

    # filter some concepts
    requested_concepts = set(['Person','Company','PersonWorkCompany','PersonCompany'])
    concept_filter = lambda concept : concept.uri in requested_concepts
    for concept in Concept.iter(doc, concept_filter) :
        print( f"{concept.uri} -> {concept.literal}"  )

except Error as ex:
    print("Exception:",ex)
