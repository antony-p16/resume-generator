import streamlit as st
import google.generativeai as genai
from fpdf import FPDF
import os
import tempfile
import unicodedata

# --- Unicode Sanitization for PDF ---
def sanitize_text(text):
    """
    Normalize the input text to remove any special Unicode characters
    that might cause encoding issues when writing to PDF.
    """
    return unicodedata.normalize("NFKD", text).encode("latin-1", "ignore").decode("latin-1")

# --- Streamlit Page Config & CSS ---
st.set_page_config(page_title="Resume & Cover Letter Generator", page_icon="📄", layout="centered")
st.markdown(
    """
    <style>
        .stButton>button {
            color: white;
            background: linear-gradient(90deg, #0072ff 0%, #00c6ff 100%);
            border-radius: 8px;
            font-size: 18px;
            padding: 0.5em 2em;
        }
        .stDownloadButton>button {
            color: white;
            background: #28a745;
            border-radius: 8px;
            font-size: 18px;
            padding: 0.5em 2em;
        }
        .stTextInput>div>div>input, .stTextArea textarea, input, textarea {
            background: #f0f4f8;
            border-radius: 6px;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Gemini API Configuration ---
genai.configure(api_key=os.getenv("API_KEY", "YOUR_GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")

# --- App Title ---
st.markdown("<h1 style='text-align: center; color: #0072ff;'>📄 Resume & Cover Letter Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Powered by Gemini AI</p>", unsafe_allow_html=True)
st.write("---")

# --- Input Form Layout ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Your Name")
        job_role = st.text_input("🎯 Target Job Role")
    with col2:
        education = st.text_area("🎓 Education", height=80)
        experience = st.text_area("💼 Work Experience", height=80)

st.write("")

# --- Generation & Output ---
if st.button("✨ Generate Resume & Cover Letter"):
    if name and education and experience and job_role:
        prompt = f"""Generate a professional resume and cover letter for:
        Name: {name}
        Education: {education}
        Experience: {experience}
        Target Job Role: {job_role}
        Use this data only to make this."""

        with st.spinner("Generating your documents with Gemini AI..."):
            response = model.generate_content(prompt)
            result_text = response.text

        st.success("Generation complete! Preview below:")

        # Show the generated text in an expandable section
        with st.expander("🔍 Preview Resume & Cover Letter"):
            st.markdown(
                f"<pre style='font-size: 15px; background: #f8f9fa; padding: 1em; border-radius: 6px;'>{result_text}</pre>",
                unsafe_allow_html=True
            )

        # --- PDF Generation with Sanitization ---
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"{sanitize_text(name)} - {sanitize_text(job_role)}", ln=True, align="C")
        pdf.ln(5)
        pdf.set_font("Arial", "", 12)
        for line in result_text.split("\n"):
            clean_line = sanitize_text(line)
            pdf.multi_cell(0, 10, clean_line)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        pdf.output(temp_file.name)

        with open(temp_file.name, "rb") as f:
            st.download_button(
                "📥 Download PDF",
                f,
                file_name=f"{sanitize_text(name).replace(' ', '_').lower()}_resume.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Please fill in all fields to generate your resume and cover letter.")
