from flask import Flask, render_template, request, send_file
import google.generativeai as genai
from fpdf import FPDF
import tempfile

app = Flask(__name__)

genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-2.5-pro")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    education = request.form["education"]
    experience = request.form["experience"]
    job_role = request.form["job_role"]

    prompt = f"""Generate a resume and cover letter for:
    Name: {name}
    Education: {education}
    Experience: {experience}
    Target Job Role: {job_role}"""

    response = model.generate_content(prompt).text

    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in response.split("\n"):
        pdf.multi_cell(0, 10, line)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)

    return send_file(temp_file.name, as_attachment=True, download_name="resume.pdf")

if __name__ == "__main__":
    app.run(debug=True)
