## Open powershell

    wsl -—list -—online
## see available software version and choose the one you like:
    
    wsl -—install -b <ubuntu-ver>

## Restart unix shell

    Ubu -> TAB
## Execute linux image

## Download Miniconda3 from https://docs.anaconda.com/miniconda/, Miniconda3 Linux 64-bit

   source Miniconda3-latest-Linux-x86_64.sh

## sometimes it helps to restart your computer to activate all the installations

## Two options:
Create environment from yml file
WARNING: change yml file last line to match your miniconda3 path!!!

    conda env create -f environment.yml

## Go to your created conda environment:

conda activate <ENV_NAME>

## If it doesn’t work - Create conda environment from scratch

    conda create env —name <ENV_NAME>
 
##  Go to your created conda environment

    conda activate <ENV_NAME>

##  Install packages

conda install python
Conda install -c conda-forge numpy
Conda install -c conda-forge pandas
Conda install -c conda-forge root
Conda install -c conda-forge matplotlib
Conda install -c conda-forge scipy

## Install ipykernel
    conda install ipykernel
    python -m ipykernel install --user --name= ENVIRONMENT_NAME
