#!/bin/bash

PYTHON_PATH="$HOME/miniconda3/envs/DataScience/bin/python"
notebooks=(./price_indices.ipynb)

for notebook in "${notebooks[@]}"; do
    "$PYTHON_PATH" -m nbconvert --to script "$notebook"
    
    mod_name="${notebook%.ipynb}"
    script_name="$mod_name.py"
    
    "$PYTHON_PATH" -m black "$script_name"
    
    "$PYTHON_PATH" -m mypy "$script_name"
done
