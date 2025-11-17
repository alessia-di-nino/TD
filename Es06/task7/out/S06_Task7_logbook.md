# S06 — Task 7: Stima del rumore ambientale

Questo report riassume i risultati ottenuti misurando il segnale a fotodiodo con diverse condizioni di illuminazione
(*stanza*, *coperto*, *flash*, *lampada treno*). Per ciascun caso si riportano offset, rumore RMS e picco-picco
dei due canali, oltre alla frequenza dominante nella banda 40–200 Hz (utile per identificare rete, PWM, ecc.).

---

### stanza

- **Frequenza di campionamento**: 10000.0 Hz  
- **Ch1** (ad es. ingresso LED o riferimento):  
  - offset = 0.00554 V, noise RMS = 0.0006786 V, p-p = 0.003683 V
- **Ch2** (uscita amplificatore / fotodiodo):  
  - offset = 0.2276 V, noise RMS = 0.04037 V, p-p = 0.123 V
- **Frequenza dominante** (banda 40–200 Hz): Ch1 = 68.35937500000041 Hz, Ch2 = 195.31250000000117 Hz

![Time](./out/stanza_time.png)
![PSD](./out/stanza_psd.png)

**Commento tecnico.** Il segnale del fotodiodo dovrebbe essere *quasi* continuo in condizioni stazionarie,
ma compaiono oscillazioni per tre motivi tipici: (i) **sfarfallio della rete**: luci alimentate a 50 Hz producono una
modulazione a **100 Hz** (raddrizzamento) chiaramente visibile nella PSD; (ii) **driver/PWM** di LED o torce del telefono,
che introducono armoniche nella banda 100–1 kHz; (iii) **rumore dell’elettronica** (op-amp, quantizzazione ADC, rumore di shot).
La **banda semitrasparente blu/arancio** è costruita come *min–max a finestra scorrevole* e rappresenta **l’inviluppo**
delle fluttuazioni su brevi intervalli: se si allarga, significa che nel breve periodo la variabilità (rumore + ripple)
aumenta anche a offset quasi costante.

---

### coperto

- **Frequenza di campionamento**: 10000.0 Hz  
- **Ch1** (ad es. ingresso LED o riferimento):  
  - offset = 0.005759 V, noise RMS = 0.001091 V, p-p = 0.007365 V
- **Ch2** (uscita amplificatore / fotodiodo):  
  - offset = 0.009611 V, noise RMS = 0.0009599 V, p-p = 0.003729 V
- **Frequenza dominante** (banda 40–200 Hz): Ch1 = 175.78125000000105 Hz, Ch2 = 48.82812500000029 Hz

![Time](./out/coperto_time.png)
![PSD](./out/coperto_psd.png)

**Commento tecnico.** Il segnale del fotodiodo dovrebbe essere *quasi* continuo in condizioni stazionarie,
ma compaiono oscillazioni per tre motivi tipici: (i) **sfarfallio della rete**: luci alimentate a 50 Hz producono una
modulazione a **100 Hz** (raddrizzamento) chiaramente visibile nella PSD; (ii) **driver/PWM** di LED o torce del telefono,
che introducono armoniche nella banda 100–1 kHz; (iii) **rumore dell’elettronica** (op-amp, quantizzazione ADC, rumore di shot).
La **banda semitrasparente blu/arancio** è costruita come *min–max a finestra scorrevole* e rappresenta **l’inviluppo**
delle fluttuazioni su brevi intervalli: se si allarga, significa che nel breve periodo la variabilità (rumore + ripple)
aumenta anche a offset quasi costante.

---

### flash

- **Frequenza di campionamento**: 10000.0 Hz  
- **Ch1** (ad es. ingresso LED o riferimento):  
  - offset = 0.005576 V, noise RMS = 0.0007632 V, p-p = 0.003683 V
- **Ch2** (uscita amplificatore / fotodiodo):  
  - offset = 2.977 V, noise RMS = 0.001742 V, p-p = 0.003729 V
- **Frequenza dominante** (banda 40–200 Hz): Ch1 = 78.12500000000047 Hz, Ch2 = 117.18750000000071 Hz

![Time](./out/flash_time.png)
![PSD](./out/flash_psd.png)

**Commento tecnico.** Il segnale del fotodiodo dovrebbe essere *quasi* continuo in condizioni stazionarie,
ma compaiono oscillazioni per tre motivi tipici: (i) **sfarfallio della rete**: luci alimentate a 50 Hz producono una
modulazione a **100 Hz** (raddrizzamento) chiaramente visibile nella PSD; (ii) **driver/PWM** di LED o torce del telefono,
che introducono armoniche nella banda 100–1 kHz; (iii) **rumore dell’elettronica** (op-amp, quantizzazione ADC, rumore di shot).
La **banda semitrasparente blu/arancio** è costruita come *min–max a finestra scorrevole* e rappresenta **l’inviluppo**
delle fluttuazioni su brevi intervalli: se si allarga, significa che nel breve periodo la variabilità (rumore + ripple)
aumenta anche a offset quasi costante.

---

### lampada_treno

- **Frequenza di campionamento**: 10000.0 Hz  
- **Ch1** (ad es. ingresso LED o riferimento):  
  - offset = 0.006299 V, noise RMS = 0.001576 V, p-p = 0.003683 V
- **Ch2** (uscita amplificatore / fotodiodo):  
  - offset = 2.159 V, noise RMS = 0.005236 V, p-p = 0.02237 V
- **Frequenza dominante** (banda 40–200 Hz): Ch1 = 175.78125000000105 Hz, Ch2 = 195.31250000000117 Hz

![Time](./out/lampada_treno_time.png)
![PSD](./out/lampada_treno_psd.png)

**Commento tecnico.** Il segnale del fotodiodo dovrebbe essere *quasi* continuo in condizioni stazionarie,
ma compaiono oscillazioni per tre motivi tipici: (i) **sfarfallio della rete**: luci alimentate a 50 Hz producono una
modulazione a **100 Hz** (raddrizzamento) chiaramente visibile nella PSD; (ii) **driver/PWM** di LED o torce del telefono,
che introducono armoniche nella banda 100–1 kHz; (iii) **rumore dell’elettronica** (op-amp, quantizzazione ADC, rumore di shot).
La **banda semitrasparente blu/arancio** è costruita come *min–max a finestra scorrevole* e rappresenta **l’inviluppo**
delle fluttuazioni su brevi intervalli: se si allarga, significa che nel breve periodo la variabilità (rumore + ripple)
aumenta anche a offset quasi costante.

---


## Nota metodologica
- L’**alone** è calcolato come min/max su finestre di ~2 ms (aggiustate automaticamente in base a fs).
- La **PSD** è stimata con una FFT a blocchi con finestra di Hann e media (stile Welch semplificato).
- Il **rumore RMS** è la deviazione standard attorno alla media (stima non-bias, ddof=1).

