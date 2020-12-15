#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.io import InputProviders

try:

    for ip in InputProviders( "/Users/phforest/corpus/english/bloomberg"):
        print(ip.id(), ip.text())

except Error as ex:
    print("Exception:",ex)
