# Compares policies based on extracted sections.
from typing import Dict

def compare_policies(policy1_sections: Dict[str, str], policy2_sections: Dict[str, str]) -> Dict[str, str]:
    differences = {}
    for section in policy1_sections:
        if section in policy2_sections:
            if policy1_sections[section] != policy2_sections[section]:
                differences[section] = (policy1_sections[section], policy2_sections[section])
    return differences