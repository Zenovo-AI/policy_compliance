# Analyzes the extracted text to identify key sections and compliance issues.
import re
from typing import List, Dict

def extract_key_sections(text: str) -> Dict[str, str]:
    # Example regex patterns to identify sections; adjust based on actual policy structure
    patterns = {
        "Coverage": re.compile(r'Coverage[\s\S]*?(?=Exclusions|$)', re.IGNORECASE),
        "Exclusions": re.compile(r'Exclusions[\s\S]*?(?=Limits|$)', re.IGNORECASE),
        "Limits": re.compile(r'Limits[\s\S]*?(?=Coverage|$)', re.IGNORECASE)
    }
    sections = {}
    for key, pattern in patterns.items():
        match = pattern.search(text)
        if match:
            sections[key] = match.group(0).strip()
    return sections

def flag_compliance_issues(sections: Dict[str, str], compliance_rules: Dict[str, str]) -> List[str]:
    issues = []
    for section, rule in compliance_rules.items():
        if section in sections:
            if not re.search(rule, sections[section], re.IGNORECASE):
                issues.append(f"Issue found in section: {section}")
    return issues