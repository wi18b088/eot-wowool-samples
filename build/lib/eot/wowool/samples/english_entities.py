#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.error import Error

try:
    english = Analyzer(language="english")
    entities = Domain( "english-entity" )

    doc = english("John Smith was in London on the 3/11/2020.")
    doc = entities(doc)

    print(doc)
except Error as ex:
    print("Exception:",ex)
