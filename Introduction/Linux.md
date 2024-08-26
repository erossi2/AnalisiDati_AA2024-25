## Linux è il sistema operativo su cui è consigliato iniziare. Esistono diverse distribuzioni possibili:

* Red Hat Enterprise è utilizzato in genere lato aziendale.
* Scientific Linux è usato al Cern, è una versione di Red Hat sponsorizzata dal Fermilab. E' stabile e lunga vita media, oltre alla disponibilità di librerie.
* Ubuntu è la più user friendly, facile da scaricare e usare, per cui ha una community piuttosto vasta. Non è ottimale, specie con le librerie grafiche.

Le istruzioni saranno per ubuntu.

## 1) Installazione sistema operativo - esempio con Ubuntu

Si parte dall'istallazione di un file immagine (*iso*) qui:

    https://www.ubuntu-it.org/download

Il suggerimento è di scegliere una distribuzione Long Term Support (LTS) piuttosto che una di sviluppo (senza LTS nel nome).

Per installarlo ci sono due modi:

1.1) Far partire una iso da uno strumento esterno (e.g. una penna usb) e realizzare una partizione. Consigliato se sapete quello che state facendo e volete impiegare parte del vostro spazio sul pc in maniera permanente.

Istruzioni:

    Scaricare la iso dal sito su una penna. 
    Ubuntu può essere pesante, ordine 3 GB, quindi occhio alla connessione.

    Riavviare il computer, e, nel bios settare il boot di modo che dia priorità alla penna. 
    Il modo di aprire il bios varia da macchina a macchina, tipicamente consiste nel premere 
    un pulsante durante il caricamento di Windows (ad es. F2). Questo di solito compare tra le scritte durante l'avvio.

    ⚠️⚠️⚠️WARNING!!! Se avete Windows come altro sistema operativo e installate linux su una partizione, può capitare che un update Windows 10 --> Windows 11 o simili vi causi una formattazione dell'area di Ubuntu!!!⚠️⚠️⚠️

1.2) Realizzare una macchina virtuale e installare il sistema operativo lì. Questo in genere ha difficoltà e rischi piuttosto bassi, quindi consigliato a meno che non vogliate lavorare su linux per la maggior parte del vostro tempo.

Istruzioni:

    Scaricare virtualbox da qui: https://www.virtualbox.org/wiki/Downloads 
    per la piattaforma ospite (ad es. Windows).
    
    Una volta avviato, creare una nuova macchina tramite file -> nuova macchina, 
    con settings Linux , Ubuntu-32 (64 a seconda dell'architettura), e nome macchina riconoscibile.
    
    Aperta la macchina, avviarla e caricare il file iso scaricato in precedenza. 
    Partirà l'installazione e il sistema operativo di conseguenza.

Suggerimenti:
    
    - Assicuratevi di avere almeno 20 GB di spazio per la partizione (reale o virtuale),
    in quanto il sistema operativo ne userà almeno 9-10 e Anaconda da solo è O(600) MB.
    
    - Una volta installata la macchina virtuale, lo schermo potrebbe essere fissato a 480x360:
    assicuratevi di cambiarla in modo da poterla usare al meglio.

1.3) Installarlo tramite ambiente di Linux per Windows (Windows Subsystem for Linux) WSL:

Scaricare  ubuntu dalla app windows: [qui l'ultima versione](https://apps.microsoft.com/store/detail/ubuntu/9PDXGNCFSCZV?hl=en-us&gl=us&rtc=1&activetab=pivot%3Aoverviewtab)

E poi da PowerShell eseguire:

    wsl --install
    wsl --set-default-version 2
    wsl --install -d ubuntu

Chiederà di scegliere nome utente e password

Lanciarlo da poi tramite programma wsl

## 2) Python3

Con la versione di linux Ubuntu 20.04 e superiori, python3 è automaticamente installato

## 3) pip/conda

3.1) Installare pip:
    
    sudo apt-get install pip

3.2) Istruzioni per Anaconda:
    
    Andare su https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html 
    seguire il link per scaricare l'installer https://www.anaconda.com/products/individual

Per usare il navigatore occorre installare i seguenti pacchetti:

    apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

Eseguire:
    
    sudo bash Anaconda-latest-Linux-x86_64.sh

Nota: può essere necessario aggiungere conda al path. 
Assumendo che anaconda sia installato in /home/myusername/anaconda3    

    PATH=$PATH:~/anaconda3/bin

## 4) git

    sudo apt-get install git
    
## 5) jupyter

Per lanciarlo, da terminale (consigliato) fate:
    
    jupyter-notebook
    
Dovrebbe partire nel browser di base, altrimenti copiate il link al server locale che genera notebook su un browser di vostra scelta.

Potete anche lanciare Anaconda navigator da linea di comando:

    anaconda-navigator

Una volta lanciato l'icona di jupyter dovrebbe apparire sulla front page potete cliccare sull'icona e installarlo o updatarlo.


## 6) root

6.1) **CONSIGLIATO PER JUPYTER** Se c'è conda installato  seguire la procedura qui :
    
    https://root.cern/install/#conda
   
Eseguire:

    conda config --set channel_priority strict
    conda create -c conda-forge --name rootenv root 
    conda activate rootenv
    
Nota bene: conda qui creerà un ambiente nuovo in cui root funziona, questa è la maniera in cui è suggerito fare. L'ambiente di default è "base". 
Se volete far funzionare ROOT dovrete fare sempre
    
    conda activate rootenv

Seguire le istruzioni trovate qui:

    https://root.cern/install

6.2) installare via binaries:
    
Scaricare i binaries qui:
    
    https://root.cern/install/#download-a-pre-compiled-binary-distribution

Eseguire:

    wget https://root.cern/download/root_v6.24.02.Linux-ubuntu20-x86_64-gcc9.3.tar.gz
    tar -xzvf root_v6.24.02.Linux-ubuntu20-x86_64-gcc9.3.tar.gz
    source root/bin/thisroot.sh # also available: thisroot.{csh,fish,bat}

