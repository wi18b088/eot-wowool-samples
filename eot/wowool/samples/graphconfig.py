graph_config = {
      "slots" : {
            "Title" : {"expr" : "Reference_Title"}
            },
       "links" : [
          {     "from"      : { "slot" : "Title", "label" : "Title"},
                "to"        : { "expr" : "Website", "label" :"Website"},
                "relation"  : { "label" : "Reference_link"},
                "file"      : True
          },
          {     "from"      : { "slot" : "Title", "label" : "Title"},
                "to"        : { "expr" : "Year", "label" :"Year"},
                "relation"  : { "label" : "Published_Year"},
                "file"      : True
          },
          {     "from"      : { "expr" : "Reference_Name", "label" :"Reference_Name","delimiter":"'\,''\&'" }, 
                "to"        : { "slot" : "Title", "label" : "Title"}, 
                "relation"  : { "label" : "AuthorOf" },
                "file"      : True
          }, 
          {     "from"      : { "expr" : "Year", "label" :"Year" },
                "to"        : { "expr" : "Website", "label" :"Website"},
                "relation"  : { "label" : "YearPublished" },
                "file"      : True
          },
          {     "from"      : { "expr" : "Website", "label" :"Website" }, 
                "to"        : { "expr" : "Reference_Name", "label" :"Reference_Name","delimiter":"'\,'" }, 
                "relation"  : { "label" : "AffiliatedTo" },
                "file"      : True
          },    
          {     "from"      : { "expr" : "Flying", "label" :"Flying" },
                "to"        : { "expr" : "Battery", "label" :"Battery"},
                "relation"  : { "label" : "transition"},
                "file"      : True
          },
          {     "from"      : { "expr" : "EngineType" , "label" :"EngineType"},
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" },
                "file"      : True
          },
          {     "from"      : { "expr" : "BatteryDensity", "label" :"BatteryDensity" },
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" },
                "file"      : True
          }, 
          {     "from"      : { "expr" : "EnginePower" , "label" :"EnginePower"},
                "to"        : { "expr" : "Range", "label" :"Range"},
                "relation"  : { "label" : "Efficiency" },
                "file"      : True
          },
          {     "from"      : { "expr" : "EngineType", "label" :"EngineType" },
                "to"        : { "expr" : "Manufacturer", "label" :"Manufacturer"},
                "relation"  : { "label" : "Invention" },
                "file"      : True
          }, 
          {     "from"      : { "expr" : "Time", "label" :"Time" },
                "to"        : { "expr" : "City", "label" :"City"},
                "relation"  : { "label" : "FlightTime" },
                "file"      : True
          },
          {     "from"      : { "expr" : "Price", "label" :"Price" },
                "to"        : { "expr" : "EngineType", "label" :"EngineType"},
                "relation"  : { "label" : "Cost" },
                "file"      : True
          },
          {     "from"      : { "expr" : "Price", "label" :"Price" },
                "to"        : { "expr" : "BatteryDict", "label" :"BatteryDict"},
                "relation"  : { "label" : "Cost" },
                "file"      : True
          },
          {     "from"      : { "expr" : "BatteryDens", "label" :"BatteryDens" },
                "to"        : { "expr" : "BatteryDict", "label" :"BatteryDict"},
                "relation"  : { "label" : "Density" },
                "file"      : True
          },
          {     "from"      : { "expr" : "EnginePower", "label" :"EnginePower" },
                "to"        : { "expr" : "EngineType", "label" :"EngineType"},
                "relation"  : { "label" : "Power" },
                "file"      : True
          },         
          {     "from"      : { "expr" : "Speed", "label" :"Speed" }, 
                "to"        : { "expr" : "EngineType", "label" :"EngineType"  },
                "relation"  : { "label" : "EngineSpeed" },
                "file"      : True
          },                              

      ],
      "global" : { "file" : True , "snippet"   : False , "operator":".." }
}