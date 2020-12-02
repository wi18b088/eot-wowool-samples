#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
# !!! make sure you build the helloworld.dom
# from the domains folder pywoc -t -l en -o helloworld.dom helloworld.wow --verbose debug
# or using scons
# scons .

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from pathlib import Path

this_folder  = Path(__file__).parent

try:
    dutch = Analyzer(language="dutch")
    helloworld = Domain( Path( this_folder, '..', '..', '..', 'domains' , 'helloworld.dom' ) )

    doc = dutch("greetings world.")
    doc = helloworld(doc)
    print( doc )
except Error as ex:
    print("Exception:",ex)
