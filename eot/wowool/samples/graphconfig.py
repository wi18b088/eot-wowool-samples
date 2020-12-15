graph_config = {
      "slots" : {
            "Title" : {"expr" : "Reference_Title"}
            },
       "links" : [
          {     "from"      : { "slot" : "Title"},
                "to"        : { "expr" : "Website"},
                "relation"  : { "label" : "Reference"}
          },
          {     "from"      : { "slot" : "Title"},
                "to"        : { "expr" : "Year"},
                "relation"  : { "label" : "Published_Year"}
          },
          {     "from"      : { "expr" : "Flying", "label" :"Flying" },
                "to"        : { "expr" : "Battery", "label" :"Battery"},
                "relation"  : { "label" : "transition"}
          },
          {     "from"      : { "expr" : "EngineType" , "label" :"EngineType"},
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" }
          },
          {     "from"      : { "expr" : "BatteryDensity", "label" :"BatteryDensity" },
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" }
          }, 
          {     "from"      : { "expr" : "EnginePower" , "label" :"EnginePower"},
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" }
          },
          {     "from"      : { "expr" : "EngineType", "label" :"EngineType" },
                "to"        : { "expr" : "Manufacturer", "label" :"Manufacturer"},
                "relation"  : { "label" : "Invention" }
          }, 
          {     "from"      : { "expr" : "Time", "label" :"Time" },
                "to"        : { "expr" : "City", "label" :"City"},
                "relation"  : { "label" : "FlightTime" }
          },
          {     "from"      : { "expr" : "Price", "label" :"Price" },
                "to"        : { "expr" : "EngineType", "label" :"EngineType"},
                "relation"  : { "label" : "Cost" }
          },
          {     "from"      : { "expr" : "Price", "label" :"Price" },
                "to"        : { "expr" : "BatteryDict", "label" :"BatteryDict"},
                "relation"  : { "label" : "Cost" }
          },
          {     "from"      : { "expr" : "Year", "label" :"Year" },
                "to"        : { "expr" : "Website", "label" :"Website"},
                "relation"  : { "label" : "YearPublished" }
          },
          {     "from"      : { "expr" : "BatteryDens", "label" :"BatteryDens" },
                "to"        : { "expr" : "BatteryDict", "label" :"BatteryDict"},
                "relation"  : { "label" : "Density" }
          },
          {     "from"      : { "expr" : "EnginePower", "label" :"EnginePower" },
                "to"        : { "expr" : "EngineType", "label" :"EngineType"},
                "relation"  : { "label" : "Power" }
          },
          {     "from"      : { "expr" : "Reference_Name", "label" :"Reference_Name" }, 
                "to"        : { "expr" : "Reference_Title", "label" :"Reference_Title"  }, 
                "relation"  : { "label" : "AuthorOf" }
          }, 
          {     "from"      : { "expr" : "Website", "label" :"Website" }, 
                "to"        : { "expr" : "Reference_Name", "label" :"Reference_Name" }, 
                "relation"  : { "label" : "AffiliatedTo" }
          },                 
          {     "from"      : { "expr" : "Website", "label" :"Website" }, 
                "to"        : { "expr" : "Reference_Title", "label" :"Reference_Title"  }, 
                "relation"  : { "label" : "Source" }
          },                 
          {     "from"      : { "expr" : "Year", "label" :"Year" }, 
                "to"        : { "expr" : "Reference_Title", "label" :"Reference_Title"  },
                "relation"  : { "label" : "PublishYear" }
          },
          {     "from"      : { "expr" : "Speed", "label" :"Speed" }, 
                "to"        : { "expr" : "EngineType", "label" :"EngineType"  },
                "relation"  : { "label" : "EngineSpeed" }
          },                              

      ],
       "global" : { "file" : True , "snippet"   : False , "operator":".." }
}