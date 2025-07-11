
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas

def generate_certificate(name, course):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 750, f"Certificate of Completion")
    c.drawString(100, 700, f"This certifies that {name} completed {course}")
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='certificate.pdf')
