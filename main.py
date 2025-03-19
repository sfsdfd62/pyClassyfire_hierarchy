#Please install the pyclassyfire first
from client import *
#structure_query("C/C(=CC=CC=C(C=CC=C(C=CC1=C(C)C(=O)[C@H](CC1(C)C)O)/C)/C)/C=C/C=C(/C=C/C1=C(C)C(=O)[C@H](CC1(C)C)O)C", 'csv')
#This is a example InChIKey for test
test_cpd = get_entity("MQZIGYBFDRPAKN-UWFIBFSHSA-N", 'json')

import json

def print_taxonomy_hierarchy(json_string):
    # Parse the JSON string into a dictionary
    taxonomy_json = json.loads(json_string)
    
    # Sort keys to ensure the order makes sense (kingdom → superclass → class, etc.)
    ordered_keys = [
        "kingdom", "superclass", "class", "subclass", 
        "intermediate_nodes", "molecular_framework", "direct_parent"
    ]
    
    # Collect valid keys in order
    valid_keys = [key for key in ordered_keys if key in taxonomy_json]
    
    # Print the hierarchy
    for idx, key in enumerate(valid_keys):
        if isinstance(taxonomy_json[key], dict) and "name" in taxonomy_json[key]:
            print("  " * idx + "└── " + taxonomy_json[key]["name"])
        elif isinstance(taxonomy_json[key], list):  # Handle intermediate_nodes
            for node in taxonomy_json[key]:
                if "name" in node:
                    print("  " * idx + "└── " + node["name"])


print_taxonomy_hierarchy(test_cpd)

'''
Output looks like this
└── Organic compounds
  └── Lipids and lipid-like molecules
    └── Prenol lipids
      └── Tetraterpenoids
        └── Carotenoids
            └── Xanthophylls
'''
