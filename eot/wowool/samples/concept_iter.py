#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error

try:
    english = Analyzer(language="dutch")
    entities = Domain( "dutch-entity" )

    doc = english("Jan Van Den Berg werkte als hoofdarts bij Omega Pharma.")
    doc = entities(doc)

    # filter some concepts
    requested_concepts = set(['Person','Position','Company'])
    concept_filter = lambda concept : concept.uri in requested_concepts
    for concept in Concept.iter(doc, concept_filter)  :
        print( f"literal: {concept.literal:<20}, stem={concept.stem}" )
    # flatten concepts into dict
    print( '-' * 40 )
    for concept in Concept.iter(doc, concept_filter) :
        print( { **concept } )

except Error as ex:
    print("Exception:",ex)
