# Epoch Hackathon – README Generator

## Overview

This project is a command-line tool that analyzes a software project and generates a structured `README.md` file automatically.

The tool scans the project directory, inspects Python files using static analysis, detects imports and framework usage, and builds a clear README based on the discovered information. If a Google API key is provided, the generated content can optionally be refined using Gemini. The tool works fully offline without requiring any API access.

---

## Features

- Recursive project structure scanning  
- Python import detection using AST  
- FastAPI / Flask endpoint detection  
- Environment variable detection  
- Automatic project type classification  
- Structured README generation  
- Versioned output folder (previous results are preserved)  

---

## Project Structure

app/
├── main.py
├── agents.py
├── analyzer.py
├── classifier.py
├── readme_generator.py
├── llm_enhancer.py
├── file_scanner.py
├── config.py
├── models.py
└── tools.py


The system is organized in a modular way:

- `file_scanner.py` handles directory traversal  
- `analyzer.py` performs static code analysis  
- `classifier.py` determines project type  
- `readme_generator.py` builds the README content  
- `llm_enhancer.py` optionally improves clarity  
- `agents.py` coordinates the full pipeline  

---

## Installation

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt