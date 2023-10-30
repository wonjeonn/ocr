from flask import render_template, request, Blueprint
from app.ocr import extract_text_from_pdf, extract_text_from_image, perform_ocr, handle_error, cleanup_image, save_uploaded_file

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/pdf', methods=['POST'])
def handle_pdf():
    if 'pdf_file' in request.files:
        pdf_file = request.files['pdf_file']

        if pdf_file.filename != '':
            pdf_filename = save_uploaded_file(pdf_file, 'uploads', pdf_file.filename)
            page_num = request.form.get('page_num')
            try:
                page_num = int(page_num)
            except ValueError:
                return "Invalid page number. Please enter a valid page number."

            try:
                extracted_image = extract_text_from_pdf(pdf_filename, page_num)
                ocr_result = perform_ocr(extracted_image)
                cleanup_image(extracted_image)
                cleanup_image(pdf_filename)
                return render_template('pdf.html', ocr_result=ocr_result)

            except Exception as e:
                return handle_error(e)

    return "PDF file not found."

@main_bp.route('/image', methods=['POST'])
def handle_image():
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        if image_file.filename != '':
            image_filename = save_uploaded_file(image_file, 'uploads', image_file.filename)

            try:
                extracted_image = extract_text_from_image(image_filename)
                ocr_result = perform_ocr(extracted_image)
                cleanup_image(image_filename)
                return render_template('image.html', ocr_result=ocr_result)

            except Exception as e:
                return handle_error(e)

    return "Image file not found."
