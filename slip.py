import os
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

def generate_pdf_slip(filename, customer_name, invoice_no, items):
    # Setup the output file path and document template (Standard Letter size)
    doc = SimpleDocTemplate(
        filename, 
        pagesize=letter, 
        rightMargin=36, 
        leftMargin=36, 
        topMargin=36, 
        bottomMargin=36,
        title="Tax Invoice"
    )
    story = []
    styles = getSampleStyleSheet()
    
    # Custom typographical styles
    title_style = ParagraphStyle(
        'DocTitle', parent=styles['Heading1'], fontSize=22, 
        leading=26, textColor=colors.HexColor("#1A365D"), spaceAfter=15
    )
    meta_style = ParagraphStyle(
        'MetaText', parent=styles['Normal'], fontSize=10, 
        leading=14, textColor=colors.HexColor("#4A5568")
    )
    
    # Document Metadata Header
    story.append(Paragraph("<b>TAX INVOICE / BILL SLIP</b>", title_style))
    story.append(Paragraph(f"<b>Invoice No:</b> {invoice_no}", meta_style))
    story.append(Paragraph(f"<b>Customer Name:</b> {customer_name}", meta_style))
    story.append(Paragraph("<b>Date:</b> 2026-10-06", meta_style))
    story.append(Spacer(1, 15))
    
    # Prepare the table grid structure
    table_data = [["Item Description", "Qty", "Unit Price", "Total"]]
    
    subtotal = 0
    for item in items:
        total_price = item["qty"] * item["price"]
        subtotal += total_price
        table_data.append([
            item["name"], 
            str(item["qty"]), 
            f"INR {item['price']:.2f}", 
            f"INR {total_price:.2f}"
        ])
    
    # Calculate tax brackets (e.g., 18% GST)
    tax = subtotal * 0.18  
    grand_total = subtotal + tax
    
    # Append calculation rows
    table_data.append(["", "", "Subtotal:", f"INR {subtotal:.2f}"])
    table_data.append(["", "", "GST (18%):", f"INR {tax:.2f}"])
    table_data.append(["", "", "Grand Total:", f"INR {grand_total:.2f}"])
    
    # Set explicit column widths to span perfectly across the page layout
    bill_table = Table(table_data, colWidths=[260, 50, 110, 120])
    
    # Apply modern table grid styling rules
    bill_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1A365D")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('ALIGN', (0, 1), (0, -1), 'LEFT'),
        ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ('BACKGROUND', (0, 1), (-1, -4), colors.HexColor("#F7FAFC")),
        ('GRID', (0, 0), (-1, -4), 0.5, colors.HexColor("#E2E8F0")),
        ('FONTNAME', (2, -3), (-1, -1), 'Helvetica-Bold'),
        ('LINEABOVE', (2, -3), (3, -3), 1, colors.HexColor("#1A365D")),
    ]))
    
    story.append(bill_table)
    
    # Render and build the actual PDF binary file
    doc.build(story)
    print(f"Softcopy successfully generated as: {filename}")

# Sample Execution Dataset
order_items = [
    {"name": "Logitech MX Master 3S Mouse", "qty": 1, "price": 8995.00},
    {"name": "Keychron K2 Mechanical Keyboard", "qty": 1, "price": 7499.00},
    {"name": "USB-C Hub Multiport Adapter", "qty": 2, "price": 1850.00}
]

generate_pdf_slip("retail_bill_slip.pdf", "Rajesh Kumar", "INV-2026-0042", order_items)
