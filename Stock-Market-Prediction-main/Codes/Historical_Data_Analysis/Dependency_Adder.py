"""

Script to analyze individual Python function files inside the 'split_functions' directory
and prepend necessary import statements based on used modules, functions, or objects.

The goal is to ensure each function file is self-contained by including all relevant
imports at the top. This script uses a heuristic approach, looking for known identifiers
to determine which modules are needed.
"""

import os
import ast
from pathlib import Path

# === CONFIGURATION ===

# Path to the folder containing the split function files(Local)
# functions_folder = Path("feature_functions_local")

# Path to the folder containing the split function files (Deployed)
functions_folder = Path("feature_functions_deployed")

# Mapping of commonly used identifiers to their respective import statements
# Includes one-line comments categorized for clarity and maintainability

import_suggestions = {
    # --- STREAMLIT APP & VISUALIZATION FRAMEWORK ---
    "st": "# Importing Streamlit for building the web-based interactive application framework\nimport streamlit as st",
    "plt": "# Importing Matplotlib for generating static plots and charts\nimport matplotlib.pyplot as plt",
    "go": "# Importing Plotly for creating interactive and dynamic visual plots\nimport plotly.graph_objects as go",
    "sns": "# Importing Seaborn for enhanced data visualizations\nimport seaborn as sns",
    # --- DATA HANDLING & MANIPULATION ---
    "pd": "# Importing Pandas for data manipulation and analysis\nimport pandas as pd",
    "np": "# Importing NumPy for numerical computations and array operations\nimport numpy as np",
    "os": "# Importing OS module for handling file and directory paths\nimport os",
    "datetime": "# Importing datetime for working with timestamps and date ranges\nfrom datetime import datetime, timedelta",
    "base64": "# Importing base64 for encoding and decoding binary data\nimport base64",
    # --- MACHINE LEARNING & MODELING ---
    "pickle": "# Importing Pickle for loading/saving pre-trained machine learning models\nimport pickle",
    "LinearRegression": "# Linear Regression model\nfrom sklearn.linear_model import LinearRegression",
    "RandomForestRegressor": "# Random Forest Regressor\nfrom sklearn.ensemble import RandomForestRegressor",
    "SVR": "# Support Vector Machine Regressor\nfrom sklearn.svm import SVR",
    "mean_squared_error": "# Importing evaluation metrics from Scikit-learn\nfrom sklearn.metrics import mean_squared_error, r2_score, precision_score, recall_score, f1_score",
    "MinMaxScaler": "# For scaling data to a 0–1 range\nfrom sklearn.preprocessing import MinMaxScaler",
    "TfidfVectorizer": "# Text feature extraction\nfrom sklearn.feature_extraction.text import TfidfVectorizer",
    # --- DEEP LEARNING (PyTorch) ---
    "torch": "# Importing PyTorch for building and training deep learning models\nimport torch",
    "nn": "# Importing PyTorch's neural network module\nimport torch.nn as nn",
    # --- NATURAL LANGUAGE PROCESSING (NLP) ---
    "TextBlob": "# Importing TextBlob for basic natural language processing tasks\nfrom textblob import TextBlob",
    # --- FINANCIAL DATA & UTILITIES ---
    "yf": "# Importing yfinance for fetching historical stock data from Yahoo Finance\nimport yfinance as yf",
    "webbrowser": "# Importing webbrowser module to open URLs in the default browser\nimport webbrowser",
    "openpyxl": "# Importing openpyxl to enable writing Excel files (.xlsx)\nimport openpyxl",
}


def get_required_imports(source_code):
    """
    Analyze source code of a function to detect required imports
    based on the presence of known identifiers.
    """
    tree = ast.parse(source_code)
    imports = set()

    for node in ast.walk(tree):
        # Detect simple names like 'pd', 'st', etc.
        if isinstance(node, ast.Name):
            if node.id in import_suggestions:
                imports.add(import_suggestions[node.id])
        # Detect attribute access like 'plt.plot'
        elif isinstance(node, ast.Attribute):
            value_id = getattr(node.value, "id", None)
            if value_id in import_suggestions:
                imports.add(import_suggestions[value_id])

    return sorted(imports)


# === MAIN PROCESS ===

changed_files_count = 0  # Counter for changed files
changed_lines_count = 0  # Counter for changed lines

# Iterate through each Python file in the target folder
for filepath in functions_folder.glob("*.py"):
    with open(filepath, "r", encoding="utf-8") as file:
        original_code = file.read()

    # Determine needed imports based on code analysis
    needed_imports = get_required_imports(original_code)

    # Combine imports and original content
    updated_code = "\n".join(needed_imports) + "\n\n" + original_code

    # Only write back to the file if changes were made
    if updated_code != original_code:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(updated_code)

        # Count the changes
        changed_files_count += 1
        changed_lines_count += updated_code.count("\n")

# Output results
print(
    f"✅ Done! {changed_files_count} file(s) updated. {changed_lines_count} lines changed."
)
