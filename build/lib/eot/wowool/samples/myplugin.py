# do not call this directly,
# this code will be triggerd when a rule with ::python::myplugin::call_this
# will be called
from eot.wowool.plugin import wowool_plugin

def call_this(ud):
    mi = wowool_plugin.match_info()
    capture = mi.capture()
    print("Capture:", capture)
    capture.add_concept("PLUGIN_COMPANY")
