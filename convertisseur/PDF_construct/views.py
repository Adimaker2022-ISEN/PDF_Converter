from django.shortcuts import render
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse

# Create your views here.
def pdf (request):
     # Render the HTML template
    html = render_to_string('PDF_construct/facture.html')

    # Create a PDF file
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse("Error generating PDF", status=400)

def pdf_html (request):
    return render(request, 'PDF_construct/facture.html')