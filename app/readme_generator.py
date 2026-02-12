from app.tools import format_list

def generate_readme(project_name, info):

    # Feature detection
    features = []

    if info.sub_type:
        features.append(info.sub_type)

    if "Google Gemini" in info.key_libraries:
        features.append("Optional LLM-based content enhancement")

    if info.endpoints:
        features.append("REST API endpoint detection")

    if not features:
        features.append("Modular Python architecture")

    endpoints_text = ""
    if info.endpoints:
        endpoints_text += "## API Endpoints\n"
        for method, path in info.endpoints:
            endpoints_text += f"- `{method} {path}`\n"
        endpoints_text += "\n"

    readme = (
        f"# {project_name}\n\n"
        "## Overview\n"
        f"{info.project_type} – {info.sub_type}\n\n"
        f"{info.purpose}\n\n"
        "## Features\n"
        f"{format_list(features)}\n\n"
        "## Tech Stack\n"
        f"{', '.join(info.key_libraries) or 'Python'}\n\n"
        "## Installation\n"
        "    python -m venv venv\n"
        "    pip install -r requirements.txt\n\n"
        + endpoints_text +
        "## Environment Variables\n"
        f"{format_list(info.env_vars)}\n"
    )

    return readme
