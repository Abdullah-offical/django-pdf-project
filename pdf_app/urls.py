from django.urls import path
from . import views

urlpatterns = [
    path('pdf-to-word/', views.pdf_to_word, name='pdf_to_word'),
    path('pdf-to-csv/', views.pdf_to_csv, name='pdf_to_csv'),
    path('marge-pdf/', views.marge_pdf, name='marge_pdf'),
    path('split-form/', views.split_form, name='split_form'),
    path('pdf-lock/', views.pdf_lock, name='pdf_lock'),
    path('pdf-unlock/', views.pdf_unlock, name='pdf_unlock'),
]