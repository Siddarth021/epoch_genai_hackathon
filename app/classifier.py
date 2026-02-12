from app.models import ProjectInfo

def classify_project(data):

    packages = set(data["packages"])

    project_type = "Software Project"
    sub_type = ""
    key_libs = []

    # Web frameworks
    if "fastapi" in packages:
        project_type = "FastAPI Backend"
        key_libs.append("FastAPI")

    elif "flask" in packages:
        project_type = "Flask Web Application"
        key_libs.append("Flask")

    # AI detection
    if "langchain" in packages:
        sub_type = "AI Agent API"
        key_libs.append("LangChain")

    if "google" in packages:
        key_libs.append("Google Gemini")

    if "openai" in packages:
        key_libs.append("OpenAI")

    # CLI detection
    if not data["endpoints"]:
        project_type = "CLI Tool"

    # Smarter purpose detection
    if "os" in packages and "ast" in packages:
        sub_type = "AI-powered README Generator"
        purpose = (
            "Hybrid README generation tool combining static code analysis "
            "and optional LLM enhancement."
        )
    elif data["endpoints"]:
        purpose = "REST API providing programmatic endpoints."
    else:
        purpose = "Application built using detected frameworks."

    return ProjectInfo(
        project_type=project_type,
        sub_type=sub_type,
        purpose=purpose,
        key_libraries=key_libs,
        total_files=data["total_files"],
        endpoints=data["endpoints"],
        env_vars=data["env_vars"]
    )
