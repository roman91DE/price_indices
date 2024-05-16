#!/bin/bash

PYTHON_PATH=$(which python)

CUR_DIR=$(pwd)

cd "./price_indices" || exit

notebooks=(./price_indices.ipynb)

# Path to the custom nbconvert configuration file
NB_CONVERT_CONFIG="./nbconvert_conf.py"

for notebook in "${notebooks[@]}"; do
    # Use the custom nbconvert configuration file
    echo -e "Converting Notebook File $notebook\n---"
    "$PYTHON_PATH" -m nbconvert --to script --config "$NB_CONVERT_CONFIG" "$notebook"
    
    # Remove the .ipynb extension to get the base name
    mod_name="${notebook%.ipynb}"
    script_name="$mod_name.py"
    
    # Format the script with Black
    echo -e "Starting Auto Formatting\n---"
    "$PYTHON_PATH" -m black "$script_name"
    
    # Check types with mypy
    echo -e "Starting static Type Checks\n---"
    "$PYTHON_PATH" -m mypy "$script_name"

    # run the tests
    echo -e "Starting Unit Tests\n---"
    "$PYTHON_PATH" ../tests/test_price_indices.py

done

cd "$CUR_DIR" || exit
echo -e "Building Sphinx Documentation\n---"
make html
ln -s build/html docs

git add * ; git commit -m "Executed CI Script" ; git push
