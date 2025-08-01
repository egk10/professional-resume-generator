#!/usr/bin/env python3
"""
Enhanced PDF Resume Generator with better formatting
"""

from pathlib import Path
import subprocess
import sys

def create_professional_html():
    """Create a professional HTML resume optimized for PDF generation"""
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Elie Georges Kfouri - Construction Estimator</title>
    <style>
        @page {
            size: A4;
            margin: 1.5cm;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Calibri', 'Arial', sans-serif;
            line-height: 1.4;
            color: #2c3e50;
            font-size: 10.5px;
        }
        
        .container {
            max-width: 100%;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            border-bottom: 3px solid #34495e;
            padding-bottom: 12px;
            margin-bottom: 18px;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 15px;
            border-radius: 5px;
        }
        
        .name {
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 8px;
            color: #2c3e50;
            letter-spacing: 1px;
        }
        
        .contact {
            font-size: 10px;
            color: #5a6c7d;
            line-height: 1.3;
        }
        
        .contact strong {
            color: #34495e;
        }
        
        .section {
            margin-bottom: 16px;
            page-break-inside: avoid;
        }
        
        .section-title {
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 4px;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .job-title {
            font-weight: bold;
            font-size: 12px;
            color: #2c3e50;
            margin-bottom: 2px;
        }
        
        .company {
            font-style: italic;
            color: #3498db;
            font-size: 11px;
            margin-bottom: 3px;
        }
        
        .date {
            font-style: italic;
            font-size: 9px;
            color: #7f8c8d;
            margin-bottom: 8px;
        }
        
        .achievement {
            margin: 3px 0;
            padding-left: 12px;
            position: relative;
            line-height: 1.3;
        }
        
        .achievement::before {
            content: "•";
            color: #3498db;
            font-weight: bold;
            position: absolute;
            left: 0;
        }
        
        .subsection {
            margin: 8px 0;
        }
        
        .competency {
            margin: 3px 0;
            padding-left: 12px;
            position: relative;
        }
        
        .competency::before {
            content: "▶";
            color: #e74c3c;
            font-size: 8px;
            position: absolute;
            left: 0;
            top: 2px;
        }
        
        .course {
            margin: 2px 0;
            font-size: 9px;
            padding-left: 15px;
        }
        
        .highlight {
            background: linear-gradient(120deg, #fff3cd 0%, #fff3cd 100%);
            padding: 2px 4px;
            border-radius: 3px;
        }
        
        .professional-summary {
            background: #f8f9fa;
            padding: 12px;
            border-left: 4px solid #3498db;
            border-radius: 0 5px 5px 0;
            margin-bottom: 18px;
        }
        
        .two-column {
            display: flex;
            gap: 20px;
        }
        
        .column {
            flex: 1;
        }
        
        .skills-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-top: 8px;
        }
        
        .skill-item {
            background: #ecf0f1;
            padding: 6px 8px;
            border-radius: 4px;
            font-size: 9px;
            border-left: 3px solid #3498db;
        }
        
        @media print {
            body { 
                margin: 0;
                font-size: 10px;
            }
            .no-print { display: none; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="name">ELIE GEORGES KFOURI</div>
            <div class="contact">
                <strong>Construction Estimator</strong> | <strong>PMP® Certified</strong><br>
                📧 eliegkfouri@gmail.com | 📱 437-655-1527 | 📍 Toronto, ON M5V 3K8<br>
                🔗 linkedin.com/in/elie-kfouri
            </div>
        </div>

        <div class="section">
            <div class="section-title">Professional Summary</div>
            <div class="professional-summary">
                <strong>PMP® Certified Construction Professional</strong> with extensive experience in cost estimation and project management, specializing in <strong>high-rise residential developments</strong> and complex institutional projects. Recently completed <strong>Post-Graduate Certificate in Construction Management</strong> (George Brown College, Dean's Honour, 3.89 GPA) with specialized training in Canadian estimating practices. Proven ability to manage strategic pricing decisions for <strong>multimillion-dollar projects</strong> while coordinating with executives, clients, and consultant teams.
            </div>
        </div>

        <div class="section">
            <div class="section-title">Core Competencies</div>
            <div class="skills-grid">
                <div class="skill-item"><strong>Strategic Cost Estimation</strong><br>Projects up to $27M</div>
                <div class="skill-item"><strong>High-Rise Expertise</strong><br>Multi-story residential</div>
                <div class="skill-item"><strong>Executive Relations</strong><br>Senior stakeholder management</div>
                <div class="skill-item"><strong>Software Proficiency</strong><br>Bluebeam, ConstructConnect</div>
                <div class="skill-item"><strong>Risk Assessment</strong><br>Market & project constraints</div>
                <div class="skill-item"><strong>Deadline Management</strong><br>Pressure & prioritization</div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Canadian Estimating Experience</div>
            <div class="job-title">Construction Estimator (Co-Op Program)</div>
            <div class="company">SKYGRiD Corporate HQ - Mississauga, Canada</div>
            <div class="date">September 2024 - December 2024</div>
            
            <div class="achievement"><strong>Strategic Pricing Leadership:</strong> Managed pricing decisions for <span class="highlight">$8.39M Decathlon commercial facility</span>, coordinating with senior management for competitive positioning</div>
            <div class="achievement"><strong>High-Rise Residential Projects:</strong> Led estimates for major developments including <span class="highlight">Lakeview Phase 1 (35 stories, 360 units)</span>, 17175 Yonge Street (208 units), and 6071 Azure Road (330 units)</div>
            <div class="achievement"><strong>Stakeholder Coordination:</strong> Interfaced with executives, consultants, and clients to establish priorities and ensure alignment with requirements</div>
            <div class="achievement"><strong>Advanced Cost Analysis:</strong> Developed detailed component analysis using Bluebeam and ConstructConnect for accurate material, labor, and equipment pricing</div>
            <div class="achievement"><strong>Multi-Project Management:</strong> Successfully managed concurrent estimates under tight deadlines with strong organizational prioritization</div>
        </div>

        <div class="section">
            <div class="section-title">Professional Construction Experience</div>
            <div class="job-title">Construction Executive & Project Manager</div>
            <div class="company">DECIVIL Construction - International Operations</div>
            <div class="date">May 2001 - December 2022 (21+ Years Experience)</div>
            
            <div class="subsection">
                <strong>Major Project Leadership:</strong>
                
                <div style="margin: 6px 0; padding: 8px; background: #f8f9fa; border-radius: 4px;">
                    <strong>🏢 Park Taipas High-Rise Development</strong><br>
                    <em>16-story | 126 units | 8,182 m² | $27M | 2019-2022</em>
                    <div class="achievement">Led strategic cost planning from feasibility through completion</div>
                    <div class="achievement">Coordinated with investors, municipal authorities, and senior management</div>
                    <div class="achievement">Managed complex scheduling integrating design, approvals, and construction</div>
                </div>
                
                <div style="margin: 6px 0; padding: 8px; background: #f8f9fa; border-radius: 4px;">
                    <strong>🏘️ New Life Taipas Residential Complex</strong><br>
                    <em>4 buildings | 80 units | 4,322 m² | $10M | 2016-2019</em>
                    <div class="achievement">Developed comprehensive project budgets for investment decision-making</div>
                    <div class="achievement">Coordinated multidisciplinary consultant teams for cost optimization</div>
                </div>
            </div>
            
            <div class="subsection">
                <strong>Portfolio Achievements:</strong>
                <div class="achievement">Successfully delivered <strong>15+ projects</strong> with combined value exceeding <strong>$75M</strong></div>
                <div class="achievement">Consistently delivered projects within approved budgets through accurate estimation</div>
                <div class="achievement">Built strategic relationships with consultants, suppliers, and executive stakeholders</div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Education & Certifications</div>
            
            <div style="margin-bottom: 12px; padding: 8px; background: #e8f5e8; border-radius: 4px;">
                <div class="job-title">🎓 Post-Graduate Certificate in Construction Management</div>
                <div class="company">George Brown College, Toronto, Canada</div>
                <div class="date">January 2024 - December 2024 | <strong>Dean's Honour (GPA: 3.89)</strong></div>
                
                <div style="margin-top: 6px;">
                    <strong>Key Coursework:</strong>
                    <div class="course">• Construction Plans & Estimating I & II: <strong>Grade A/A+</strong></div>
                    <div class="course">• Ontario Building Code: <strong>Grade A</strong></div>
                    <div class="course">• Construction Contract Law: <strong>Grade A+</strong></div>
                </div>
            </div>
            
            <div style="margin-bottom: 8px;">
                <div class="job-title">🏆 PMP® Certification</div>
                <div class="company">Project Management Institute (PMI) - 2025</div>
            </div>
            
            <div style="margin-bottom: 8px;">
                <div class="job-title">⚡ Certificate in Electrical Techniques</div>
                <div class="company">George Brown College - Dean's Honour (GPA: 3.74)</div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Technical Skills & Software</div>
            
            <div class="two-column">
                <div class="column">
                    <strong>🔧 Construction Software:</strong>
                    <div class="achievement">Bluebeam (Advanced)</div>
                    <div class="achievement">ConstructConnect</div>
                    <div class="achievement">BuildingConnected</div>
                    <div class="achievement">AutoCAD</div>
                    
                    <strong style="margin-top: 8px; display: block;">📊 Analysis & Management:</strong>
                    <div class="achievement">MS Excel (Advanced modeling)</div>
                    <div class="achievement">MS Project</div>
                    <div class="achievement">Financial Analysis</div>
                </div>
                
                <div class="column">
                    <strong>🏗️ Industry Expertise:</strong>
                    <div class="achievement">High-rise residential construction</div>
                    <div class="achievement">GTA market conditions</div>
                    <div class="achievement">Cost coding systems</div>
                    <div class="achievement">Strategic pricing methodologies</div>
                    
                    <strong style="margin-top: 8px; display: block;">📋 Certifications:</strong>
                    <div class="achievement">WHMIS Certified</div>
                    <div class="achievement">Blueprint Interpretation</div>
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Professional Profile</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div>
                    <strong>🎯 Specialization:</strong>
                    <div class="achievement">High-rise residential development in GTA</div>
                    <div class="achievement">Commercial & institutional projects</div>
                    
                    <strong style="margin-top: 6px; display: block;">📍 Location & Availability:</strong>
                    <div class="achievement">Downtown Toronto resident</div>
                    <div class="achievement">Immediate availability</div>
                </div>
                
                <div>
                    <strong>💼 Professional Approach:</strong>
                    <div class="achievement">Integrity & accuracy focused</div>
                    <div class="achievement">Collaborative stakeholder relationships</div>
                    
                    <strong style="margin-top: 6px; display: block;">🗣️ Communication:</strong>
                    <div class="achievement">Fluent English (written & oral)</div>
                    <div class="achievement">Executive presentation skills</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>'''
    
    html_file = Path("elie_resume_professional.html")
    html_file.write_text(html_content, encoding='utf-8')
    print(f"✅ Professional HTML file created: {html_file.absolute()}")
    return html_file

def generate_professional_pdf(html_file):
    """Generate a professional PDF with optimized settings"""
    try:
        pdf_file = Path("Elie_Georges_Kfouri_Professional_Resume.pdf")
        
        # Enhanced wkhtmltopdf settings for professional output
        cmd = [
            "wkhtmltopdf",
            "--page-size", "A4",
            "--margin-top", "15mm",
            "--margin-bottom", "15mm", 
            "--margin-left", "15mm",
            "--margin-right", "15mm",
            "--encoding", "UTF-8",
            "--print-media-type",
            "--disable-smart-shrinking",
            "--dpi", "300",
            "--image-quality", "100",
            str(html_file),
            str(pdf_file)
        ]
        
        print("🔄 Generating professional PDF with enhanced settings...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Professional PDF generated: {pdf_file.absolute()}")
            return pdf_file
        else:
            print(f"❌ Error: {result.stderr}")
            return None
            
    except Exception as e:
        print(f"❌ Error generating professional PDF: {e}")
        return None

def main():
    """Generate professional PDF resume"""
    print("🎨 Professional PDF Resume Generator")
    print("=" * 60)
    
    # Create professional HTML
    html_file = create_professional_html()
    
    # Generate professional PDF
    pdf_file = generate_professional_pdf(html_file)
    
    if pdf_file and pdf_file.exists():
        print("\n🎉 SUCCESS!")
        print(f"📄 Professional Resume PDF: {pdf_file.absolute()}")
        print(f"📁 File size: {pdf_file.stat().st_size / 1024:.1f} KB")
        
        # Keep HTML for reference
        print(f"📋 HTML source available: {html_file.absolute()}")
        
        print("\n💡 Features included:")
        print("  ✓ Professional formatting with colors")
        print("  ✓ High-resolution (300 DPI)")
        print("  ✓ Optimized for ATS systems")
        print("  ✓ Clean, modern design")
        print("  ✓ Strategic keyword placement")
        
    else:
        print("\n❌ Professional PDF generation failed!")

if __name__ == "__main__":
    main()
