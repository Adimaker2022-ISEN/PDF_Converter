from django.urls import path
from PDF_construct import views

urlpatterns = [
    path("", views.pdf_html, name="pdf_html"),
    path("pdf", views.pdf,  name="pdf")
]