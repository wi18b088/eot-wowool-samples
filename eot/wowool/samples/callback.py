#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer
from eot.wowool.native import Domain
from eot.wowool.annotation import Concept

a = Analyzer(language="english")
dc = Domain("english-company")
doc = dc(a("this is a EyeOnText."))

call_plugin = Domain(
    source="""
rule:{ Company }= ::python::myplugin::call_this;
rule:{ Company }= Other@(name=f"{rule.literal()}" );

"""
)

doc = call_plugin(doc)
concepts = [c for c in Concept.iter(doc)]
uris = [c.uri for c in concepts]
print(doc)

assert "PLUGIN_COMPANY" in uris, "Missing some plugin annotation"
assert "Company" in uris, "Missing some plugin annotation"
assert concepts[1].attributes["name"][0] == "EyeOnText", "Missing attributes."
