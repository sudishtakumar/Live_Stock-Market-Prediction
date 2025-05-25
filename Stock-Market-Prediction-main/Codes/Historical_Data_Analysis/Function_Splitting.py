"""

Script to split top-level functions (excluding 'main') from a large Streamlit app file
into separate Python files, preserving:
- Any comment immediately above the function
- Any global variable used within the function

Each function is saved as a standalone `.py` file inside the `split_functions/` directory.
"""

import ast
import os
import astunparse

# === CONFIGURATION ===
INPUT_FILE = "Streamlit_app_local_combined.py"  # The source Python file to extract functions from

# For Local Running functions
# OUTPUT_DIR = "feature_functions_local"  # Directory to store individual function files

# For Deployed Functions
OUTPUT_DIR = (
    "feature_functions_deployed"  # Directory to store individual function files
)

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read the entire source file content
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    source = f.read()

# Parse the source code into an abstract syntax tree (AST)
tree = ast.parse(source)
lines = source.splitlines()

# Containers to hold relevant nodes
function_nodes = []  # Functions to extract
global_vars = []  # Global variables (assignments) at top level
import_lines = []  # All top-level import statements

# Classify top-level elements in the AST
for node in tree.body:
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        import_lines.append(node)  # Collect import lines
    elif isinstance(node, ast.Assign):
        global_vars.append(node)  # Track top-level assignments
    elif isinstance(node, ast.FunctionDef) and node.name != "main":
        function_nodes.append(node)  # Collect functions except 'main'


# Extract comment immediately above a function, if present
def get_leading_comment(node):
    lineno = node.lineno - 2
    while lineno >= 0 and lines[lineno].strip().startswith("#"):
        return lines[lineno].strip()
    return ""


# Get all variable names used in a function
def get_used_names(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


# Prepare a mapping of global variable name -> source code
all_globals = {
    t.targets[0].id: astunparse.unparse(t).strip()
    for t in global_vars
    if isinstance(t.targets[0], ast.Name)
}

# Create a separate file for each function
for func_node in function_nodes:
    func_name = func_node.name
    func_code = ast.get_source_segment(
        source, func_node
    )  # Full source code of the function
    used_names = get_used_names(func_node)  # Variables used in the function

    leading_comment = get_leading_comment(
        func_node
    )  # Optional comment above the function
    globals_needed = [all_globals[name] for name in used_names if name in all_globals]

    file_path = os.path.join(OUTPUT_DIR, f"{func_name}.py")

    with open(file_path, "w", encoding="utf-8") as out_file:
        if leading_comment:
            out_file.write(leading_comment + "\n")  # Write leading comment if present
        for g in globals_needed:
            out_file.write(g + "\n")  # Write any required globals
        out_file.write("\n" + func_code + "\n")  # Finally, write the function code

print(f"✅ Done! Functions split into {OUTPUT_DIR}")
