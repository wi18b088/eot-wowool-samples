#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.error import Error

try:
    english = Analyzer(language="english")
    entities = Domain( "english-entity" )
    mydomain = Domain( source=""" rule:{ Person .. City }= PersonCity; """)

    doc = mydomain(entities(english("John Smith was in London on the 3/11/2020.")))
    for sentence in doc:
        print(f"S:({sentence.begin_offset},{sentence.end_offset})")
        for a in sentence:
            if a.is_token:
                print(f"  T:({a.begin_offset},{a.end_offset}): {a.literal}, {a.stem}, {a.pos}, {a.properties}")
            elif a.is_concept:
                print(f"""C:[{a.begin_offset},{a.end_offset}]: {a.uri}, attributes={a.attributes}, literal="{a.literal}" """)


except Error as ex:
    print("Exception:",ex)
