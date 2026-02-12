import os

IGNORE = {"venv", "__pycache__", "node_modules", ".git"}

def scan_project(root_path):
    structure = {}

    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        rel = os.path.relpath(root, root_path)
        structure[rel] = files

    return structure
