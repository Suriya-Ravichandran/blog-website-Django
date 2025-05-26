from django.urls import path
from . import views

app_name= 'invoicegen'
urlpatterns = [

    path("invoice/pdf/",views.generate_pdf_bill,name="generate_pdf_bill"),
    path("invoice/preview/",views.preview_invoice,name="preview_invoice"),
]