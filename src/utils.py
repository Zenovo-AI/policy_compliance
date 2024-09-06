# Utility functions for logging and other tasks.
def log_analysis(log_path: str, content: str) -> None:
    with open(log_path, 'a') as file:
        file.write(content + '\n')