#!/bin/bash

echo "Setting conda init..."
CONDA_PATH=$(conda info | grep -i 'base environment' | cut -d ":" -f2 | cut -d " " -f2)
source $CONDA_PATH/etc/profile.d/conda.sh

echo "Setting environment..."
conda env create -f environment.yml

echo "Activating environment..."
conda activate env_opics_common

echo "Upgrading pip..."
# upgrading pip - https://stackoverflow.com/questions/61365790/error-could-not-build-wheels-for-scipy-which-use-pep-517-and-cannot-be-installe
python -m pip install pip --upgrade

echo "Updating poetry config..."
# disabling poetry's experimental new installer - https://github.com/python-poetry/poetry/issues/4210#issuecomment-877778420
python -m poetry config experimental.new-installer false

echo "Installing dependencies using poetry..."
python -m poetry install

echo "installing gdown without caching"
python -m pip install -U --no-cache-dir gdown --pre
