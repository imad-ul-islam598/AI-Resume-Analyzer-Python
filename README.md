# 📄 AI-Powered Resume Analyzer

## Growth Mindset Challenge
This is a project that I have been working on as part of a growth mindset challenge. 
I tried my best to make this project good, but as a fresher i did all the things that i understood to make this mini project professional.

## 🚀 Project Overview
The **AI-Powered Resume Analyzer** is a Streamlit-based web application that allows users to upload their resumes in various formats (PDF, DOCX, JPG, PNG). 
It extracts and analyzes resume content, providing professional feedback on its structure, completeness, and key sections. 
The tool helps users to enhance their resumes by identifying missing elements and will give insights on how to improve your resumes for looking more professional and impactful.

## 🎯 Features
✅ Supports Multiple File Formats: Upload your resume in PDF, DOCX, or image formats: **PDF, DOCX, JPEG, PNG, JPG**  
✅ AI-Based Text Extraction: Uses **pdfplumber**, **python-docx**, and **Tesseract OCR** to extract text from different file types. 
✅ Resume Analysis: Checks for essential sections like Experience, Education, Skills, Projects, Certifications, Contact, Languages, Interests, Achievements, Objective, Summary, and Profile Picture.
✅ Feedback & Suggestions: Provides personalized feedback on missing sections and suggestions to improve resume quality.
✅ Dark & Light Theme Support: Customize the UI theme as per user preference.
✅ Modern & Clean UI: Built with Streamlit to ensure a smooth user experience.
✅ Built with **Python, Streamlit, OCR (Tesseract), and NLP techniques**  

## 🛠️ Tech Stack
- **Frontend & Backend**: Streamlit
- **Text Extraction**: pdfplumber, docx, pytesseract (OCR)
- **Image Processing**: PIL (Pillow)
- **Programming Language**: Python

## 📌 Installation & Setup

### 1️⃣ Prerequisites
#### Make sure you have the following installed on your system:
✔️ Python 3.8+
✔️ pip (Python package manager)
✔️ Tesseract OCR (For extracting text from images)

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 3️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate    # For Windows
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Install Tesseract OCR
- Download and install **Tesseract-OCR** from [here](https://github.com/UB-Mannheim/tesseract/wiki)
- Add the installation path to your system environment variables
- Verify the installation by running `tesseract --version` in your terminal

### 6️⃣ Run the Application
```bash
streamlit run app.py
```

## 📖 How to Use
🔹 **Upload** your resume in supported formats (PDF, DOCX, JPEG, PNG, JPG).  
🔹 The app will **extract and analyze** the resume content.  
🔹 You will receive **feedback** on missing sections or appreciation if your resume is well-structured.  
🔹 If improvements are suggested, update your resume accordingly for a more professional touch.  

## 📬 Follow For More...
🔗 GitHub: [imad-ul-islam598](https://github.com/imad-ul-islam598)

