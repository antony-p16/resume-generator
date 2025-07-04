# 📝 Resume & Cover Letter Generator using Gemini + Streamlit

This is an AI-powered web app that generates professional resumes and tailored cover letters using **Google Gemini (Generative AI)** and a sleek **Streamlit interface**.

---

## 🚀 Features

- ✅ Simple, beautiful UI built with **Streamlit**
- ✅ Uses **Gemini 2.5 Pro** via `google-generativeai`
- ✅ Takes user input: Name, Education, Experience, Job Role
- ✅ Generates resume + cover letter in real-time
- ✅ Provides preview and **PDF download**
- ✅ Fully deployable on **Streamlit Cloud**

---

## 🔧 Technologies Used

- [Streamlit](https://streamlit.io/) – GUI
- [Google Generative AI](https://ai.google.dev/) – Gemini text generation
- [FPDF](https://py-pdf.github.io/fpdf2/) – PDF creation
- Python

---

## 📦 Installation

1. Clone this Repo

```bash
git clone https://github.com/your-username/resume-generator-streamlit.git
cd resume-generator-streamlit
```
2. install dependencies:
```python
pip install -r requirements.txt
```

3. Set your Gemini API key:
```bash
set API_KEY=your_gemini_api_key

OR

export API_KEY=your_gemini_api_key
```

4. Run the app
```bash
streamlit run app.py
```
