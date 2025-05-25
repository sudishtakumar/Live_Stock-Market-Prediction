"""

Script to generate a single import file (Import_Functions.py) that aggregates
function imports from individual .py files inside the 'split_functions' directory.

Each file is assumed to define a function with the same name as the filename.

The output file includes:
- A docstring at the top explaining the purpose
- Individual import statements
- A summary comment with total number of imported functions
"""

import os

# === CONFIGURATION ===

# For Local
# FUNCTION_DIR = "feature_functions_local"
# IMPORT_FILE = "Import_Functions_Local.py"

# For Deployment
FUNCTION_DIR = "feature_functions_deployed"
IMPORT_FILE = "Import_Functions_Deployed.py"

# List all Python files in the function directory
function_files = [f for f in os.listdir(FUNCTION_DIR) if f.endswith(".py")]
total_imports = len(function_files)

# === GENERATE THE IMPORT FILE ===
with open(IMPORT_FILE, "w", encoding="utf-8") as f:
    # Write top-level docstring to the output file
    f.write('"""\n')
    f.write(
        f"This file was auto-generated to import all functions from '{FUNCTION_DIR}/'.\n"
    )
    f.write(
        f"Each function file is expected to define a function named after the filename.\n"
    )
    f.write(f"Total functions imported: {total_imports}\n")
    f.write('"""\n\n')

    f.write("# === FUNCTION IMPORTS ===\n")

    # Write each import statement
    for filename in function_files:
        module_name = filename[:-3]  # Remove .py extension
        f.write(f"from {FUNCTION_DIR}.{module_name} import {module_name}\n")

    # Footer summary comment
    f.write(f"\n# ✅ Total functions imported: {total_imports}\n")

print(
    f"✅ '{IMPORT_FILE}' created with {total_imports} function imports from '{FUNCTION_DIR}/'"
)
