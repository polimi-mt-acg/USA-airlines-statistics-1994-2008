#!/bin/bash

set -e

ROOT=`git rev-parse --show-toplevel`

echo "==> Fetching dataset..."
$ROOT/script/get_dataset.sh

echo "==> Creating conda environment..."
conda env create -f environment.yml

echo "==> Installing iPyWidgets Jupyter Lab extension"
source activate bd-mt-project
jupyter labextension install @jupyter-widgets/jupyterlab-manager

echo "==> Installing Matplotlib Jupyter extension"
jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib

source deactivate