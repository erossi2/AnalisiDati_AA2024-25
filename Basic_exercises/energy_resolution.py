from scipy.stats import poisson,binom,expon
import matplotlib.pyplot as plt
import math
import ROOT


import os


#Possiamo modificare qui questi parametri:
e_init=10
e_lambda=50
res_sigma=5
events=200
nrebin=1
#Nota bene: questa parte può essere modificata per prendere i parametri dall'esterno, da linea di comando o da un file di configurazione (vedremo in ulteriori esempi).


#Se vogliamo usare i numeri prodotti in precedenza possiamo fare, ad esempio:
#from cosmic_muons import muon_rate
#events=int(muon_rate)

#Creiamo una cartella per i files:
initdir="energy_resolution_dir"
if not os.path.exists(initdir):
    os.system("mkdir "+initdir)

#Generiamo una distribuzione esponenziale a lambda= 200
expo1 = ROOT.TF1("exponential","1/[0]*exp(-(x-[1])/[0])",10,200)
expo1.SetParameters(e_lambda,e_init)

#Prendiamo una risoluzione Gaussiana:
res = ROOT.TF1("resolution","1/sqrt([1]*TMath::Pi())*exp(-((x-[0])*(x-[0]))/(2*[1]*[1]))",-200,200)
res.SetParameter(0,0)
res.SetParameter(1,res_sigma)

C1 = ROOT.TCanvas("")
expo1.Draw()
prefix="_l_"+str(e_lambda)+"_s_"+str(res_sigma)+"_n_"+str(events)
if nrebin!=1:
    prefix=prefix+"_rebin_"+str(nrebin)

C1.SaveAs(initdir+"/exponential_"+prefix+".png")

res.Draw()
C1.SaveAs(initdir+"/resolution_"+prefix+".png")

#Mettiamoli in un istogramma:
GenSample = ROOT.TH1F("GenSample","Generated sample",190,10,200)

#E riempiamo:
for i in range(events):
    e0=expo1.GetRandom()
    res.SetParameter(0,e0)
    e1=res.GetRandom()
    GenSample.Fill(e1)

#Se dobbiamo rebinnare:
if(nrebin!=1):
    GenSample.Rebin(nrebin)
#Facciamo il plot senza errori:
GenSample.Draw()
C1.SaveAs(initdir+"/data_l_"+prefix+".png")
#E con barre d'errore
GenSample.Draw("e")
C1.SaveAs(initdir+"/data_witherror_l_"+prefix+".png")

#Facciamo un fit esponenziale:
expo2 = ROOT.TF1("exponential_fit","[2]*1/[0]*exp(-(x-[1])/[0])",10,200)
expo2.SetParameter(0,50)
expo2.SetParameter(2,events)
expo2.FixParameter(1,10)
GenSample.Fit("exponential_fit","")
ROOT.gStyle.SetOptFit(1111)
GenSample.Draw("e")
C1.SaveAs(initdir+"/data_fit_"+prefix+".png")

#E tramite una landau:
landauf = ROOT.TF1("landau_fit","landau",10,200)
landauf.SetParameter(1,10)
landauf.SetParameter(2,50)
landauf.FixParameter(3,20)
GenSample.Fit("landau_fit","")
ROOT.gStyle.SetOptFit(1111)
GenSample.Draw("e")
C1.SaveAs(initdir+"/data_fit_landau_"+prefix+".png")
