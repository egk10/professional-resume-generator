#!/usr/bin/env python3
"""
Script to generate PDF from HTML resume
"""

import subprocess
import sys
from pathlib import Path

def install_dependencies():
    """Install required dependencies for PDF generation"""
    print("📦 Installing required dependencies...")
    
    # Install weasyprint and dependencies
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "weasyprint"], 
                      check=True, capture_output=True)
        print("✅ weasyprint installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install weasyprint: {e}")
        return False
    
    return True

def create_html_file():
    """Create the HTML resume file"""
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Elie Georges Kfouri - Resume</title>
    <style>
        @page {
            size: A4;
            margin: 2cm;
        }
        body {
            font-family: Arial, sans-serif;
            line-height: 1.4;
            margin: 0;
            color: #333;
            font-size: 11px;
        }
        .header {
            text-align: center;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .name {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .contact {
            font-size: 11px;
            color: #666;
        }
        .section {
            margin-bottom: 18px;
            page-break-inside: avoid;
        }
        .section-title {
            font-size: 14px;
            font-weight: bold;
            border-bottom: 1px solid #ccc;
            padding-bottom: 3px;
            margin-bottom: 8px;
            color: #000;
        }
        .job-title {
            font-weight: bold;
            font-size: 12px;
        }
        .company {
            font-style: italic;
            margin-bottom: 3px;
            font-size: 11px;
        }
        .date {
            font-style: italic;
            font-size: 10px;
            color: #666;
        }
        .achievement {
            margin: 4px 0;
            padding-left: 15px;
        }
        .subsection {
            margin: 8px 0;
        }
        .competency {
            margin: 3px 0;
        }
        .course {
            margin: 2px 0;
            font-size: 10px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="name">Elie Georges Kfouri</div>
        <div class="contact">
            <strong>Email:</strong> eliegkfouri@gmail.com | <strong>Phone:</strong> 437-655-1527 | 
            <strong>Location:</strong> M5V 3K8 - Toronto, ON, Canada | 
            <strong>LinkedIn:</strong> linkedin.com/in/elie-kfouri
        </div>
    </div>

    <div class="section">
        <div class="section-title">Professional Summary</div>
        <p><strong>Civil Engineering Professional</strong> with extensive experience in construction project management and cost estimation, specializing in high-rise residential developments and complex institutional projects. Recently completed Post-Graduate Certificate in Construction Management (George Brown College, Dean's Honour, 3.89 GPA) with specialized training in Canadian estimating practices. Proven ability to manage strategic pricing decisions for multimillion-dollar projects while coordinating with executives, clients, and consultant teams. <strong>PMP® Certified</strong> with demonstrated success in meeting challenging deadlines under pressure and delivering accurate, competitive estimates for diverse project types.</p>
    </div>

    <div class="section">
        <div class="section-title">Core Competencies</div>
        <div class="competency"><strong>Strategic Cost Estimation:</strong> Comprehensive pricing strategy development for projects up to $27M</div>
        <div class="competency"><strong>High-Rise Project Experience:</strong> Extensive background with multi-story residential and mixed-use developments</div>
        <div class="competency"><strong>Executive & Client Relations:</strong> Proven ability to interface with senior leadership, investors, and client representatives</div>
        <div class="competency"><strong>Software Proficiency:</strong> Advanced Excel, AutoCAD, MS Project; experience with construction management platforms</div>
        <div class="competency"><strong>Risk Assessment:</strong> Strategic evaluation of project-specific constraints and market conditions</div>
        <div class="competency"><strong>Deadline Management:</strong> Consistent delivery under pressure with strong organizational and prioritization skills</div>
    </div>

    <div class="section">
        <div class="section-title">Canadian Estimating Experience</div>
        <div class="job-title">Estimator (Co-Op Program)</div>
        <div class="company">SKYGRiD Corporate HQ - Mississauga, Canada</div>
        <div class="date">September 2024 - December 2024</div>
        <div class="achievement">• <strong>Managed strategic pricing decisions</strong> for major projects including $8.39M Decathlon commercial facility, coordinating with senior management to develop competitive and accurate pricing strategies</div>
        <div class="achievement">• <strong>Led high-rise residential project estimates</strong> including Lakeview Phase 1 (35 stories, 360 units), 17175 Yonge Street (208 units), and 6071 Azure Road (330 units), conducting comprehensive quantity take-offs using advanced software tools</div>
        <div class="achievement">• <strong>Coordinated with project stakeholders</strong> including executives, consultants, and client representatives to establish project priorities and ensure alignment with company and client requirements</div>
        <div class="achievement">• <strong>Developed detailed cost analysis</strong> for complex building components using Bluebeam and ConstructConnect, ensuring accurate material, labor, and equipment pricing for competitive bid positioning</div>
        <div class="achievement">• <strong>Managed multiple concurrent estimates</strong> under tight deadlines, demonstrating strong organizational skills and ability to prioritize tasks effectively</div>
        <div class="achievement">• <strong>Conducted comprehensive project reviews</strong> analyzing drawings, specifications, and tender documents to identify scope requirements and potential cost impacts</div>
    </div>

    <div class="section">
        <div class="section-title">Professional Construction Experience</div>
        <div class="job-title">Construction Executive & Project Manager</div>
        <div class="company">DECIVIL Construction - International Operations</div>
        <div class="date">May 2001 - December 2022</div>
        
        <div class="subsection">
            <strong>High-Rise & Complex Project Leadership:</strong>
            
            <div style="margin: 8px 0;">
                <strong>Park Taipas High-Rise Development</strong> (16-story, 126 units, 8,182 m², $27M, 2019-2022)
                <div class="achievement">• <strong>Led strategic cost planning</strong> from initial feasibility through construction completion, managing comprehensive budget development and cost control processes</div>
                <div class="achievement">• <strong>Coordinated with executive stakeholders</strong> including investors, municipal authorities, and senior management to ensure project alignment with strategic objectives</div>
                <div class="achievement">• <strong>Managed complex project scheduling</strong> integrating design development, approval processes, and construction phases to meet challenging delivery deadlines</div>
            </div>
            
            <div style="margin: 8px 0;">
                <strong>New Life Taipas Residential Complex</strong> (4 buildings, 80 units, 4,322 m², $10M, 2016-2019)
                <div class="achievement">• <strong>Developed comprehensive project budgets</strong> analyzing all construction components to provide accurate cost projections for investment decision-making</div>
                <div class="achievement">• <strong>Coordinated multidisciplinary consultant teams</strong> ensuring design feasibility and cost optimization throughout development process</div>
            </div>
        </div>
        
        <div class="subsection">
            <strong>Additional Project Portfolio:</strong>
            <div class="achievement">• Successfully delivered 15+ projects with combined value exceeding $75M</div>
            <div class="achievement">• Managed strategic pricing for diverse project types including residential, institutional, and commercial developments</div>
            <div class="achievement">• Coordinated with financial institutions and executive teams throughout project lifecycles</div>
        </div>
        
        <div class="subsection">
            <strong>Key Achievements:</strong>
            <div class="achievement">• Consistently delivered projects within approved budgets through accurate initial cost estimation</div>
            <div class="achievement">• Successfully coordinated complex projects under challenging deadlines and market pressures</div>
            <div class="achievement">• Built strategic relationships with consultants, suppliers, and executive stakeholders</div>
            <div class="achievement">• Developed standardized cost estimation processes enhancing accuracy and competitive positioning</div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Education & Specialized Training</div>
        
        <div style="margin-bottom: 15px;">
            <div class="job-title">Post-Graduate Certificate in Construction Management</div>
            <div class="company">George Brown College, Toronto, Canada</div>
            <div class="date">January 2024 - December 2024 | Dean's Honour (GPA: 3.89)</div>
            
            <div style="margin-top: 5px;">
                <strong>Advanced Estimating Coursework:</strong>
                <div class="course">• <strong>BLDG 1174 - Construction Plans & Estimating I:</strong> Grade A (4.0)</div>
                <div class="course">• <strong>BLDG 1186 - Construction Plans & Estimating II:</strong> Grade A+ (4.0)</div>
                <div class="course">• <strong>Ontario Building Code:</strong> Grade A (4.0) - Critical for high-rise residential projects</div>
                <div class="course">• <strong>Construction Contract Law:</strong> Grade A+ (4.0) - Essential for strategic pricing decisions</div>
                <div class="course">• <strong>Construction Project Planning & Scheduling:</strong> Grade A- (3.7)</div>
            </div>
        </div>
        
        <div style="margin-bottom: 10px;">
            <div class="job-title">Certificate in Electrical Techniques</div>
            <div class="company">George Brown College, Toronto, Canada</div>
            <div class="date">May 2023 - December 2023 | Dean's Honour (GPA: 3.74)</div>
        </div>
        
        <div style="margin-bottom: 10px;">
            <div class="job-title">Civil Engineering Degree</div>
            <div class="company">Accredited International Institution</div>
            <div style="font-size: 10px; color: #666;">Technical foundation supporting comprehensive construction cost analysis</div>
        </div>
        
        <div>
            <div class="job-title">Business Administration Post-Graduate</div>
            <div class="company">Accredited International Institution</div>
            <div style="font-size: 10px; color: #666;">Strategic business and financial management expertise</div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Technical Skills & Certifications</div>
        
        <div class="subsection">
            <strong>Professional Certifications:</strong>
            <div>• PMP® Certification – Project Management Institute (PMI), 2025</div>
            <div>• WHMIS Certification – Workplace Hazardous Materials Information System</div>
        </div>
        
        <div class="subsection">
            <strong>Software Proficiency:</strong>
            <div>• <strong>Construction Software:</strong> Bluebeam (Advanced), ConstructConnect, BuildingConnected</div>
            <div>• <strong>Project Management:</strong> MS Project, advanced scheduling and resource allocation</div>
            <div>• <strong>Financial Analysis:</strong> MS Excel (Advanced formulas, pivot tables, financial modeling)</div>
            <div>• <strong>Technical Design:</strong> AutoCAD, blueprint interpretation, specification analysis</div>
            <div>• <strong>Communication:</strong> MS Office Suite, presentation development for executive briefings</div>
        </div>
        
        <div class="subsection">
            <strong>Industry Knowledge:</strong>
            <div>• High-rise residential construction methods and systems</div>
            <div>• GTA market conditions and supplier networks</div>
            <div>• Construction cost coding systems and database management</div>
            <div>• Strategic pricing methodologies for competitive positioning</div>
        </div>
    </div>

    <div class="section">
        <div class="section-title">Additional Information</div>
        <div>• <strong>Location:</strong> Downtown Toronto with reliable transportation for GTA project sites and client meetings</div>
        <div>• <strong>Communication:</strong> Fluent English with strong written and oral presentation abilities</div>
        <div>• <strong>Availability:</strong> Immediate availability for full-time position</div>
        <div>• <strong>Professional Approach:</strong> Committed to integrity, accuracy, and collaborative stakeholder relationships</div>
        <div>• <strong>Industry Focus:</strong> Specialized interest in high-rise residential development within the Greater Toronto Area</div>
    </div>
</body>
</html>'''
    
    html_file = Path("elie_resume.html")
    html_file.write_text(html_content, encoding='utf-8')
    print(f"✅ HTML file created: {html_file.absolute()}")
    return html_file

def generate_pdf(html_file):
    """Generate PDF from HTML file using weasyprint"""
    try:
        from weasyprint import HTML, CSS
        
        # Define output file
        pdf_file = Path("Elie_Georges_Kfouri_Resume.pdf")
        
        # Generate PDF
        print("🔄 Generating PDF...")
        HTML(filename=str(html_file)).write_pdf(str(pdf_file))
        
        print(f"✅ PDF generated successfully: {pdf_file.absolute()}")
        return pdf_file
        
    except ImportError:
        print("❌ weasyprint not available. Trying alternative method...")
        return generate_pdf_alternative(html_file)
    except Exception as e:
        print(f"❌ Error generating PDF with weasyprint: {e}")
        return generate_pdf_alternative(html_file)

def generate_pdf_alternative(html_file):
    """Alternative PDF generation using wkhtmltopdf if available"""
    try:
        pdf_file = Path("Elie_Georges_Kfouri_Resume.pdf")
        
        # Try wkhtmltopdf
        cmd = [
            "wkhtmltopdf",
            "--page-size", "A4",
            "--margin-top", "20mm",
            "--margin-bottom", "20mm", 
            "--margin-left", "20mm",
            "--margin-right", "20mm",
            "--encoding", "UTF-8",
            str(html_file),
            str(pdf_file)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ PDF generated successfully with wkhtmltopdf: {pdf_file.absolute()}")
            return pdf_file
        else:
            print(f"❌ wkhtmltopdf failed: {result.stderr}")
            return None
            
    except FileNotFoundError:
        print("❌ wkhtmltopdf not found. Please install it or use weasyprint.")
        print("💡 Install instructions:")
        print("   - Ubuntu/Debian: sudo apt-get install wkhtmltopdf")
        print("   - macOS: brew install wkhtmltopdf") 
        print("   - Or install weasyprint: pip install weasyprint")
        return None
    except Exception as e:
        print(f"❌ Error with alternative PDF generation: {e}")
        return None

def main():
    """Main function to generate PDF resume"""
    print("📄 PDF Resume Generator")
    print("=" * 50)
    
    # Install dependencies
    if not install_dependencies():
        print("⚠️  Dependencies installation failed. Continuing with existing packages...")
    
    # Create HTML file
    html_file = create_html_file()
    
    # Generate PDF
    pdf_file = generate_pdf(html_file)
    
    if pdf_file and pdf_file.exists():
        print("\n🎉 SUCCESS!")
        print(f"📄 Resume PDF created: {pdf_file.absolute()}")
        print(f"📁 File size: {pdf_file.stat().st_size / 1024:.1f} KB")
        
        # Clean up HTML file
        try:
            html_file.unlink()
            print("🧹 Temporary HTML file removed")
        except:
            pass
            
    else:
        print("\n❌ PDF generation failed!")
        print(f"📄 HTML file available at: {html_file.absolute()}")
        print("💡 You can manually convert the HTML to PDF using:")
        print(f"   - Browser: Open {html_file.absolute()} and print to PDF")
        print(f"   - Online tools: Upload the HTML file to online PDF converters")

if __name__ == "__main__":
    main()
