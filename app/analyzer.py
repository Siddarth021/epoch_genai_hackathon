import os
import ast
import re

def analyze_project(root_path, structure):
    packages = set()
    endpoints = []
    env_vars = set()
    total_files = 0

    env_pattern = re.compile(r"os\.getenv\(['\"](.*?)['\"]")

    for rel, files in structure.items():
        for file in files:
            total_files += 1
            full = os.path.join(root_path, rel, file)

            if file.endswith(".py"):
                try:
                    with open(full, "r", encoding="utf-8") as f:
                        content = f.read()

                    # ENV detection
                    env_vars.update(env_pattern.findall(content))

                    tree = ast.parse(content)

                    for node in ast.walk(tree):

                        # Import detection
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                packages.add(alias.name.split(".")[0])

                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                packages.add(node.module.split(".")[0])

                        # Endpoint detection (FastAPI / Flask)
                        elif isinstance(node, ast.FunctionDef):
                            for deco in node.decorator_list:
                                if hasattr(deco, "func") and hasattr(deco.func, "attr"):
                                    method = deco.func.attr.lower()
                                    if method in ["get", "post", "put", "delete"]:
                                        endpoints.append((method.upper(), "/"))

                except:
                    continue

    return {
        "packages": list(packages),
        "endpoints": endpoints,
        "env_vars": list(env_vars),
        "total_files": total_files
    }
