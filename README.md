# 📄 Professional Resume Generator

A comprehensive Python-based resume generator that creates multiple format outputs optimized for different job application scenarios.

## 🎯 Features

- **Multiple Output Formats**: PDF (Standard & Professional), HTML, and ATS-optimized text
- **Professional Design**: Clean, modern layouts with strategic color usage
- **ATS Optimization**: Plain text version optimized for Applicant Tracking Systems
- **High Resolution**: 300 DPI PDF output for print quality
- **Responsive Design**: HTML version works on all devices
- **Document Converter**: Convert any HTML document to professional PDF

## 📋 Generated Formats

### 1. Standard PDF Resume (`Your_Name_Resume.pdf`)
- **Size**: ~38KB
- **Best for**: General job applications, email attachments
- **Features**: Clean, professional, universally compatible

### 2. Professional PDF Resume (`Your_Name_Professional_Resume.pdf`)
- **Size**: ~75KB  
- **Best for**: Executive positions, senior roles
- **Features**: Enhanced design, professional colors, premium appearance

### 3. ATS-Optimized Text (`Your_Name_ATS_Resume.txt`)
- **Size**: ~6.6KB
- **Best for**: Online applications, ATS systems
- **Features**: Plain text, keyword optimized, machine-readable

### 4. HTML Version (`your_resume_professional.html`)
- **Best for**: Web portfolios, easy customization
- **Features**: Responsive design, modern CSS, easily editable

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ubuntu/Debian (for PDF generation)

### Installation

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y wkhtmltopdf

# Clone the repository
git clone https://github.com/egk10/professional-resume-generator.git
cd professional-resume-generator

# Run the generator
python3 generate_professional_resume.py
```

## 📁 Project Structure

```
resume-generator-project/
├── README.md                                    # This file
├── requirements.txt                             # Python dependencies
├── generate_professional_resume.py             # Main generator (enhanced)
├── generate_resume_pdf.py                      # Basic generator with fallbacks
├── generate_document_pdf.py                    # Universal HTML to PDF converter
├── resume_manager.py                           # File management and summary
├── Your_Name_Resume.pdf                        # Standard PDF output (generated)
├── Your_Name_Professional_Resume.pdf           # Professional PDF output (generated)
├── Your_Name_ATS_Resume.txt                    # ATS-optimized text (generated)
└── your_resume_professional.html               # HTML source (generated)
```

## 🛠️ Usage

### First Time Setup
**Important**: Before generating your resume, you need to customize the content in the Python files with your personal information.

1. **Edit the HTML content** in `generate_professional_resume.py` to include your:
   - Name and contact information
   - Professional experience
   - Education and certifications
   - Skills and competencies

2. **Update the ATS content** in `resume_manager.py` with your information

3. **Customize file naming** throughout the scripts to match your name

### Generate All Formats
```bash
python3 resume_manager.py
```

### Generate Professional PDF Only
```bash
python3 generate_professional_resume.py
```

### Generate with Fallback Options
```bash
python3 generate_resume_pdf.py
```

### Convert Any HTML Document to PDF
```bash
# For legal documents (wider margins)
python3 generate_document_pdf.py document.html --type legal

# For resumes (standard margins)
python3 generate_document_pdf.py resume.html --type resume

# For reports (medium margins)
python3 generate_document_pdf.py report.html --type report --output custom_name.pdf
```

## 🎯 Use Case Recommendations

| Scenario | Recommended File | Why |
|----------|------------------|-----|
| 🏢 General Applications | Standard PDF | Clean, professional, widely compatible |
| 💼 Executive Positions | Professional PDF | Enhanced design, visual appeal |
| 🤖 ATS/Online Systems | ATS Text | Plain text, keyword optimized |
| 📧 Email Attachments | Standard PDF | Small file size, fast loading |
| 🌐 Web Portfolio | HTML | Web-friendly, easily customizable |
| 📄 Legal Documents | Any HTML | Use `generate_document_pdf.py --type legal` |
| 📊 Reports | Any HTML | Use `generate_document_pdf.py --type report` |

## 📝 License

This project is open source and available under the MIT License.

---

**Generated Resume Formats**: ✅ PDF (Standard & Professional) ✅ HTML ✅ ATS-Optimized Text  
**Print Ready**: ✅ 300 DPI ✅ Professional Layout ✅ Color & B&W Compatible  
**ATS Compatible**: ✅ Keyword Optimized ✅ Plain Text ✅ Machine Readable
