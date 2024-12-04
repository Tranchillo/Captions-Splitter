
# Captions Splitter Script

## Description
This Python script automates the process of extracting and saving captions from a text file. Each caption is saved in a separate file, named based on a numerical identifier at the beginning of each line in the input file.

### Key Features
- Reads a text file containing multiple lines of captions.
- Extracts the numerical identifier at the beginning of each line.
- Saves each extracted caption into a separate `.txt` file, using the numerical identifier as the file name.

## Requirements
- Python 3 installed on your system.
- Input file (`caption_list.txt`) formatted with lines containing a numerical identifier followed by the caption (e.g., `001 h4b1t4t, a person in winter clothes...`).

## How to Use

### Steps:
1. Place the input file (`caption_list.txt`) in the same directory as the Python script (`generate_captions.py`).
2. Ensure Python is installed and configured correctly.
3. To simplify execution, use the provided `.bat` file to run the script.

### Manual Execution:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script:
   ```bash
   cd /path/to/your/script
   ```
3. Run the script:
   ```bash
   python generate_captions.py
   ```

### Execution via `.bat` File:
1. Double-click on the `run_script.bat` file.
2. The script will execute automatically, and the files will be generated.

## Output
The script will create a directory named `output_captions` (if it doesn’t already exist) and save the generated files inside it. Each file will have:
- Name: The numerical identifier from the input line (e.g., `001.txt`, `002.txt`, etc.).
- Content: The caption corresponding to the input line.

## Input Example
Input file `caption_list.txt`:
```
001 h4b1t4t, a person in winter clothes with a fur-lined hood, standing in a snow-covered landscape, with a desert habitat above their head.
002 h4b1t4t, a young woman in a white tennis outfit, standing on a tennis court, with a serene lake habitat above her head.
003 h4b1t4t, a person in skateboarding gear at a skatepark, with a small ocean habitat above their head.
```

### Output Example
Directory `output_captions`:
- `001.txt` containing:
  ```
  h4b1t4t, a person in winter clothes with a fur-lined hood, standing in a snow-covered landscape, with a desert habitat above their head.
  ```
- `002.txt` containing:
  ```
  h4b1t4t, a young woman in a white tennis outfit, standing on a tennis court, with a serene lake habitat above her head.
  ```
- `003.txt` containing:
  ```
  h4b1t4t, a person in skateboarding gear at a skatepark, with a small ocean habitat above their head.
  ```

## Customization
If the input file has a different name or is located in another directory, modify the `input_file` variable in the Python script to specify its path.

## Troubleshooting
- **"Python not found" Error:** Ensure that Python is added to your system's `PATH`.
- **Input file not found:** Verify that the input file is in the correct location and that its name matches what is specified in the script (`caption_list.txt`).

## License
This script is provided "as is" and can be freely modified to suit your needs.
