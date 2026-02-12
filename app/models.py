from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class ProjectInfo:
    project_type: str
    sub_type: str
    purpose: str
    key_libraries: List[str]
    total_files: int
    endpoints: List[Tuple[str, str]]
    env_vars: List[str]
