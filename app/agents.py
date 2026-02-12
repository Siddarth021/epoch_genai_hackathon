import os
from app.file_scanner import scan_project
from app.analyzer import analyze_project
from app.classifier import classify_project
from app.readme_generator import generate_readme
from app.llm_enhancer import enhance_with_llm

def run_readme_agent(path):

    structure = scan_project(path)
    analysis = analyze_project(path, structure)
    info = classify_project(analysis)

    readme = generate_readme(os.path.basename(path), info)
    readme = enhance_with_llm(readme)

    return readme