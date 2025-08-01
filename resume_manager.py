#!/usr/bin/env python3
"""
Resume Summary and File Management
"""

from pathlib import Path
import subprocess

def create_summary():
    """Create a summary of generated resume files"""
    print("📋 RESUME FILES GENERATED")
    print("=" * 60)
    
    files = [
        {
            "name": "Elie_Georges_Kfouri_Resume.pdf",
            "description": "Standard professional resume",
            "best_for": "General applications, email attachments",
            "size": "Small (38KB)"
        },
        {
            "name": "Elie_Georges_Kfouri_Professional_Resume.pdf", 
            "description": "Enhanced professional resume with colors",
            "best_for": "High-end positions, executive roles",
            "size": "Medium (75KB)"
        },
        {
            "name": "elie_resume_professional.html",
            "description": "HTML source file",
            "best_for": "Web portfolios, easy editing",
            "size": "Text file"
        }
    ]
    
    for i, file_info in enumerate(files, 1):
        file_path = Path(file_info["name"])
        exists = "✅ Available" if file_path.exists() else "❌ Missing"
        
        print(f"\n{i}. {file_info['name']}")
        print(f"   Status: {exists}")
        print(f"   Description: {file_info['description']}")
        print(f"   Best for: {file_info['best_for']}")
        print(f"   Size: {file_info['size']}")
    
    print(f"\n📁 All files located in:")
    print(f"   {Path.cwd()}")
    
    return files

def generate_ats_optimized():
    """Generate an ATS-optimized plain text version"""
    ats_content = """ELIE GEORGES KFOURI
Construction Estimator | PMP Certified
Email: eliegkfouri@gmail.com | Phone: 437-655-1527
Location: Toronto, ON M5V 3K8 | LinkedIn: linkedin.com/in/elie-kfouri

PROFESSIONAL SUMMARY
PMP Certified Construction Professional with extensive experience in cost estimation and project management, specializing in high-rise residential developments and complex institutional projects. Recently completed Post-Graduate Certificate in Construction Management (George Brown College, Dean's Honour, 3.89 GPA) with specialized training in Canadian estimating practices. Proven ability to manage strategic pricing decisions for multimillion-dollar projects while coordinating with executives, clients, and consultant teams.

CORE COMPETENCIES
- Strategic Cost Estimation: Comprehensive pricing strategy development for projects up to $27M
- High-Rise Project Experience: Extensive background with multi-story residential and mixed-use developments  
- Executive & Client Relations: Proven ability to interface with senior leadership, investors, and client representatives
- Software Proficiency: Advanced Excel, AutoCAD, MS Project, Bluebeam, ConstructConnect
- Risk Assessment: Strategic evaluation of project-specific constraints and market conditions
- Deadline Management: Consistent delivery under pressure with strong organizational and prioritization skills

CANADIAN ESTIMATING EXPERIENCE

Construction Estimator (Co-Op Program)
SKYGRiD Corporate HQ - Mississauga, Canada
September 2024 - December 2024

- Managed strategic pricing decisions for major projects including $8.39M Decathlon commercial facility, coordinating with senior management to develop competitive and accurate pricing strategies
- Led high-rise residential project estimates including Lakeview Phase 1 (35 stories, 360 units), 17175 Yonge Street (208 units), and 6071 Azure Road (330 units), conducting comprehensive quantity take-offs using advanced software tools
- Coordinated with project stakeholders including executives, consultants, and client representatives to establish project priorities and ensure alignment with company and client requirements
- Developed detailed cost analysis for complex building components using Bluebeam and ConstructConnect, ensuring accurate material, labor, and equipment pricing for competitive bid positioning
- Managed multiple concurrent estimates under tight deadlines, demonstrating strong organizational skills and ability to prioritize tasks effectively
- Conducted comprehensive project reviews analyzing drawings, specifications, and tender documents to identify scope requirements and potential cost impacts

PROFESSIONAL CONSTRUCTION EXPERIENCE

Construction Executive & Project Manager
DECIVIL Construction - International Operations
May 2001 - December 2022

High-Rise & Complex Project Leadership:

Park Taipas High-Rise Development (16-story, 126 units, 8,182 m², $27M, 2019-2022)
- Led strategic cost planning from initial feasibility through construction completion, managing comprehensive budget development and cost control processes
- Coordinated with executive stakeholders including investors, municipal authorities, and senior management to ensure project alignment with strategic objectives
- Managed complex project scheduling integrating design development, approval processes, and construction phases to meet challenging delivery deadlines

New Life Taipas Residential Complex (4 buildings, 80 units, 4,322 m², $10M, 2016-2019)
- Developed comprehensive project budgets analyzing all construction components to provide accurate cost projections for investment decision-making
- Coordinated multidisciplinary consultant teams ensuring design feasibility and cost optimization throughout development process

Additional Project Portfolio:
- Successfully delivered 15+ projects with combined value exceeding $75M
- Managed strategic pricing for diverse project types including residential, institutional, and commercial developments
- Coordinated with financial institutions and executive teams throughout project lifecycles

Key Achievements:
- Consistently delivered projects within approved budgets through accurate initial cost estimation
- Successfully coordinated complex projects under challenging deadlines and market pressures
- Built strategic relationships with consultants, suppliers, and executive stakeholders
- Developed standardized cost estimation processes enhancing accuracy and competitive positioning

EDUCATION & SPECIALIZED TRAINING

Post-Graduate Certificate in Construction Management
George Brown College, Toronto, Canada
January 2024 - December 2024 | Dean's Honour (GPA: 3.89)

Advanced Estimating Coursework:
- BLDG 1174 - Construction Plans & Estimating I: Grade A (4.0)
- BLDG 1186 - Construction Plans & Estimating II: Grade A+ (4.0)
- Ontario Building Code: Grade A (4.0) - Critical for high-rise residential projects
- Construction Contract Law: Grade A+ (4.0) - Essential for strategic pricing decisions
- Construction Project Planning & Scheduling: Grade A- (3.7)

Certificate in Electrical Techniques
George Brown College, Toronto, Canada
May 2023 - December 2023 | Dean's Honour (GPA: 3.74)

Civil Engineering Degree
Accredited International Institution
Technical foundation supporting comprehensive construction cost analysis

Business Administration Post-Graduate
Accredited International Institution
Strategic business and financial management expertise

TECHNICAL SKILLS & CERTIFICATIONS

Professional Certifications:
- PMP Certification – Project Management Institute (PMI), 2025
- WHMIS Certification – Workplace Hazardous Materials Information System

Software Proficiency:
- Construction Software: Bluebeam (Advanced), ConstructConnect, BuildingConnected
- Project Management: MS Project, advanced scheduling and resource allocation
- Financial Analysis: MS Excel (Advanced formulas, pivot tables, financial modeling)
- Technical Design: AutoCAD, blueprint interpretation, specification analysis
- Communication: MS Office Suite, presentation development for executive briefings

Industry Knowledge:
- High-rise residential construction methods and systems
- GTA market conditions and supplier networks
- Construction cost coding systems and database management
- Strategic pricing methodologies for competitive positioning

ADDITIONAL INFORMATION
- Location: Downtown Toronto with reliable transportation for GTA project sites and client meetings
- Communication: Fluent English with strong written and oral presentation abilities
- Availability: Immediate availability for full-time position
- Professional Approach: Committed to integrity, accuracy, and collaborative stakeholder relationships
- Industry Focus: Specialized interest in high-rise residential development within the Greater Toronto Area"""

    txt_file = Path("Elie_Georges_Kfouri_ATS_Resume.txt")
    txt_file.write_text(ats_content, encoding='utf-8')
    
    print(f"\n✅ ATS-Optimized Text Resume Created:")
    print(f"   📄 {txt_file.absolute()}")
    print(f"   📁 Size: {txt_file.stat().st_size / 1024:.1f} KB")
    print(f"   💡 Use for: ATS systems, online applications, plain text submissions")
    
    return txt_file

def show_usage_recommendations():
    """Show recommendations for different use cases"""
    print(f"\n🎯 USAGE RECOMMENDATIONS")
    print("=" * 60)
    
    recommendations = [
        {
            "scenario": "🏢 General Job Applications",
            "file": "Elie_Georges_Kfouri_Resume.pdf",
            "reason": "Clean, professional, widely compatible"
        },
        {
            "scenario": "💼 Executive/Senior Positions", 
            "file": "Elie_Georges_Kfouri_Professional_Resume.pdf",
            "reason": "Enhanced design, visual appeal, premium look"
        },
        {
            "scenario": "🤖 ATS/Online Applications",
            "file": "Elie_Georges_Kfouri_ATS_Resume.txt", 
            "reason": "Plain text, keyword optimized, ATS-friendly"
        },
        {
            "scenario": "📧 Email Attachments",
            "file": "Elie_Georges_Kfouri_Resume.pdf",
            "reason": "Small file size, fast loading"
        },
        {
            "scenario": "🌐 Portfolio/Website",
            "file": "elie_resume_professional.html",
            "reason": "Web-friendly, easily customizable"
        }
    ]
    
    for rec in recommendations:
        print(f"\n{rec['scenario']}")
        print(f"   📎 Use: {rec['file']}")
        print(f"   💡 Why: {rec['reason']}")

def main():
    """Main function to summarize all resume files"""
    # Create summary
    files = create_summary()
    
    # Generate ATS version
    generate_ats_optimized()
    
    # Show usage recommendations
    show_usage_recommendations()
    
    print(f"\n🎉 COMPLETE RESUME PACKAGE READY!")
    print("=" * 60)
    print("✅ Standard PDF Resume")
    print("✅ Professional PDF Resume") 
    print("✅ ATS-Optimized Text Resume")
    print("✅ HTML Source File")
    print("✅ Usage Guidelines")
    
    print(f"\n📋 Quick Actions:")
    print("• Copy files to desired location")
    print("• Use appropriate version for each application")
    print("• Customize HTML for specific opportunities")
    print("• Keep ATS version for online portals")

if __name__ == "__main__":
    main()
