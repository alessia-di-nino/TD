import tdwf # importiamo il modulo...
import matplotlib.pyplot as plt
import numpy as np

ad2 = tdwf.AD2() # connessione all’hardware
 
 
scope = tdwf.Scope(ad2.hdwf) # inizializzazione oscilloscopio
scope.fs = 1e6 # => frequenza di sampling impostata a 1MSa/s
scope.npt = 1000 # => acquisizione impostata a 1000 punti
 
scope.ch1.rng = 5 # range Ch1 su [-2.5,+2.5]
scope.ch2.rng = 50 # range Ch2 su [-25,+25]
 
 
scope.ch2.avg = True # attiva media su Ch2
scope.sample() # Avvio acquisizione
 
print(scope.ch1.vals) # stampa su shell 

plt.plot(scope.time.vals, scope.ch1.vals)
plt.xlabel("Tempo [s]")
plt.ylabel("Ch1 [V]")

data = np.column_stack((scope.time.vals,scope.ch1.vals,scope.ch2.vals))
np.savetxt("nomefile.txt", data, delimiter="\t")

scope.sample() # Avvio acquisizione
 
print(scope.ch1.vals) # stampa su shell 

plt.plot(scope.time.vals, scope.ch1.vals)
plt.xlabel("Tempo [s]")
plt.ylabel("Ch1 [V]")

data = np.column_stack((scope.time.vals,scope.ch1.vals,scope.ch2.vals))
np.savetxt("nomefile.txt", data, delimiter="\t")


plt.show()