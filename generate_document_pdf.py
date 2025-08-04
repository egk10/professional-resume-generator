#!/usr/bin/env python3
"""
Document PDF Generator - Convert HTML documents to professional PDF
"""

import subprocess
import sys
from pathlib import Path
import argparse

def generate_pdf_from_html(html_file, output_file=None, document_type="legal"):
    """
    Generate PDF from HTML file with optimized settings for different document types
    
    Args:
        html_file (str): Path to HTML file
        output_file (str): Output PDF filename (optional)
        document_type (str): Type of document ("legal", "resume", "report")
    """
    html_path = Path(html_file)
    
    if not html_path.exists():
        print(f"❌ Error: HTML file '{html_file}' not found!")
        return False
    
    # Generate output filename if not provided
    if output_file is None:
        output_file = html_path.stem + ".pdf"
    
    pdf_path = Path(output_file)
    
    # Document-specific settings
    settings = {
        "legal": {
            "margin-top": "25mm",
            "margin-bottom": "20mm", 
            "margin-left": "30mm",
            "margin-right": "20mm",
            "dpi": "300"
        },
        "resume": {
            "margin-top": "15mm",
            "margin-bottom": "15mm",
            "margin-left": "15mm", 
            "margin-right": "15mm",
            "dpi": "300"
        },
        "report": {
            "margin-top": "20mm",
            "margin-bottom": "20mm",
            "margin-left": "20mm",
            "margin-right": "20mm", 
            "dpi": "300"
        }
    }
    
    # Get settings for document type
    doc_settings = settings.get(document_type, settings["legal"])
    
    # Build wkhtmltopdf command
    cmd = [
        "wkhtmltopdf",
        "--page-size", "A4",
        "--margin-top", doc_settings["margin-top"],
        "--margin-bottom", doc_settings["margin-bottom"],
        "--margin-left", doc_settings["margin-left"], 
        "--margin-right", doc_settings["margin-right"],
        "--encoding", "UTF-8",
        "--dpi", doc_settings["dpi"],
        "--image-quality", "100",
        str(html_path),
        str(pdf_path)
    ]
    
    try:
        print(f"🔄 Generating PDF from {html_file}...")
        print(f"📁 Document type: {document_type}")
        print(f"📄 Output: {pdf_path}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            file_size = pdf_path.stat().st_size / 1024
            print(f"✅ PDF generated successfully!")
            print(f"📁 File: {pdf_path.absolute()}")
            print(f"📏 Size: {file_size:.1f} KB")
            
            # Show any warnings (but not errors since generation was successful)
            if result.stderr and "is not support using unpatched qt" in result.stderr:
                print("ℹ️  Note: Some advanced features were ignored (this is normal)")
            
            return True
        else:
            print(f"❌ Error generating PDF:")
            print(f"   {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ Error: wkhtmltopdf not found. Please install it:")
        print("   sudo apt-get install wkhtmltopdf")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(
        description="Generate PDF from HTML documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 generate_document_pdf.py perito.html
  python3 generate_document_pdf.py document.html --output report.pdf --type report
  python3 generate_document_pdf.py resume.html --type resume
        """
    )
    
    parser.add_argument("html_file", help="HTML file to convert")
    parser.add_argument("-o", "--output", help="Output PDF filename")
    parser.add_argument("-t", "--type", 
                       choices=["legal", "resume", "report"],
                       default="legal",
                       help="Document type (affects margins and formatting)")
    
    args = parser.parse_args()
    
    print("📄 Document PDF Generator")
    print("=" * 50)
    
    success = generate_pdf_from_html(args.html_file, args.output, args.type)
    
    if success:
        print("\n🎉 Success! PDF generated successfully.")
    else:
        print("\n❌ Failed to generate PDF.")
        sys.exit(1)

if __name__ == "__main__":
    main()
