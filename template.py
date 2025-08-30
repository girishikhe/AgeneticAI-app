import os
from pathlib import Path

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/langgraph/__init__.py",
    f"{project_name}/langgraph/graph/__init__.py",
    f"{project_name}/langgraph/LLMS/__init__.py",
    f"{project_name}/langgraph/nodes/__init__.py",
    f"{project_name}/langgraph/state/__init__.py",
    f"{project_name}/langgraph/tools/__init__.py",
    f"{project_name}/langgraph/ui/__init__.py",
    f"{project_name}/langgraph/ui/uiconfigfile.py",
    f"{project_name}/langgraph/ui/uiconfigfile.ini",
    f"{project_name}/langgraph/ui/streamlitui/__init__.py",   
    f"{project_name}/langgraph/ui/streamlitui/display_result.py",
    f"{project_name}/langgraph/ui/streamlitui/loadui.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")