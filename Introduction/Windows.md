In generale, Windows non è consigliato per lo sviluppo in HEP, per via in primis di ROOT, ma anche di diverse operazioni eseguite da shell. 

Per far funzionare simultaneamente ROOT, python, jupyter la maniera migliore è usare l'emulatore nativo di Windows 10 via PowerShell, seguono degli step utili.

**CONSIGLIATO** il consiglio è usare la versione con l'emulatore nativo di linux da windows seguendo gli steps 1-5 e poi le  [istruzioni da linux, passi 3-6](https://github.com/oiorio/AnalisiDati/blob/main/1.%20Introduzione/Istruzioni_Linux.md)

## 1) Lanciare la powershell

Powershell dovrebbe essere già presente nella barra dei comandi, bisogna solo fare attenzione a lanciare il comando con privilegi di amministratore per permettere l'installazione di ulteriori componenti / alcune interazioni.

## 2) Lanciare l'emulatore nativo di linux da windows

Queste istruzioni sonoo state testate su ubuntu, quindi si consiglia di fare seguito allo stesso modo.

2.1) In molte installazioni windows c'è già ubuntu installato. Basta digitare da power shell
    
    ubuntu 

oppure

    ubuntu.exe
    
Per controllare si può iniziare a digitare la parola e premere "tab", che effettuerà completamento automatico.

2.2) In caso non sia installato o per installare una versione specifica si può usare Windows Subsystem for Linux (wsl). 

Potete seguire i passi indicati qui:

[https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview)

Ovvero scaricare ubuntu dalla pagina di windows, [qui l'ultima versione](https://apps.microsoft.com/store/detail/ubuntu/9PDXGNCFSCZV?hl=en-us&gl=us&rtc=1&activetab=pivot%3Aoverviewtab)

E poi da PowerShell eseguire:

    wsl --install
    wsl --set-default-version 2
    wsl --install -d ubuntu

Chiederà di scegliere nome utente e password

A questo punto dovrebbe essere possibile lanciare ubuntu come da punto 1

## 3) Installare conda, jupyter, root via powershell

Si possono seguire esattamente le stesse istruzioni riportate qui:

https://github.com/oiorio/AnalisiDati/blob/main/1.%20Introduzione/Istruzioni_Linux.md

## 4) lanciare jupyter

Se avete lanciato la powershell in modalità admin, si può lanciare firefox da windows normalmente e usare il server jupyter generato con linux.

Per farlo basta copiare l'indirizzo fornito al lancio di 

    jupyter-notebook
 
nella barra di firefox.

## 5) Alternativa: installazione macchina virtuale

Alternativamente al punto 2) si può installare la macchina virtuale da qui e seguire le istruzioni generali:

    https://www.virtualbox.org/wiki/Downloads

In particolare la versione per windows:

    https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-Win.exe
