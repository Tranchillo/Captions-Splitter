import os

# Nome del file di input
input_file = "caption_list.txt"

# Directory in cui salvare i file generati
output_dir = "output_captions"

# Creazione della directory di output, se non esiste
os.makedirs(output_dir, exist_ok=True)

# Lettura del file di input
with open(input_file, "r") as file:
    lines = file.readlines()

# Elaborazione delle linee
for line in lines:
    # Ignora linee vuote
    if not line.strip():
        continue
    
    # Divide il numero dalla descrizione
    parts = line.split(" ", 1)
    if len(parts) != 2:
        continue  # Salta linee malformate
    
    file_name = parts[0]  # Primo elemento come nome file
    caption_content = parts[1].strip()  # Secondo elemento come contenuto

    # Percorso completo per il file di output
    output_file_path = os.path.join(output_dir, f"{file_name}.txt")

    # Scrittura del contenuto nel file
    with open(output_file_path, "w") as output_file:
        output_file.write(caption_content)

print(f"File generati nella directory: {output_dir}")
