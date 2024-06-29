from django.shortcuts import render
from .forms import Pdf2WordForm

def pdf_to_word(request):
    if request.method == 'POST':
        return
    else:
        form = Pdf2WordForm()
        context = {
            'form' : form
        }
        return render(request, 'pdf/pdf_to_word.html', context)
