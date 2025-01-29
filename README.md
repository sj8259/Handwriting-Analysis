<?xml version="1.0" encoding="UTF-8"?>
<project>
    <name>Handwriting Analysis</name>
    <overview>
        <description>This project is a Handwriting Analysis tool that extracts key features such as line spacing, font size, and word spacing from handwritten text images. It uses Flask for the backend, Tesseract OCR for text recognition, and OpenCV for image processing.</description>
    </overview>
    <features>
        <feature>Upload an image of handwritten text</feature>
        <feature>Extract font size, word spacing, and line spacing</feature>
        <feature>Compute OCR confidence level</feature>
        <feature>Return results in JSON format</feature>
    </features>
    <technologies>
        <technology>Python</technology>
        <technology>Flask</technology>
        <technology>OpenCV</technology>
        <technology>Tesseract OCR</technology>
        <technology>NumPy</technology>
        <technology>HTML/CSS (for frontend rendering)</technology>
    </technologies>
    <installation>
        <step>Clone the repository:</step>
        <command>git clone https://github.com/your-username/handwriting-analysis.git</command>
        <command>cd handwriting-analysis</command>
        <step>Create a virtual environment:</step>
        <command>python -m venv venv</command>
        <command>source venv/bin/activate  # On Windows use: venv\Scripts\activate</command>
        <step>Install dependencies:</step>
        <command>pip install -r requirements.txt</command>
        <step>Install Tesseract OCR:</step>
        <platform>
            <windows>Download and install from official site</windows>
            <linux>sudo apt install tesseract-ocr</linux>
            <macos>brew install tesseract</macos>
        </platform>
    </installation>
    <usage>
        <step>Start the Flask application:</step>
        <command>python app.py</command>
        <step>Open browser:</step>
        <command>http://127.0.0.1:5000/</command>
        <step>Upload an image and get results in JSON format.</step>
    </usage>
    <api>
        <endpoint method="POST" path="/upload">
            <description>Accepts an image file and returns handwriting analysis results.</description>
            <request>
                <file type="JPEG/PNG">Image file</file>
            </request>
            <response>
                <font_size_cm>0.45</font_size_cm>
                <word_spacing_cm>0.30</word_spacing_cm>
                <line_spacing_cm>0.75</line_spacing_cm>
                <accuracy_percentage>85.4</accuracy_percentage>
            </response>
        </endpoint>
    </api>
    <folder_structure>
        <folder name="handwriting-analysis">
            <file>app.py (Main Flask application)</file>
            <folder name="templates">
                <file>index.html (Frontend UI)</file>
            </folder>
            <folder name="uploads">Stores uploaded images</folder>
            <file>requirements.txt (Dependencies)</file>
            <file>README.md (Project documentation)</file>
        </folder>
    </folder_structure>
    <license>
        <type>MIT License</type>
    </license>
    <author>
        <name>Thuraka Sai JEevan</name>
        <github>Your GitHub Profile</github>
    </author>
    <contributions>
        <description>Pull requests are welcome! If you find any bugs or want to enhance features, feel free to contribute.</description>
    </contributions>
    <message>Happy Coding! 🚀</message>
</project>
