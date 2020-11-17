#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.error import Error

try:
    english = Analyzer(language="dutch")
    entities = Domain( "dutch-entity" )

    # scope is the range of sentence, in this case 3 before until the current sentence.
    # concept id the type of annotation we are looking for.
    # required means that we must have that attribute. in this case 'hij' must be male.
    # you can also add relevancy if you have seen a attribute, ex: relevancy="_ana:referent:6.1"
    #   this means that if we have a candidate with a attribute _ana="referent" we add more relevancy.
    anaphora = Domain( source = """
    namespace entity {
         rule:{ Person } = Person;
    }

    namespace anaphora {
        rule: { <'hij'>} =
            wow::anaphora@( concept="Person" , scope="-3:0" , inherit="true", required="gender:male" );
    }

""")

    doc = english("Jan Van Den Berg werkte als hoofdarts samen met Pol Jannsens bij Omega Pharma. Hij is ook de CEO.")
    doc = entities(doc)
    doc = anaphora(doc)
    print(doc)
except Error as ex:
    print("Exception:",ex)
