import os
from PIL import Image
import pytesseract
import fitz

def save_uploaded_file(file, folder, filename):
    file_path = os.path.join(folder, filename)
    file.save(file_path)
    return file_path

def extract_text_from_pdf(pdf_filename, page_num):
    try:
        with fitz.open(pdf_filename) as doc:
            if page_num > doc.page_count:
                return f"Invalid page number. The PDF has {doc.page_count} pages."
            else:
                page = doc.load_page(page_num - 1)
                scaling_matrix = fitz.Matrix(2, 2)
                pixmap = page.get_pixmap(matrix=scaling_matrix)
                extract_image = 'extract.png'
                pixmap.save(extract_image)
                return extract_image
    except FileNotFoundError:
        return f"PDF file '{pdf_filename}' not found."

def extract_text_from_image(image_filename):
    try:
        image = Image.open(image_filename)
        image_path = 'extract.png'
        image.save(image_path)
        return image_path
    except FileNotFoundError:
        return f"Image file '{image_filename}' not found."

def perform_ocr(image_path):
    try:
        image = Image.open(image_path)
        ocr_text = pytesseract.image_to_string(image)
        cleanup_image(image_path)
        return ocr_text
    except pytesseract.TesseractError as e:
        return f"Tesseract OCR error: {str(e)}"
    except Exception as e:
        return f"Error during OCR: {str(e)}"

def cleanup_image(image_path):
    if image_path:
        try:
            os.remove(image_path)
        except Exception as e:
            pass

def handle_error(e):
    return f"An error occurred: {str(e)}"
