#  Copyright (c) 2020 EyeOnText, All Rights Reserved.
#  NOTICE:  All information contained herein is, and remains the property of EyeOnText.

from eot.wowool.native import Analyzer, Domain
from eot.wowool.error import Error
from eot.wowool.annotation import Concept
from eot.wowool.annotation import Token

try:
    analyzer = Analyzer(language="dutch")
    rule_source ="""
// Compound Sample:
// capture all the word with verzekering
lexicon:(input="component"){
    verzekering } = INSURANCE_COMP;

// capture only the real verzekering not verzekeringsmaatschapijen
lexicon:(input="head"){
    verzekering } = INSURANCE_HEAD;

// capture the cost of the insurance.
rule:{ h'verzekering' { <+currency> } = INSURANCE_PRICE };
    """
    compounds = Domain(source=rule_source)
    input = "Er zijn verzekeringsmaatschapijen €40.000.000 en verzekeringen: autoverzekeringen €100, fietsverzekering €10"
    doc = compounds(analyzer(input))
    print("-" * 80)
    print(rule_source)
    print("-" * 80)
    print(input)
    print("-" * 80)
    print(f"{'uri':<20s} | {'literal':<30s} | {'stem'}")
    print("-" * 80)
    for concept in Concept.iter(doc, lambda concept : concept.uri.startswith("INSURANCE") ):
        print(f"{concept.uri:<20s} | {concept.literal:<30s} | {concept.stem}")
except Error as ex:
    print("Exception:",ex)


