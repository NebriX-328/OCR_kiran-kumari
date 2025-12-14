Handwritten OCR Web Application

A production-style full-stack OCR web application that converts handwritten images into accurate, editable digital text using only open-source tools.
The system supports batch image upload, advanced preprocessing, OCR, and post-processing correction, all accessible through a clean web interface.

Features
📤 Upload multiple handwritten images at once
🧹 Advanced image preprocessing
-Grayscale conversion
-Denoising
-Adaptive thresholding
🔍 OCR using Tesseract OCR
✨ Post-processing correction using SymSpell
📝 Page-wise and merged editable text output
📋 Copy extracted text to clipboard
🌐 Full-stack web app (FastAPI + HTML/CSS/JS)
🔒 No external APIs or paid services
⚡ Optimized startup using lazy loading

Frontend (HTML/CSS/JS)
        |
        v
FastAPI Backend
        |
        v
Preprocess Image (OpenCV)
        |
        v
OCR Engine (Tesseract)
        |
        v
Post-process Text (SymSpell)
        |
        v
JSON Response → Frontend UI


handwritten-ocr/
├── backend/
│   ├── app.py
│   ├── preprocess.py
│   ├── ocr.py
│   ├── postprocess.py
│   ├── static/
│   │   └── index.html
│   ├── storage/
│   │   └── uploads/
│   └── venv/
└── README.md

“This project implements a modular OCR pipeline where handwritten images are preprocessed to enhance clarity, processed using an open-source OCR engine, and refined using post-processing correction techniques. The system is deployed as a full-stack web application using FastAPI and a lightweight frontend.”
