# PDF to DOCX Converter

A Python script to convert PDF files into DOCX format using the `pdf2docx` library.

## Features
- Converts a specified PDF file to a DOCX file.
- Allows users to provide custom output file names.
- Easy-to-use input prompt for specifying file paths and names.

## Prerequisites
Before running the script, ensure the following:
- Python 3.6 or higher is installed.
- The `pdf2docx` library is installed. Install it using:
  ```bash
  pip install pdf2docx
  
## How to Use
1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using:
   ```bash
   python script_name.py
   Replace `script_name.py` with the actual script file name.

4. Follow the on-screen prompts:
5. The converted DOCX file will be saved in the same directory as the script.

### Example
  - Enter the path of the PDF file you want to convert `(ex: "/home/novalagung/Desktop/my text.txt"): /path/to/input.pdf`
  - Enter the name of the output file: `output_file_name`
  - Conversion complete! The output file has been saved in: output_file_name.docx

### Notes
- Make sure the specified PDF file path exists and is accessible.
- The output DOCX file will be overwritten if a file with the same name already exists.

## Troubleshooting
- If the script throws a `ModuleNotFoundError `, ensure `pdf2docx` is properly installed:
  ```bash
  pip install pdf2docx

## License
This project is licensed under the MIT License. Feel free to modify and use it as needed.
