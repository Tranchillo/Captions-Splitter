
# Captions Splitter Script

## Descrizione
Questo script Python automatizza il processo di estrazione e salvataggio di caption da un file di testo. Ogni caption viene salvata in un file separato, con un nome basato su un identificatore numerico presente all'inizio di ogni riga del file di input.

### Funzionalità principali
- Legge un file di testo contenente più righe di caption.
- Estrae l'identificatore numerico all'inizio di ogni riga.
- Salva ogni caption estratta in un file `.txt` separato, utilizzando l'identificatore numerico come nome del file.

## Requisiti
- Python 3 installato sul sistema.
- File di input (`caption_list.txt`) formattato con righe contenenti un identificatore numerico seguito dalla caption (ad esempio: `001 h4b1t4t, a person in winter clothes...`).

## Come utilizzare

### Passaggi:
1. Posiziona il file di input (`caption_list.txt`) nella stessa directory dello script Python (`generate_captions.py`).
2. Assicurati che Python sia installato e configurato correttamente.
3. Se desideri semplificare l'esecuzione, usa il file `.bat` fornito per avviare lo script.

### Esecuzione manuale:
1. Apri un terminale o prompt dei comandi.
2. Spostati nella directory contenente lo script:
   ```bash
   cd /path/to/your/script
   ```
3. Esegui lo script:
   ```bash
   python generate_captions.py
   ```

### Esecuzione tramite file `.bat`:
1. Fai doppio clic sul file `run_script.bat`.
2. Lo script verrà eseguito automaticamente e i file saranno generati.

## Output
Lo script creerà una directory chiamata `output_captions` (se non esiste già) e salverà i file generati al suo interno. Ogni file avrà:
- Nome: il numero identificativo della riga (es. `001.txt`, `002.txt`, ecc.).
- Contenuto: la caption corrispondente alla riga di input.

## Esempio di input
File `caption_list.txt`:
```
001 h4b1t4t, a person in winter clothes with a fur-lined hood, standing in a snow-covered landscape, with a desert habitat above their head.
002 h4b1t4t, a young woman in a white tennis outfit, standing on a tennis court, with a serene lake habitat above her head.
003 h4b1t4t, a person in skateboarding gear at a skatepark, with a small ocean habitat above their head.
```

### Esempio di output
Directory `output_captions`:
- `001.txt` con contenuto:
  ```
  h4b1t4t, a person in winter clothes with a fur-lined hood, standing in a snow-covered landscape, with a desert habitat above their head.
  ```
- `002.txt` con contenuto:
  ```
  h4b1t4t, a young woman in a white tennis outfit, standing on a tennis court, with a serene lake habitat above her head.
  ```
- `003.txt` con contenuto:
  ```
  h4b1t4t, a person in skateboarding gear at a skatepark, with a small ocean habitat above their head.
  ```

## Personalizzazioni
Se il file di input ha un nome diverso o si trova in un'altra directory, modifica la variabile `input_file` nello script Python per specificarne il percorso.

## Risoluzione dei problemi
- **Errore "Python non trovato":** Assicurati che Python sia aggiunto al `PATH` del sistema.
- **File di input non trovato:** Verifica che il file di input si trovi nella posizione corretta e che il nome corrisponda a quello indicato nello script (`caption_list.txt`).

## Licenza
Questo script è fornito "così com'è" e può essere modificato liberamente per adattarlo alle tue esigenze.
