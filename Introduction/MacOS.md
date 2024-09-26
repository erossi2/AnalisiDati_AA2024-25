## 1) Python3 & matplotlib

Richiede macOS 11.0 o versioni successive e un Mac con chip Apple M1 o versioni successive.
Con le versioni di macOS recenti, python3 è automaticamente installato. 
Per vedere la versione di python usare i comandi python3 --version o python --version:

<img width="352" alt="image" src="https://github.com/user-attachments/assets/84b75873-ed4c-488d-99f3-0286dedc22af">

Aggiungere matplotlib:

        python3 -m pip install matplotlib

Aggiungere vector (utile per qualche esercizio proposto):

        python3 -m venv path/to/venv
        source path/to/venv/bin/activate
        python3 -m pip install vector

## 2) pip/conda

2.1) Install pip:
1) Open Terminal from Applications > Utilities. 
2) Type: python -m ensurepip or python3 -m ensurepip
3) Press Return.
4) If pip isn’t already installed, Ensurepip will install it.
5) If you want to upgrade pip instead of installing it from scratch, add upgrade to the end of the command in step 2.
    
    python3 -m ensurepip

2.2) Install Anaconda: 
1)    go on the site: https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html
2) select https://www.anaconda.com/download/ to dowload Anaconda, register and you'll get a link by email:
   <img width="366" alt="image" src="https://github.com/user-attachments/assets/201ab284-0b61-4540-8778-25b5045415a1">
   
3) Create an account
   
    <img width="355" alt="image" src="https://github.com/user-attachments/assets/28b11169-01d3-4aae-8202-2f59145cf7b7">
    
    <img width="342" alt="image" src="https://github.com/user-attachments/assets/29b7e256-7004-4794-8daa-0136213c77e8">
    
5) Install the downloaded file by double-clicking the .pkg file.
   
    <img width="308" alt="image" src="https://github.com/user-attachments/assets/99c972c1-b5dd-475d-ae0f-929db052d4fd">
    
6) To verify your installation, in your terminal window, run the command conda list. A list of installed packages appears if it has been installed correctly:
   
   conda list

##  3) Installing git
   (Already installed in macOS check with)

    git --version

##  4) jupyter
   To launch it, from the terminal (recommended) do:
    
    jupyter-notebook
    
It should start in the basic browser, otherwise copy the link to the local server that generates notebooks to a browser of your choice.

You can also run Anaconda navigator from the command line:

    anaconda navigator

Once launched, the Jupyter icon should appear on the front page, you can click on the icon and install or update it.

##  5) Root

    **RECOMMENDED FOR JUPYTER** If you have conda installed follow the procedure here:
    
    https://root.cern/install/#conda

    For any Linux distribution and MacOS, ROOT is available as a conda package. To create a new conda environment containing ROOT and activate it, execute

    conda config --set channel_priority strict
    conda create -c conda-forge --name <my-environment> root
    conda activate <my-environment>

    Please note: conda here will create a new environment for root to function in, this is the way it is suggested to do it. The default environment is "base". 
    If you want to run ROOT you will always have to
    
        conda activate <my-environment>
    
    To leave the environment:

        conda deactivate

    Follow the instructions found here:

    https://root.cern/install

## 6) Scipy
Install Scipy:

    conda install scipy

Or using brew:

    brew install scipy

## 7) matplotlib   
Install matplotlib:

    conda install -c conda-forge matplotlib    
