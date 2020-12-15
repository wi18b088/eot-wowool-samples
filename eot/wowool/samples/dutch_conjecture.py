#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.error import Error

try:
    english = Analyzer(language="dutch")
    entities = Domain( "dutch-entity" )

    conjecture = Domain(source="""


namespace conjecture {

    rule :
    {
        'het' { <> }= Info
        'bedrijf'
        {(Prop)+} = Company@(info=f"{rule.Info.stem().upper()}")
    };
}
    """)

    doc = english("Het Vlaams bedrijf NietGekent werkt same met EyeOnText.")
    doc = entities(doc)
    doc = conjecture(doc)
    print(doc)
except Error as ex:
    print("Exception:",ex)


