from django.urls import path
from PDF_construct import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.pdf_html, name="pdf_html"),
    path("pdf", views.pdf,  name="pdf")
]

urlpatterns += staticfiles_urlpatterns()