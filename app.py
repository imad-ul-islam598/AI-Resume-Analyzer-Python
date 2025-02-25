import streamlit as st # streamlit → For building the web app
import pdfplumber # pdfplumber → For extracting text from PDF files
import docx # python-docx → For extracting text from DOCX files
import pytesseract # pytesseract → For extracting text from images like PNG, JPG, JPEG etc
from PIL import Image # Pillow → For opening and manipulating images
import io # io → For reading and writing files

import streamlit as st
import pdfplumber
import docx
import pytesseract
from PIL import Image
import io

# Set Tesseract Path (Ensure Tesseract is Installed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set Page Config
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

# Initialize Session State for Theme and Uploaded File
if "theme" not in st.session_state:
    st.session_state["theme"] = "Light"

if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None

# Sidebar Theme Selection
theme_choice = st.sidebar.radio("Choose Theme", ["Light", "Dark"], index=0)

# Update Theme ONLY if changed
if theme_choice != st.session_state["theme"]:
    st.session_state["theme"] = theme_choice
    st.rerun()

# Function to Apply UI Styling
def apply_theme():
    if st.session_state["theme"] == "Dark":
        st.markdown(
            """
            <style>
                body { background-color: #121212; color: #EAEAEA; }
                .stApp { background-color: #0d1b2a; color: #fff; }
                .main-container { background-color: #222831; padding: 2rem; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.5); }
                .success { color: #7CFC00; font-size: 18px; font-weight: bold; }
                .warning { color: #FF0000; font-size: 18px; font-weight: bold; }
                h1, h2, h3 { color: #00ADB5; }
                .stApp h1 { color: #1F51FF; }
                .stApp h3 { color: #e0e1dd; }
                div.stFileUploader label { color: #fff !important; font-weight: bold; }
                section[data-testid="stSidebar"] { background-color: #0d1b2a !important; border-top-right-radius: 40px; width: 3rem; }
                div[data-testid="stRadio"] label { color: white !important; font-weight: bold; }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
                body { background-color: white; color: black; }
                .stApp { background-color: #F5F5F5; }
                .main-container { background-color: white; padding: 2rem; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); }
                .success { color: green; font-size: 18px; }
                .warning { color: red; font-size: 18px; }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Apply Theme
apply_theme()

# Title Section
st.title("📄 AI-Powered Resume Analyzer")
st.subheader("Upload your resume and get professional feedback instantly!")

# File Upload
uploaded_file = st.file_uploader("Upload your Resume (PDF, DOCX, JPEG, PNG, JPG)", type=["pdf", "docx", "jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.session_state["uploaded_file"] = uploaded_file

uploaded_file = st.session_state["uploaded_file"]

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_image(image_file):
    try:
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image)
        return text if text.strip() else "⚠️ No readable text found. Ensure the resume text is clear and not handwritten."
    except Exception:
        return "⚠️ Image text extraction failed. Ensure Tesseract-OCR is installed or upload a PDF/DOCX instead."

def analyze_resume(text):
    required_sections = ["Experience", "Education", "Skills", "Projects", "Certifications", "Contact"]
    optional_sections = ["Languages", "Interests", "Achievements", "Objective", "Summary", "Profile Picture"]
    
    missing_required = [section for section in required_sections if section.lower() not in text.lower()]
    missing_optional = [section for section in optional_sections if section.lower() not in text.lower()]
    
    if len(text.split()) < 100:
        return "Your resume is too short. Consider adding more details."
    
    if not missing_required:
        appreciation = "🎉 Your resume has all the necessary elements! Well done!"
        if not missing_optional:
            return appreciation + " It is highly professional and complete."
        else:
            return appreciation + f" However, consider adding: {', '.join(missing_optional)} to enhance it."
    
    return f"Your resume is missing these key sections: {', '.join(missing_required)}. If you add these sections in your RESUME, this will make it more attractive and professional!"

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")
    st.write("Resume Name:", uploaded_file.name)
    
    extracted_text = ""
    if uploaded_file.type == "application/pdf":
        extracted_text = extract_text_from_pdf(io.BytesIO(uploaded_file.getvalue()))
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        extracted_text = extract_text_from_docx(io.BytesIO(uploaded_file.getvalue()))
    elif uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        extracted_text = extract_text_from_image(io.BytesIO(uploaded_file.getvalue()))
    
    if extracted_text:
        feedback = analyze_resume(extracted_text)
        
        if "🎉" in feedback:
            st.markdown(f'<p class="success">{feedback}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="warning">{feedback}</p>', unsafe_allow_html=True)
        
        with st.expander("📄 View Extracted Resume Text"):
            st.text_area("Extracted Text:", extracted_text, height=250)
    else:
        st.warning("Could not extract text from your resume. Please check the file format.")
