"""


Script to clean a Streamlit app by removing all top-level functions except 'main'.
Also removes unused import statements.
Preserves:
- All used import statements
- Global variables
- Top-level code (outside functions)
- The 'main' function (if present)

Saves the result as 'app_cleaned.py'.
"""

import ast
import black

# For Deployed
INPUT_FILE = "Streamlit_app_combined.py"
CLEANED_FILE = "Streamlit_app.py"

# Read source
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    source = f.read()

lines = source.splitlines()
tree = ast.parse(source)

# Step 1: Remove non-main top-level functions and their header comments
lines_to_remove = set()
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name != "main":
        comment_line = node.lineno - 2
        if 0 <= comment_line < len(lines):
            lines_to_remove.add(comment_line)
        for i in range(node.lineno - 1, node.end_lineno):
            lines_to_remove.add(i)

cleaned_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]
cleaned_code = "".join(line + "\n" for line in cleaned_lines)


# Step 2: Parse cleaned code to remove unused imports
class ImportUsageAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = {}
        self.used_names = set()

    def visit_Import(self, node):
        for alias in node.names:
            self.imports[alias.asname or alias.name] = node.lineno

    def visit_ImportFrom(self, node):
        for alias in node.names:
            name = alias.asname or alias.name
            self.imports[name] = node.lineno

    def visit_Name(self, node):
        self.used_names.add(node.id)


# Analyze the cleaned code
tree = ast.parse(cleaned_code)
analyzer = ImportUsageAnalyzer()
analyzer.visit(tree)

# Identify unused imports
unused_import_lines = set()
for name, lineno in analyzer.imports.items():
    if name not in analyzer.used_names:
        unused_import_lines.add(lineno - 1)  # Convert to 0-based

# Final clean-up: remove unused imports
final_lines = [
    line
    for i, line in enumerate(cleaned_code.splitlines())
    if i not in unused_import_lines
]
final_code = "".join(line + "\n" for line in final_lines)
formatted_code = black.format_str(final_code, mode=black.FileMode())

# Write the cleaned, formatted file
with open(CLEANED_FILE, "w", encoding="utf-8") as f:
    f.write(formatted_code)

print(
    f"✅ Cleaned and formatted file saved as '{CLEANED_FILE}' "
    "(only 'main' retained, unused imports and comments removed)."
)
