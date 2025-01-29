from flask import Flask, request, jsonify, render_template
import cv2
import pytesseract
import numpy as np
import os

app = Flask(__name__)

# Set upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Process image to extract features
def extract_features(image_path, dpi=300):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Use Tesseract to extract OCR data
    ocr_data = pytesseract.image_to_data(binary_image, output_type=pytesseract.Output.DICT)
    
    font_sizes = []
    word_spacings = []
    line_spacings = []
    confidences = []
    
    prev_x, prev_y, prev_w, prev_h = None, None, None, None
    
    for i in range(len(ocr_data['level'])):
        x, y, w, h = (ocr_data['left'][i], ocr_data['top'][i], 
                      ocr_data['width'][i], ocr_data['height'][i])
        conf = ocr_data['conf'][i]
        
        if conf == '-1':  # Skip invalid entries
            continue

        font_sizes.append(h)
        confidences.append(int(conf))
        
        if prev_x is not None and prev_y == y:
            word_spacings.append(x - prev_x - prev_w)
        if prev_y is not None and prev_y != y:
            line_spacings.append(y - prev_y)
        
        prev_x, prev_y, prev_w, prev_h = x, y, w, h
    
    # Convert from pixels to cm
    pixel_to_cm = 2.54 / dpi
    avg_font_size = np.mean(font_sizes) * pixel_to_cm if font_sizes else 0
    avg_word_spacing = np.mean(word_spacings) * pixel_to_cm if word_spacings else 0
    avg_line_spacing = np.mean(line_spacings) * pixel_to_cm if line_spacings else 0
    avg_confidence = np.mean(confidences) if confidences else 0
    
    return avg_font_size, avg_word_spacing, avg_line_spacing, avg_confidence

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    avg_font_size, avg_word_spacing, avg_line_spacing, avg_confidence = extract_features(file_path)
    
    return jsonify({
        "font_size_cm": round(avg_font_size, 2),
        "word_spacing_cm": round(avg_word_spacing, 2),
        "line_spacing_cm": round(avg_line_spacing, 2),
        "accuracy_percentage": round(avg_confidence, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
