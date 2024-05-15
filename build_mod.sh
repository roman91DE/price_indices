#!/bin/bash

PYTHON_PATH="$HOME/miniconda3/envs/DataScience/bin/python"
notebooks=(./price_indices.ipynb)

# Path to the custom nbconvert configuration file
NB_CONVERT_CONFIG="nbconvert_conf.py"

for notebook in "${notebooks[@]}"; do
    # Use the custom nbconvert configuration file
    "$PYTHON_PATH" -m nbconvert --to script --config "$NB_CONVERT_CONFIG" "$notebook"
    
    # Remove the .ipynb extension to get the base name
    mod_name="${notebook%.ipynb}"
    script_name="$mod_name.py"
    
    # Format the script with Black
    "$PYTHON_PATH" -m black "$script_name"
    
    # Check types with mypy
    "$PYTHON_PATH" -m mypy "$script_name"
done
