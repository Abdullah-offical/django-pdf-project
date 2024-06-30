from django.shortcuts import render
from .forms import Pdf2WordForm, Pdf2CSVForm, MergePdfForm, SplitForm, PDFLockForm, PDFUnlockForm

def pdf_to_word(request):
    if request.method == 'POST':
        return
    else:
        form = Pdf2WordForm()
        context = {
            'form' : form
        }
        return render(request, 'pdf/pdf_to_word.html', context)
    
def pdf_to_csv(request):
    if request.method == 'POST':
        return
    else:
        form = Pdf2CSVForm()
        context = {
            'form' : form
        }
        return render(request, 'pdf/pdf_to_csv.html', context)
    
def split_form(request):
    if request.method == 'POST':
        return
    else:
        form = SplitForm()
        context = {
            'form' : form
        }
        return render(request, 'pdf/split_form.html', context)


def marge_pdf(request):
    if request.method == 'POST':
        return
    else:
        form = MergePdfForm()
        context = {
            'form' : form
        }
        return render(request, 'pdf/marge_pdf.html', context)
    
def pdf_lock(request):
    if request.method == 'POST':
        return
    else:
        form = PDFLockForm()
        context = {
            'form' : form
        }
        return render(request, 'pdf/pdf_lock.html', context)
    
def pdf_unlock(request):
    if request.method == 'POST':
        return
    else:
        form = PDFUnlockForm()
        context = {
            'form' : form
        }
        return render(request, 'pdf/pdf_unlock.html', context)
