from django.shortcuts import render
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse

def generate_pdf_bill(request):
    template_path = 'invoice_template.html'
    
    items = [
        {'name': 'Product A', 'quantity': 2, 'price': 50},
        {'name': 'Product B', 'quantity': 1, 'price': 80},
    ]

    # Add per-item total
    for item in items:
        item['total'] = item['quantity'] * item['price']

    context = {
        'customer_name': 'John Doe',
        'invoice_number': 'INV-001',
        'date': '2025-05-26',
        'items': items,
        'total': sum(item['total'] for item in items),
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def preview_invoice(request):
    items = [
        {'name': 'Product A', 'quantity': 2, 'price': 50},
        {'name': 'Product B', 'quantity': 1, 'price': 80},
    ]

    for item in items:
        item['total'] = item['quantity'] * item['price']

    context = {
        'customer_name': 'John Doe',
        'invoice_number': 'INV-001',
        'date': '2025-05-26',
        'items': items,
        'total': sum(item['total'] for item in items),
    }

    return render(request, 'invoice_template.html', context)

