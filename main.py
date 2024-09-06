# Main script to run the analysis.
import os
from src.data_preprocessing import load_text, preprocess_text
from src.policy_analysis import extract_key_sections, flag_compliance_issues
from src.policy_comparison import compare_policies
from src.utils import log_analysis

def main():
    policy_files = ["data/sample_policies/policy1.txt", "data/sample_policies/policy2.txt"]
    compliance_rules = {
        "Coverage": r"Minimum coverage amount of \$10000",
        "Exclusions": r"Pre-existing conditions are excluded",
        "Limits": r"Annual limit of \$50000"
    }

    policies = [load_text(file) for file in policy_files]
    sections = [extract_key_sections(text) for text in policies]

    issues = flag_compliance_issues(sections[0], compliance_rules)
    differences = compare_policies(sections[0], sections[1])

    log_analysis("data/logs/analysis_log.txt", f"Issues: {issues}")
    log_analysis("data/logs/analysis_log.txt", f"Differences: {differences}")

    print(f"Issues: {issues}")
    print(f"Differences: {differences}")

if __name__ == "__main__":
    main()