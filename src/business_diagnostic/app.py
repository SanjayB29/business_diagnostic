# from flask import Flask, render_template, request, jsonify
# from business_diagnostic.crew import ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew
# from markdown_pdf import MarkdownPdf, Section

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('input.html')

# @app.route('/generate', methods=['POST'])
# def generate_report():
#     try:
#         # Get form data
#         company_name = request.form.get('company_name')
#         company_website = request.form.get('company_website')

#         # Validate input
#         if not company_name or not company_website:
#             return jsonify({'error': 'Please provide both company name and website.'}), 400

#         # Run the crew process
#         inputs = {
#             'company_name': company_name,
#             'company_website': company_website,
#         }
#         report = ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew().crew().kickoff(inputs=inputs)

#         # Generate Markdown and PDF files
#         pdf = MarkdownPdf(toc_level=1)
#         pdf.add_section(Section(report.raw))
#         file_name = f"{inputs['company_name']}_diagnostic_report.pdf"
#         pdf.save(file_name)

#         return jsonify({'success': True, 'file_name': file_name}), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# def main():
#     app.run(debug=True)
#----------------------------------------------------------------------------------------------------------------------------

# from flask import Flask, render_template, request, jsonify, send_file
# import markdown2
# from business_diagnostic.crew import ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew
# from markdown_pdf import MarkdownPdf, Section
# import os

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('input.html')

# @app.route('/generate', methods=['POST'])
# def generate_report():
#     try:
#         # Get form data
#         company_name = request.form.get('company_name')
#         company_website = request.form.get('company_website')

#         # Validate input
#         if not company_name or not company_website:
#             return jsonify({'error': 'Please provide both company name and website.'}), 400

#         # Run the crew process
#         inputs = {
#             'company_name': company_name,
#             'company_website': company_website,
#         }
#         report = ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew().crew().kickoff(inputs=inputs)

#         # Save Markdown file
#         md_file_name = f"{inputs['company_name']}_diagnostic_report.md"
#         with open(md_file_name, 'w') as f:
#             f.write(report.raw)

#         # Generate PDF file
#         pdf = MarkdownPdf(toc_level=1)
#         pdf.add_section(Section(report.raw))
#         pdf_file_name = f"{inputs['company_name']}_diagnostic_report.pdf"
#         pdf.save(pdf_file_name)

#         return jsonify({'success': True, 'md_file_name': md_file_name, 'pdf_file_name': pdf_file_name}), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/view/<filename>')
# def view_file(filename):
#     try:
#         # Ensure file exists
#         if not os.path.exists(filename):
#             return f"File {filename} not found", 404

#         # Convert Markdown to HTML using markdown2
#         with open(filename, 'r') as f:
#             md_content = f.read()
#             html_content = markdown2.markdown(md_content)

#         return render_template('view.html', html_content=html_content)

#     except Exception as e:
#         return f"An error occurred: {e}", 500

# def main():
#     app.run(debug=True)
#----------------------------------------------------------------------------------------------------------------------------
# from flask import Flask, render_template, request, jsonify
# import markdown2
# from business_diagnostic.crew import ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew
# from markdown_pdf import MarkdownPdf, Section
# import os

# app = Flask(__name__)

# # Directory to store generated files
# GENERATED_FILES_DIR = r"src\business_diagnostic\generated_files"
# if not os.path.exists(GENERATED_FILES_DIR):
#     os.makedirs(GENERATED_FILES_DIR)

# # Global list to store generated files
# generated_files = []

# @app.route('/')
# def home():
#     return render_template('input.html', generated_files=generated_files)

# @app.route('/generate', methods=['POST'])
# def generate_report():
#     try:
#         # Get form data
#         company_name = request.form.get('company_name')
#         company_website = request.form.get('company_website')

#         # Validate input
#         if not company_name or not company_website:
#             return jsonify({'error': 'Please provide both company name and website.'}), 400

#         # Run the crew process
#         inputs = {
#             'company_name': company_name,
#             'company_website': company_website,
#         }
#         report = ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew().crew().kickoff(inputs=inputs)

#         # Save Markdown file
#         md_file_name = os.path.join(GENERATED_FILES_DIR, f"{inputs['company_name']}_diagnostic_report.md")
#         with open(md_file_name, 'w') as f:
#             f.write(report.raw)

#         # Generate PDF file
#         pdf = MarkdownPdf(toc_level=1)
#         pdf.add_section(Section(report.raw))
#         pdf_file_name = os.path.join(GENERATED_FILES_DIR, f"{inputs['company_name']}_diagnostic_report.pdf")
#         pdf.save(pdf_file_name)

#         # Store file information
#         generated_files.append({
#             'company_name': company_name,
#             'md_file_name': md_file_name,
#             'pdf_file_name': pdf_file_name
#         })

#         return jsonify({'success': True, 'md_file_name': md_file_name, 'pdf_file_name': pdf_file_name}), 200

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/view/<path:filename>')
# def view_file(filename):
#     try:
#         # Ensure file exists
#         if not os.path.exists(filename):
#             return f"File {filename} not found", 404

#         # Convert Markdown to HTML using markdown2
#         with open(filename, 'r') as f:
#             md_content = f.read()
#             html_content = markdown2.markdown(md_content)

#         return render_template('view.html', html_content=html_content)

#     except Exception as e:
#         return f"An error occurred: {e}", 500

# @app.route('/download/<path:filename>')
# def download_file(filename):
#     try:
#         if not os.path.exists(filename):
#             return f"File {filename} not found", 404
#         return send_file(filename, as_attachment=True)
#     except Exception as e:
#         return f"An error occurred: {e}", 500

# def main():
#     app.run(debug=True)
#----------------------------------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request, jsonify, send_file
import markdown2
from business_diagnostic.crew import ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew
from markdown_pdf import MarkdownPdf, Section
import os

app = Flask(__name__)

# Directory to store generated files
GENERATED_FILES_DIR = r"src\business_diagnostic\generated_files"
if not os.path.exists(GENERATED_FILES_DIR):
    os.makedirs(GENERATED_FILES_DIR)

# Global list to store generated files metadata
generated_files = []

# Load previously generated files from the directory
def load_generated_files():
    for filename in os.listdir(GENERATED_FILES_DIR):
        if filename.endswith("_diagnostic_report.md"):
            company_name = filename.split("_diagnostic_report.md")[0]
            md_file_name = os.path.join(GENERATED_FILES_DIR, filename)
            pdf_file_name = os.path.join(GENERATED_FILES_DIR, f"{company_name}_diagnostic_report.pdf")
            if os.path.exists(pdf_file_name):
                generated_files.append({
                    'company_name': company_name,
                    'md_file_name': md_file_name,
                    'pdf_file_name': pdf_file_name
                })

# Load files at application start
load_generated_files()

@app.route('/')
def home():
    return render_template('input.html', generated_files=generated_files)

@app.route('/generate', methods=['POST'])
def generate_report():
    try:
        # Get form data
        company_name = request.form.get('company_name')
        company_website = request.form.get('company_website')

        # Validate input
        if not company_name or not company_website:
            return jsonify({'error': 'Please provide both company name and website.'}), 400

        # Run the crew process
        inputs = {
            'company_name': company_name,
            'company_website': company_website,
        }
        report = ComprehensiveBusinessDiagnosticAndMarketAnalysisToolCrew().crew().kickoff(inputs=inputs)

        # Save Markdown file
        md_file_name = os.path.join(GENERATED_FILES_DIR, f"{inputs['company_name']}_diagnostic_report.md")
        with open(md_file_name, 'w') as f:
            f.write(report.raw)

        # Generate PDF file
        pdf = MarkdownPdf(toc_level=1)
        pdf.add_section(Section(report.raw))
        pdf_file_name = os.path.join(GENERATED_FILES_DIR, f"{inputs['company_name']}_diagnostic_report.pdf")
        pdf.save(pdf_file_name)

        # Add to global metadata list
        generated_files.append({
            'company_name': company_name,
            'md_file_name': md_file_name,
            'pdf_file_name': pdf_file_name
        })

        return jsonify({'success': True, 'md_file_name': md_file_name, 'pdf_file_name': pdf_file_name}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/view/<path:filename>')
def view_file(filename):
    try:
        # Ensure file exists
        if not os.path.exists(filename):
            return f"File {filename} not found", 404

        # Convert Markdown to HTML using markdown2
        with open(filename, 'r') as f:
            md_content = f.read()
            html_content = markdown2.markdown(md_content)

        return render_template('view.html', html_content=html_content)

    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        if not os.path.exists(filename):
            return f"File {filename} not found", 404
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"An error occurred: {e}", 500

def main():
    app.run(debug=True)
