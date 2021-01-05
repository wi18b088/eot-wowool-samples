graph_config = {
      "slots" : {
            "Title" : {"expr" : "Reference_Title"},
            #"Document" : {"data" : "ip.id()"} 
            },
       "links" : [
          {     "from"      : { "expr" : "Reference_Title", "label" : "Title"},
                "to"        : { "expr" : "Website", "label" :"Website"},
                "relation"  : { "label" : "Reference_link"}
          },
          {     "from"      : { "expr" : "Reference_Title", "label" : "Title"},
                "to"        : { "expr" : "Year", "label" :"Year"},
                "relation"  : { "label" : "Published_Year"}
          },
          {     "from"      : { "expr" : "Reference_Name", "label" :"Reference_Name","delimiter":"Punct"}, 
                "to"        : { "expr" : "Reference_Title", "label" : "Title"}, 
                "relation"  : { "label" : "AuthorOf" },
                "file"      : True #doesn't seem to do anything???
          }, 
          {     "from"      : { "expr" : "Year", "label" :"Year" },
                "to"        : { "expr" : "Website", "label" :"Website"},
                "relation"  : { "label" : "YearPublished" }
          },
          {     "from"      : { "expr" : "Website", "label" :"Website" }, 
                "to"        : { "expr" : "Reference_Name", "label" :"Reference_Name","delimiter":"Punct"}, 
                "relation"  : { "label" : "AffiliatedTo" }
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
          {     "from"      : { "expr" : "BatteryDens", "label" :"BatteryDens" },
                "to"        : { "expr" : "BatteryDict", "label" :"BatteryDict"},
                "relation"  : { "label" : "Density" }
          },
          {     "from"      : { "expr" : "EnginePower", "label" :"EnginePower" },
                "to"        : { "expr" : "EngineType", "label" :"EngineType"},
                "relation"  : { "label" : "Power" }
          },         
          {     "from"      : { "expr" : "Speed", "label" :"Speed" }, 
                "to"        : { "expr" : "EngineType", "label" :"EngineType"  },
                "relation"  : { "label" : "EngineSpeed" }
          },                              

      ],
      #"global" : { "file" : True , "snippet"   : False , "operator":".." } #seems to work but connects everything to the file and only the file....
}