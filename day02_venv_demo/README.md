## Setup (conda)

This project also supports a conda-based environment for reproducibility.

### Create the conda environment
From the project root directory, create the environment using the provided `environment.yml` file:

conda env create -f environment.yml

### Activate the environment
Activate the conda environment with:

conda activate day03-conda-env

Your terminal prompt should update to show `(day03-conda-env)`.

### Run the analysis
Once the environment is activated, you can run the analysis script with:

python src/simple_analysis.py

### Deactivate the environment
When you are finished, deactivate the conda environment with:

conda deactivate

### Updating the conda environment
If `environment.yml` is modified in the future, update the environment using:

conda env update -f environment.yml --prune

