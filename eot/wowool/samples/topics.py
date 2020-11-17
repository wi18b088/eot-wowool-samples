#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.
#  requirements.txt
#
from eot.wowool.native import Analyzer, Domain
from eot.wowool.annotation import Concept
from eot.wowool.error import Error
from eot.wowool.topic_identifier import TopicIdentifier

try:

    model = TopicIdentifier(language="english", topic_model="english.topic_model")
    topics = model.get_topics("I saw black cars and a green bird and green house.", 5)
    print(topics)

except Error as ex:
    print("Exception:",ex)
