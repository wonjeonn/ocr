# Optical Character Recognition (OCR)

This is an Optical Character Recognition (OCR) web application that allows users to extract text from both PDF files and images.

## Installation

Before using the OCR script, you need to install the required prerequisites:

- Python 3.x
- Tesseract OCR engine
- Flask (Python web framework)
- Python libraries: PyMuPDF (a Python binding for the MuPDF PDF parsing and rendering library), pytesseract, Pillow

### Installation on Windows

You can install Tesseract on Windows by following the instructions on the [UB-Mannheim/tesseract GitHub wiki](https://github.com/UB-Mannheim/tesseract/wiki).

After Tesseract is installed, use the following commands to install the required Python libraries:

```bash
python3 -m pip install pytesseract
python3 -m pip install Pillow
python3 -m pip install pymupdf
python3 -m pip install flask
```

### Installation on macOS

If you are using macOS, you can install Homebrew using the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once Homebrew is installed, you can install Tesseract and the required Python libraries with the following commands:

```bash
brew install tesseract
which tesseract

python3 -m pip install pytesseract
python3 -m pip install Pillow
python3 -m pip install pymupdf
python3 -m pip install flask
```

## Usage

1. Access the web application in your web browser.

2. Choose the OCR option you want: "PDF to Text" or "Image to Text."

3. Click the "Extract Text" button to perform OCR and display the extracted text on the result page.

## Project Structure

| Directory/File    | Description                                                |
|-------------------|------------------------------------------------------------|
| OCR/              | Root directory of the project                              |
| app/              | Application code                                           |
|   ├── __init__.py | Initialization file for the `app` package                  |
|   ├── ocr.py      | Contains OCR-related functionality                         |
|   └── routes.py   | Contains routes for the web application.                   |
| static/           | Static files                                               |
|   └── style.css   | CSS styles for the application                             |
| templates/        | HTML templates for web pages                               |
|   ├── image.html  | Template for image OCR page                                |
|   ├── index.html  | Template for the main page                                 |
|   └── pdf.html    | Template for PDF OCR page                                  |
| uploads/          | Temporary storage for extracted files (auto-cleaned)       |
| main.py           | Main entry point for the application                       |
